import json
import sqlite3
from server import app
from flask import url_for, session, render_template, redirect, flash, request
from server import db_handler
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html', userCount=len(get_users()), postCount=len(get_posts()))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if logged_in():
        return redirect(url_for('users'))  # posts get shown
    if request.method == "POST":
        conn = db_handler.create_connection()
        cur = conn.cursor()

        password = request.form['password']
        username = request.form['username']
        cur.execute(
            'SELECT password FROM User WHERE username=?', (username,))

        pw_hash = cur.fetchone()
        if not pw_hash:
            flash('username or password is incorrect, please try again', 'danger')
            return redirect(url_for('login'))
        else:
            pw_hash = pw_hash[0]
        if bcrypt.check_password_hash(pw_hash, password):
            session['logged_in'] = True
            session['username'] = username
            # loggs in and members get shown
            return redirect(url_for('users'))
        else:
            flash('username or password is incorrect, please try again', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/users')  # /posts?usrname=reza should show Reza's posts
def users():
    if logged_in():
        if request.args.get('username'):
            user = get_user(request.args.get('username'))
            return render_template('users.html', user=user)

        return render_template('users.html', users=get_users())
    return redirect(url_for('login'))


@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if logged_in():
        if request.method == 'POST':
            username = session['username']
            conn = db_handler.create_connection()
            cur = conn.cursor()
            cur.execute('SELECT id FROM User WHERE username=?', (username,))
            user_id = cur.fetchone()[0]
            title = request.form['title']
            content = request.form['content']
            cur.execute(
                'INSERT INTO Post(title, content, author_id) VALUES(?,?,?)', (title, content, user_id))
            conn.commit()
            conn.close()
            return redirect(url_for('users', username=session['username']))

        return render_template('new_post.html')

    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if logged_in():
        return redirect(url_for('users'))  # posts get shown
    if request.method == "POST":
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password'])

        if is_username_available(username):
            add_user(username, password)
            flash('You are successfully signed up, please login', 'success')
            return redirect(url_for('login'))
        else:
            flash(
                'The username is already used, try with another username please', 'danger')
            return redirect(url_for('signup'))

    return render_template('signup.html')


@app.route('/logout')
def logout():
    session['logged_in'] = False
    session['username'] = ''
    return render_template('login.html')


def logged_in():
    return 'logged_in' in session and session['logged_in'] == True


def add_user(username, password):
    try:
        conn = db_handler.create_connection()
        cur = conn.cursor()

        cur.execute(
            'INSERT INTO User(username, password) VALUES (?,?)', (username, password))

        conn.commit()
        conn.close()
        dbUsers = get_users()  # update the users variable

    except sqlite3.Error as e:
        print(e)


def get_user(username):
    conn = db_handler.create_connection()
    cur = conn.cursor()
    cur.execute('SELECT id FROM User WHERE username=?', (username,))
    user_id = cur.fetchone()[0]
    cur.execute('SELECT * FROM Post WHERE author_id=?', (user_id,))
    posts = cur.fetchall()
    user_with_posts = {
        'username': username,
        'posts': posts
    }
    return user_with_posts


def get_users():
    try:
        conn = db_handler.create_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM User')
        return cur.fetchall()
    except sqlite3.Error as e:
        print(e)


def get_posts():
    try:
        conn = db_handler.create_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM Post')
        return cur.fetchall()
    except sqlite3.Error as e:
        print(e)


def is_username_available(username):
    try:
        conn = db_handler.create_connection()
        cur = conn.cursor()

        cur.execute('SELECT id FROM User WHERE username=?', (username,))
        user_id = cur.fetchone()
        # if user_id:
        #     return False
        # else:
        #     return True
        return not user_id
    except sqlite3.Error as e:
        print(e)
