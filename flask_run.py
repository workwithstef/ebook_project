from flask import Flask, render_template



from py_db import MSDBconnection



app = Flask(__name__)





nwind = MSDBconnection()

results = nwind.sql_query("SELECT * FROM google_books_1299")

list=[results.fetchone()]





@app.route('/')

def hello_world():

    return  render_template("homepage.html",list=list)



@app.route('/index')

def index():

    return render_template("index.html")



@app.route('/page2')

def page2():

    return render_template("page2.html")



if( __name__ == '__main__'):

    app.run(host='0.0.0.0')