from flask import Flask  
from flask import render_template
from flask import request
from database import get_all_cats

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
        n = request.form['name']
        create_cat(n)
        print('reived post request')
        return render_template("home.html")
@app.route('/', methods=['GET', 'POST'])
def add_vote():

    if(request.method == 'GET'):
        return render_template("home.html")
    else:                             
        vote_count  = vote_count + 1
        return render_template("home.html")

if __name__ == '__main__':
    app.run(debug = True)

