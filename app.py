from flask import Flask, render_template, jsonify
from connection import findEmployee, getKPIValues, getLEAvg

app = Flask(__name__)


@app.route('/')  # http://127.0.0.1:5000/col
def displayStores():
    return (jsonify(findEmployee()))


@app.route('/items')  # http://127.0.0.1:5000//items
def displayItems():
    return ("charan")


@app.route('/kpilist')  # http://127.0.0.1:5000/kpilist
def getkpilist():
    return ({"kpilist": getKPIValues()})


@app.route('/le')
def getleavg():
    return {"leavg":getLEAvg()}

app.run(port=5000)
