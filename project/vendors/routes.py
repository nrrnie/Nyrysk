from project.vendors import vendors
from project.vendors import db
from flask import render_template

@vendors.route('/show')
def show(limit=20):
    vendors = db.vendors.find().limit(limit=limit)
    vendor_list = []
    for v in vendors:
        v_dict = {
            'id': v['_id'],
            'name': v['name'],
            'type': v['type'],
            'contacts': v['contacts'],
        }
        vendor_list.append(v_dict)

    return render_template('vendors.html', list=vendor_list)