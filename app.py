#coding: utf-8

from flask import Flask,render_template,request,redirect,url_for,g
import sqlite3

app= Flask(__name__)

# Routing
@app.route('/')
def index():
    return render_template('index.html')

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
