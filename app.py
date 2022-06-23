from flask import Flask, render_template
from flask import Response

app = Flask(__name__)

@app.route("/")
def index():
    item1 = f'<a href="/properties">Properties</a>'
    item2 = f'<a href="/tenants">Tenants</a>'
    item3 = f'<a href="/malipo">Payments</a>'

    return item1 + item2 + item3

@app.route("/properties")
def indexx():
    item1 = f'<div style="color:green">We have 120 properties</div>'
    item2 = f'<a href="/">go back</a>'
    return item1 + item2

@app.route("/tenants")
def indexxx():
    item1 = f'<div style="color:black">We have 120 tenants</div>'
    item2 = f'<a href="/">go back</a>'
    # return item1 + item2
    return Response(render_template("iman.html"))

@app.route("/malipo")
def indexxxx():
    item1 = f'<div style="color:red">No one has paid 😠 </div>'
    item2 = f'<a href="/">go back</a>'
    return item1 + item2