from misgastos_app import app
from misgastos_app.controllers.users import login_required
from flask import render_template, redirect, request, session, flash, jsonify
from misgastos_app.models.categoria import Categoria
from misgastos_app.models.form import ioForm
from misgastos_app.models.item import Item
from misgastos_app.models.movimiento import Movimiento
from misgastos_app.models.tipopago import Tipopago

@app.route ('/iorecords')
@app.route ('/iorecords/<mid>')
@login_required
def iorecords(mid=None):
    ioform = ioForm()
    ioform.mov_uid.data = session['uid']
    if request.path == '/iorecords':
        cio = {'cio': 0}
        session['cio'] = cio
        idata = {'iio': 0, 'cid': 1, 'uid': session['uid']}
        session['idata'] = idata
    elif request.path == f'/iorecords/{mid}':
        data = {'mid': mid, 'uid': session['uid']}
        mov = Movimiento.get_by_mid_uid(data)
        if mov:
            ioform.mid.data = mov.mid
            ioform.mio.data = mov.mio
            cio = {'cio': mov.mio}
            session['cio'] = cio
            ioform.mov_cid.data = mov.mov_cid
            idata = {'iio': mov.mio, 'cid': mov.mov_cid, 'uid': session['uid']}
            session['idata'] = idata
            ioform.mov_iid.data = mov.mov_iid
            ioform.mdate.data = mov.mdate
            ioform.mamount.data = mov.mamount
            ioform.mov_tpid.data = mov.mov_tpid
            ioform.mcomment.data = mov.mcomment
        else:
            flash('Registro no existe')
            return redirect ('/detalle')
    ioform.mov_cid.choices = [(categoria.cid, categoria.cname) for categoria in Categoria.get_all_by_cio(cio)]
    ioform.mov_iid.choices = [(item.iid, item.iname) for item in Item.get_all_by_iio_cid_uid(idata)]
    ioform.mov_tpid.choices = [(tipopago.tpid, tipopago.tpname) for tipopago in Tipopago.get_all()]
    return render_template('iorecords.html', ioform = ioform)

@app.route ('/iorecords/save', methods=['POST'])
@app.route ('/iorecords/save/<mid>', methods=['POST'])
@login_required
def iorecrods_save(mid=None):
    ioform = ioForm()
    ioform.mov_uid.data = session['uid']
    ioform.mov_cid.choices = [(categoria.cid, categoria.cname) for categoria in Categoria.get_all_by_cio(session['cio'])]
    ioform.mov_iid.choices = [(item.iid, item.iname) for item in Item.get_all_by_iio_cid_uid(session['idata'])]
    ioform.mov_tpid.choices = [(tipopago.tpid, tipopago.tpname) for tipopago in Tipopago.get_all()]
    if ioform.validate():
        if request.path == '/iorecords/save':
            Movimiento.save(ioform.data)
            if ioform.mio.data == 0:
                flash ('Gasto registrado')
            else:
                flash ('Ingreso registrado')
            return redirect ('/iorecords')
        elif request.path == f'/iorecords/save/{mid}':
            ioform.mid.data = mid
            Movimiento.update(ioform.data)
            if ioform.mio.data == 0:
                flash ('Gasto actualizado')
            else:
                flash ('Ingreso actualizado')
            return redirect ('/detalle')
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
    idata = {'iio':iio, 'cid': cid, 'uid': session['uid']}
    session['idata'] = idata
    items = Item.get_all_by_iio_cid_uid(idata)
    itemArray = []
    for item in items:
        itemDict = {}
        itemDict['iid'] = item.iid
        itemDict['iname'] = item.iname
        itemArray.append(itemDict)
    return jsonify ({'items': itemArray})