from misgastos_app import app
from misgastos_app.controllers.users import login_required
from flask import render_template, redirect, request, session, flash, jsonify
from misgastos_app.models.categoria import Categoria
from misgastos_app.models.form import ioForm
from misgastos_app.models.item import Item
from misgastos_app.models.movimiento import Movimiento
from misgastos_app.models.tipopago import Tipopago


@app.route ('/iorecords', methods=['GET', 'POST'])
@login_required
def iorecords():
    ioform = ioForm()
    cio = {'cio': 0}
    idata = {'iio': 0, 'cid': 1, 'uid': session['uid']}
    ioform.mov_uid.data = session['uid']
    ioform.mov_cid.choices = [(categoria.cid, categoria.cname) for categoria in Categoria.get_all_by_cio(cio)]
    ioform.mov_iid.choices = [(item.iid, item.iname) for item in Item.get_all_by_iio_cid_uid(idata)]
    ioform.mov_tpid.choices = [(tipopago.tpid, tipopago.tpname) for tipopago in Tipopago.get_all()]
    if request.method == 'POST':
        ioform.mov_cid.choices = [(categoria.cid, categoria.cname) for categoria in Categoria.get_all_by_cio(session['cio'])]
        ioform.mov_iid.choices = [(item.iid, item.iname) for item in Item.get_all_by_iio_cid_uid(session['idata'])]
        if ioform.validate():
            Movimiento.save(ioform.data)
            flash ('Registro ingresado')
            return redirect ('/iorecords')
    return render_template('iorecords.html', ioform = ioform)

@app.route ('/cat/<cio>')
@login_required
def cat(cio):
    cio = {'cio':cio}
    session['cio'] = cio
    cats = Categoria.get_all_by_cio(cio)
    catArray = []
    for cat in cats:
        catDict = {}
        catDict['cid'] = cat.cid
        catDict['cname'] = cat.cname
        catArray.append(catDict)
    return jsonify ({'cats': catArray})

@app.route ('/item/<iio>/<cid>')
@login_required
def item(iio, cid):
    data = {'iio':iio, 'cid': cid, 'uid': session['uid']}
    session['idata'] = data
    items = Item.get_all_by_iio_cid_uid(data)
    itemArray = []
    for item in items:
        itemDict = {}
        itemDict['iid'] = item.iid
        itemDict['iname'] = item.iname
        itemArray.append(itemDict)
    return jsonify ({'items': itemArray})