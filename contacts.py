# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 00:39:07 2020

@author: fatemeh
"""


import json
from random import randint

from bottle import route, run, redirect, request
from sql_injection import conn
# from bottle import Bottle



@route('/contacts', method="GET")
def contact_list():
    c = conn.cursor()
    c.execute("SELECT * FROM contacts ORDER BY firstname")
    result = c.fetchall()
    print('all data fetched from db')
    c.close()
    final_res = [{'id':item[0],'firstname': item[1], 'lastname': item[2],
                  'cellnumber': item[3]} for item in result]

    return json.dumps(final_res)


@route('/new', method='POST')
def new_item():
      if request.json:
            data = request.json
            c = conn.cursor()
            insert_query = '''INSERT INTO contacts (id,firstname,lastname,cellnumber) VALUES  ({},'{}','{}','{}');
            '''.format(randint(0,999999999),data.get('firstname'),data.get('lastname'),data.get('cellnumber'))
            c.execute(insert_query)
            conn.commit()
            c.close()
      else:
          return "Not valiud data"

      return json.dumps(data)

        
@route('/edit/<no>', method='PUT')
def edit_item(no):
            data = request.json
            c = conn.cursor()
            c.execute('''UPDATE contacts SET firstname = '{}', lastname = '{}' ,cellnumber = '{}' WHERE id={};'''.format(
                data.get('firstname'), data.get('lastname'), data.get('cellnumber'), no))
            conn.commit()
            c.close()
            return json.dumps(data)



@route('/delete/<no>', method=["GET"])
def delete_item(no):
            c = conn.cursor()
            c.execute('''DELETE FROM contacts WHERE id ={};'''.format(no))
            result = c.fetchall()
            conn.commit()
            return result


@route('/contacts/<id>', method=["GET"])
def get_item(id):
           c = conn.cursor()
           c.execute('''Select id,firstname,lastname,cellnumber FROM contacts WHERE id ={};'''.format(id))
           result = c.fetchall()[0]
           final_res = {"id":result[0],"firstname":result[1],"lastname":result[2],"cellnumber":result[3]}
           conn.commit()
           return final_res

    
    
     

# app = Bottle()
# @app.route('/contacts')
# def show_contacts():
#     db = sqlite3.connect('contacts.db')
#     c = db.cursor()
#     c.execute("SELECT * FROM contacts")
#     data = c.fetchall()
#     c.close()
#     output = template('bring_to_contacts', rows=data)
#     return output

run(host='localhost', port=8080, debug=True)
