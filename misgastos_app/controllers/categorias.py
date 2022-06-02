from misgastos_app import app
from flask import render_template, redirect, request, session, flash
from misgastos_app.controllers.users import login_required
from misgastos_app.models.categoria import Categoria
from misgastos_app.models.item import Item

@app.route ('/categorias')
@login_required
def categorias():

    cio = {'cio': 0}
    cats_gastos = Categoria.get_all_by_cio(cio)
    items_gastos = []
    for cat in cats_gastos:
        idata = {'iio': 0, 'cid': cat.cid, 'uid': session['uid']}
        items_gastos.append(Item.get_all_by_iio_cid_uid(idata))

    cio = {'cio': 1}
    cats_ingresos = Categoria.get_all_by_cio(cio)
    items_ingresos = []
    for cat in cats_ingresos:
        idata = {'iio': 1, 'cid': cat.cid, 'uid': session['uid']}
        items_ingresos.append(Item.get_all_by_iio_cid_uid(idata))

    return render_template ('categorias.html', cats_gastos=cats_gastos, cats_ingresos=cats_ingresos, items_gastos=items_gastos, items_ingresos=items_ingresos)