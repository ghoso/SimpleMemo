#coding: utf-8

from flask import Flask,render_template,request,redirect,url_for,g
import sqlite3

DATABASE = 'db/memo.db'
app= Flask(__name__)
app.config.from_object(__name__)

# DB接続
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# メインページ表示
def get_list():
    con = g.db.cursor()
    cur = con.execute("SELECT * FROM memos")
    rows = cur.fetchall()
    return rows

# リクエスト前に行われる処理
@app.before_request
def before_request():
    con = connect_db()
    con.row_factory = sqlite3.Row
    g.db = con

# リクエスト終了時に行われる処理
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
#
# Routing
#

# indexページ表示
@app.route('/')
def index():
    rows = get_list()
    return render_template('index.html',rows = rows)

# データ登録処理
@app.route('/new',methods=['POST'])
def create_memo():
    if request.method == 'POST':
        try:
            memo = request.form['memo']
            print("memo=%s"%memo)
            cur = g.db.cursor()
            cur.execute("INSERT INTO memos (title,text) VALUES (?,?)",('Test Memo',memo))
            g.db.commit()
        except:
            cur.rollback()
    rows = get_list()
    return render_template('index.html',rows = rows)

# データ更新処理
@app.route('/edit',methods=['POST'])
def edit_memo():
    if request.method == 'POST':
        try:
            memo = request.form['memo']
            memo_id = request.form['id']
            cur = g.db.cursor()
            cur.execute("UPDATE memos SET text=? where id=?",(memo,memo_id))
            g.db.commit()
        except:
            cur.rollback()
    rows = get_list()
    return render_template('index.html',rows = rows)

# データ削除処理
@app.route('/delete',methods=['POST'])
def delete_memo():
    rows = get_list()
    return render_template('index.html',rows = rows)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=3000)
