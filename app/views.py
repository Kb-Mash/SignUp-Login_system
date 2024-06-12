from flask import render_template, redirect, request, url_for, session
from app import app, db, bcrypt
from app.models import User

# home page
@app.route('/')
def home():
    return render_template('home.html')

# user sign up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            hashed_password = bcrypt.generate_hash(password).decode('utf-8')
            user = User(username=username, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            # TO-DO: message
            return redirect(url_for('signup'))
    return render_template('signup.html')

# user login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = reuest.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            # TO-DO: message
            return redirect(url_for('login'))
    return render_template('login.html')

# logout user
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))
