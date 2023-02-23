from project.auth import auth
from project.auth import db
from flask import request, render_template, flash, redirect, url_for, session, get_flashed_messages
from passlib.hash import sha256_crypt



@auth.route('/login', methods=['GET', 'POST'])
def login ():
    if request.method == 'GET':
        return render_template('log.html')
    
    phone_number = request.form.get('phone')
    password = request.form.get('password')


    user = db['users'].find_one({"phone_number": phone_number})
    if user is None or sha256_crypt.verify(password, user['password']) is False:
        flash('Username or password is wrong', 'error')
        return render_template('log.html')
    
    session['name'] = user['name']
    session['id'] = user['_id']
    return redirect(url_for('items.show'))

@auth.route('/logout')
def logout():
    session['name'] = None
    session['id'] = None
    return redirect(url_for('index'))

@auth.route('/register', methods=['GET', 'POST'])
def register ():
    if request.method == 'GET':
        return render_template('register.html')
    
    phone_number = request.form.get('phone')
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    verify_pass = request.form.get('verify')

    print(phone_number)

    find_user = db['users'].find_one({'phone_number': phone_number})
    print(find_user)

    if password != verify_pass:
        flash('Passwords do not match')
    if find_user is not None:
        flash('Phone number is already taken')
    if db['users'].find_one({'email': email}) is not None:
        flash('Email is already taken')


    if len(get_flashed_messages()) != 0:
        return render_template('register.html')
    
    user = db['users'].insert_one({
    'name': name,
    'email': email,
    'phone_number': phone_number,
    'password': sha256_crypt.hash(password),
    'outlet': None,
    'position': None,
    })                     

    

    return render_template('register.html')