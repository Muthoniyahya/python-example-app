from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    color = f'<div style="color:blue">HEY</div>'
    return color