from misgastos_app import app
from flask_charts import Chart
from flask import render_template, redirect, request, session, flash
from misgastos_app.controllers.users import login_required
from misgastos_app.models.movimiento import Movimiento
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

@app.route ('/panel')
@login_required
def panel():
    uid = {'uid': session['uid']}
    totals = Movimiento.get_total_by_cat(uid)
    cat_chart = Chart("PieChart", "cat_chart", options= {'is3D':True, 'legend':'labeled', 'backgroundColor':'whitesmoke', 'fontName':'verdana'})
    cat_chart.data.add_column("string", "Categoría")
    cat_chart.data.add_column("number", "Gasto")
    if not totals:
        cat_chart.data.add_row(["Sin registro de gastos", 1])
    else:
        for cat in totals:
            cat_chart.data.add_row([f"{cat.cname}", int(cat.subtotal)])
    return render_template ('panel.html', totals = totals, cat_chart = cat_chart)

@app.route ('/detalle')
@login_required
def detalle():
    data = {'uid': session['uid'], 'mio':0}
    gastos = Movimiento.get_by_uid_this_month(data)
    data['mio'] = 1
    ingresos = Movimiento.get_by_uid_this_month(data)
    total = {'gastos': 0, 'ingresos': 0, 'saldo': 0}
    for gasto in gastos:
        total['gastos'] +=  gasto.mamount
    for ingreso in ingresos:
        total['ingresos'] += ingreso.mamount
    total['saldo'] = total['ingresos'] - total['gastos']
    return render_template ('detalle.html', gastos = gastos, ingresos = ingresos, total = total)

@app.route ('/mov_delete/<mid>')
@login_required
def mov_delete(mid):
    data = {'mid': mid, 'uid': session['uid']}
    Movimiento.delete(data)
    flash ('Registro eliminado')
    return redirect ('/detalle')

@app.route ('/mov_edit/<mid>')
@login_required
def mov_edit(mid):
    data = {'mid': mid, 'uid': session['uid']}
    Movimiento