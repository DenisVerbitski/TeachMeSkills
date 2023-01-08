
from flask import Blueprint, render_template
from datetime import datetime
import requests

app1 = Blueprint('app1', __name__)


@app1.route('/times')
def times():
    current_times = datetime.now().date()
    return f"<h3> {str(current_times)} </h3>"


@app1.route('/quote')
def quote():
    src = requests.get('https://api.kanye.rest')
    return f"<h3> {src.text[1:-1]} </h3>"