from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja # from dojo and ninja .py files

@app.route('/ninjas')
def ninjas():
    return render_template('/ninja.html',dojos= dojo.Dojo.get_all()) #from models dojo.py file

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/') # no render template, redirect because it's a post