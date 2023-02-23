from project.accounts import accounts
from project.accounts import db
from flask import render_template, session, redirect, url_for

@accounts.route('/show')
def show():
    if 'id' not in session:
        return redirect(url_for('auth.login'))
    
    collection = db['accounts']
    print(session['id'])
    accs = collection.find({'ownerId': session['id']})
    acc_list = []
    for acc in accs:
        print(acc)
        acc_dict = {
            'name': acc['name'],
            'type': acc['type'],
            'is_negative_allowed': acc['negative'],
            'amount': acc['amount'],
        }
        acc_list.append(acc_dict)

    return render_template('accounts.html', accs = acc_list)