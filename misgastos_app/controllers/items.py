from misgastos_app import app
from flask import render_template, redirect, request, session, flash
from misgastos_app.controllers.users import login_required
from misgastos_app.models.item import Item

@app.route ('/items_edit/<iio>/<cid>')
@login_required
def items_edit(iio, cid):
    idata = {'iio': iio, 'cid': cid, 'uid': session['uid']}
    items = Item.get_all_by_iio_cid_uid(idata)
    return render_template ('items_edit.html', items = items)

@app.route ('/items_delete/<iio>/<cid>')
@login_required
def items_delete(iio, cid):
    idata = {'iio': iio, 'cid': cid, 'uid': session['uid']}
    Item.delete(idata)
    flash('Items eliminados')
    return redirect('/categorias')