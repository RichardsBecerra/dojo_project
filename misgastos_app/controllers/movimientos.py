from misgastos_app import app
from flask import render_template, redirect, request, session, flash
from misgastos_app.controllers.users import login_required
from misgastos_app.models.movimiento import Movimiento

@app.route ('/panel')
@login_required
def panel():
    uid = {'uid': session['uid']}
    totals = Movimiento.get_total_by_cat(uid)
    return render_template ('panel.html', totals = totals)

@app.route ('/detalle')
@login_required
def detalle():
    data = {'uid': session['uid'], 'mio':0}
    gastos = Movimiento.get_by_uid_this_month(data)
    data['mio'] = 1
    ingresos = Movimiento.get_by_uid_this_month(data)
    return render_template ('detalle.html', gastos = gastos, ingresos = ingresos)