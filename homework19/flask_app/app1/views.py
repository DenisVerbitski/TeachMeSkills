from flask import Blueprint, render_template, request, abort
import requests
from .validation import Validator, Validation  # добавление задания 13.3

app1 = Blueprint('app1', __name__)

url = 'https://api.kanye.rest'


@app1.route('/quote')
def quote():
    global url
    quote_number = request.args.get('number', 1)  
    some_list = []  
    if quote_number is None:  
        src = requests.get(url)
        for value in src.json().values():
            some_list.append(value)
        return render_template("index.html", some_list=some_list)
    elif int(
            quote_number) > 0:  
        try:
            quote_number = int(quote_number)
        except ValueError:
            abort(404)
        else:
            west = [requests.get(url).json()['quote'] for x in
                    range(quote_number)]
        return render_template("index.html", some_list=west)


@app1.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':  
        src = dict(request.form)  
        try:
            username, password, email = request.form['username'], request.form['password'], request.form['email']
        except KeyError as e:
            return f"Поле {e} не было передано"
        validator_1 = Validator(username, password, email)  
        try:
            if validator_1.validation():  
                abort(405)
        except Validation:  
            abort(406) 
    return render_template('register.html')


@app1.errorhandler(405)
def valid_accept(error):
    return render_template('error405.html')


@app1.errorhandler(406)
def valid_error(error):
    return f"Valid_error"