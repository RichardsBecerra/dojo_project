from flask import Flask
from flask_charts import GoogleCharts

app = Flask(__name__)
charts = GoogleCharts(app)
app.secret_key = 'fullstackjpython'