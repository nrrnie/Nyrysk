from flask import render_template, request, session, flash, redirect, url_for
from project.users import users
from project.users import db

@users.route('/profile')
def profile():
    if session['name'] is None:
        redirect(url_for('login'))
    user = db['users'].find_one({'_id': session['id']})
    if request.method == 'GET':
        return render_template('profile.html', user=user)
    
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')


    user = db['users'].find_one({'_id': session['id']})

    if user['name'] != name or user['email'] != email or user['phone_number'] != phone:
        user['name'] = name
        user['email'] = email
        user['phone'] = phone

        values = {
            "$set": {
            'name': name,
            'email':email,
            'phone':phone,
            }
        }

        db['users'].update_one({'_id': session['id']}, {})

    collection = db['users']
    user = collection.find({'_id': session['id']}, values)
    return render_template('profile.html', user=user)