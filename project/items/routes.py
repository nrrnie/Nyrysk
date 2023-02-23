from project.items import items
from project.items import db
from flask import render_template, redirect, url_for, session


@items.route ('/show')
def show (limit=20):
    collection = db['items']
    items = collection.find().skip(skip=150).limit(limit)
    item_list = []
    for item in items:
        item_dict = {
            "id": item["_id"],
            "barcode": item["barcode"],
            "name": item["name"],
            "weight": item["weight"],
            "buying_price": item["buyingPrice"],
            "selling_price": item["sellingPrice"],
            "amount": item["amount"],
        }
        if item['weight'] == 'true':
            item_dict["weight"] = 'kg'
        else:
            item_dict["weight"] = 'units'
        if 'brandId' in item:
            item_dict["brandId"] = item["brandId"]
        if 'brandName' in item:
            item_dict["brandName"] = item["brandName"]
        if 'categoryName' in item:
            item_dict["categoryName"]= item["categoryName"]
        if 'categoryId' in item:
            item_dict["categoryId"]= item["categoryId"]
        #print(item_dict)
        item_list.append(item_dict)

    return render_template('items.html',  items=item_list)


@items.route('/delete/<barcode>')
def delete(barcode):
    if session['id'] is None:
        return redirect(url_for('auth.login'))
    collection = db['items']
    deletion = collection.delete_one({'barcode': barcode})
    return 

@items.route('/purchases')
def purchases():
    if session['id'] is None:
        return redirect(url_for('auth.login'))
    p_list = []

    return render_template('purchases.html', list=p_list)