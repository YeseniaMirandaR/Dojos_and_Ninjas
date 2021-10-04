from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos') #main page

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all() # from model dojo.py 
    return render_template("index.html",all_dojos = Dojo.get_all()) 

@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos') # no render template, redirect because it's a post

@app.route('/dojo/<int:id>')
def showDojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.dojos_ninjas_join(data))