from flaskr import app
from flask import redirect, render_template,request, url_for
import sqlite3
import random
DATABASE = 'database.db'


#ホーム
@app.route('/home')
def home():
    return render_template(
        'home.html'
    )

#未完ルーム入室
@app.route('/enter_the_room',methods=['POST'])
def enter_the_room():
    return redirect(url_for('index'))

#未完ルーム作成
@app.route('/room_create',methods=['POST'])
def room_create():
    room_name = request.form['room_name']
    room_id = random.randint(0,999999)

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO room VALUES(?,?)',
                [room_id,room_name])
    con.commit()
    con.close()
    return redirect(url_for('room',room_id=room_id,room_name=room_name))

#未完ルーム
@app.route('/room/<room_name>/<room_id>')
def room(room_id,room_name):
    return render_template('room.html',room_id=room_id,room_name=room_name)


#投稿
@app.route('/create_tweet',methods=['POST'])
def create_tweet():
    return render_template('room.html')