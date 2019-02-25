from flask import Flask,redirect 
from flask import render_template
from flask import request
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cat', methods=['GET', 'POST'])
def cat():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        return render_template('cat.html')

@app.route('/details', methods=['GET', 'POST'])
def add_cat():
    if(request.method == 'GET'):
        return render_template("details.html")
    else:                                                          
        name = request.form['name']
        create_cat(name,0)
        return redirect("/")
@app.route('/add_vote', methods=['GET', 'POST'])
def add_vote():

    if(request.method == 'GET'):
        return render_template("/home")
    else:
        cat_id = request.form['cat_id']                             
        add_like(cat_id)
        return redirect("/")

if __name__ == '__main__':
    app.run(debug = True)

