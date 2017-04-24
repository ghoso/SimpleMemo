#coding: utf-8

from flask import Flask,render_template,request,redirect,url_for,g
import sqlite3

DATABASE = 'db/memo.db'
app= Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    
    con = connect_db()
    con.row_factory = sqlite3.Row
    g.db = con

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# Routing
@app.route('/')
def index():
    con = g.db.cursor()
    cur = con.execute("select * from memos")
    rows = cur.fetchall()
    return render_template('index.html',rows = rows)

@app.route('/new',methods=['POST'])
def create_memo():
    if request.method == 'POST':
        memo = request.form['memo']
        print("memo=%s"%memo)
        return render_template('index.html')
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=3000)
