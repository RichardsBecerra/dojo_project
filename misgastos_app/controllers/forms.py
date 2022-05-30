from misgastos_app import app
from misgastos_app.controllers.users import login_required
from flask import render_template, redirect, request, session, flash, jsonify
from misgastos_app.models.categoria import Categoria
from misgastos_app.models.form import ioForm
from misgastos_app.models.item import Item
from misgastos_app.models.tipopago import Tipopago

@app.route ('/iorecords')
@login_required
def iorecords():
    ioform = ioForm()
    uid = {'uid': session['uid']}
    ioform.mov_cid.choices = [(categoria.cid, categoria.cname) for categoria in Categoria.get_all()]
    ioform.mov_iid.choices = [(item.iid, item.iname) for item in Item.get_all_by_uid(uid)]
    ioform.mov_tpid.choices = [(tipopago.tpid, tipopago.tpname) for tipopago in Tipopago.get_all()]
    return render_template('iorecords.html', ioform = ioform)

@app.route ('/item/<cid>')
@login_required
def item(cid):
    data = {'cid': cid, 'uid': session['uid']}
    items = Item.get_by_cid_uid(data)
    itemArray = []
    for item in items:
        itemDict = {}
        itemDict['iid'] = item.iid
        itemDict['iname'] = item.iname
        itemArray.append(itemDict)
    return jsonify ({'items': itemArray})