from misgastos_app import app
from flask import render_template, redirect, request, session, flash
from misgastos_app.controllers.users import login_required
from misgastos_app.models.form import ItemForm
from misgastos_app.models.item import Item

@app.route ('/items_edit/<iio>/<cid>/<cname>')
@app.route ('/item_edit/<iid>/<iname>')
@login_required
def items_edit(iid=None, iname = None, iio=None, cid=None, cname=None):
    itemform = ItemForm()
    if iid:
        iedit = {'iid': iid, 'iname': iname}
        itemform.iid.data = iid
        itemform.iname.data = iname
        return render_template ('item_edit.html', iedit = iedit, itemform = itemform)
    else:
        idata = {'iio': iio, 'cid': cid, 'cname': cname, 'uid': session['uid']}
        items = Item.get_all_by_iio_cid_uid(idata)
        return render_template ('items_edit.html', items = items, itemform = itemform, idata = idata)

@app.route ('/items_delete/<iio>/<cid>')
@app.route ('/items_delete/<iid>')
@login_required
def items_delete(iid=None, iio=None, cid=None):
    if iid:
        idata = {'iid': iid, 'uid': session['uid']}
    else:
        idata = {'iio': iio, 'cid': cid, 'uid': session['uid']}
    Item.delete(idata)
    flash('Items eliminados')
    return redirect('/categorias')

@app.route ('/items_save', methods=['POST'])
@login_required
def items_save ():
    itemform = ItemForm()
    itemform.itm_uid.data = session['uid']
    if itemform.validate():
        Item.save(itemform.data)
        flash(f'Nuevo item {itemform.iname.data} ingresado')
    return redirect (f'/items_edit/{itemform.iio.data}/{itemform.itm_cid.data}/{itemform.itm_cname.data}')

@app.route ('/item_update', methods=['POST'])
@login_required
def item_update ():
    itemform = ItemForm()
    itemform.itm_uid.data = session['uid']
    if itemform.validate():
        Item.update(itemform.data)
        flash ('Item actualizado')
    return redirect ('categorias')