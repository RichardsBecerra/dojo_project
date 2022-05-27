from flask_charts import Chart, ChartData
from misgastos_app import app
from flask import render_template, redirect, request, session, flash, url_for, jsonify
from random import randint

@app.route('/charts')
def charts():
    my_chart = Chart("PieChart", "my_chart", options= {"title": "Fixed values"})
    my_chart.data.add_column("string", "Person")
    my_chart.data.add_column("number", "Count")
    my_chart.data.add_row(["Gabriel", 6])
    my_chart.data.add_row(["Benjamin", 21])
    my_chart.data.add_row(["Rodrigo", 44])
    my_chart.data.add_row(["Marcela", 45])
    random_chart = Chart("PieChart", "random_chart", options= {"title": "Random values"}, data_url=url_for("data"), refresh=3000)
    return render_template('charts.html', my_chart = my_chart, random_chart = random_chart)

@app.route("/data", methods=["POST"])
def data():
    data = ChartData()
    data.add_column("string", "Person")
    data.add_column("number", "Count")
    data.add_row(["Gabriel", randint(1, 100)])
    data.add_row(["Benjamin", randint(1, 100)])
    data.add_row(["Rodrigo", randint(1, 100)])
    data.add_row(["Marcela", randint(1, 100)])
    return jsonify(data.data())