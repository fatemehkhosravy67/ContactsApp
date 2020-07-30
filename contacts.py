# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 00:39:07 2020

@author: fatemeh
"""


#from ContactsApp.sqcontacts import conn
import json
from bottle import route, run, debug, template, redirect, request, static_file, error,default_app
import sqlite3, os
# from bottle import Bottle



@route('/contacts', method=["GET"])
def contact_list():
    if  os.path.exists ('contacts.db'):
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute("SELECT * FROM contacts ORDER BY firstname")
        result = c.fetchall()
        print('all data fetched from db')
        print(result)
        conn.commit()
        c.close()
    else:
        print('No path to database found.') 
    # output = template('make_table', rows=result)
    print('template rendered successfully')
    final_res = [{'id':item[0],'firstname': item[1], 'lastname': item[2],
                  'cellnumber': item[3]} for item in result]

    return json.dumps(final_res)

# @route('/item<item:re:[0-9]+>')
# def show_item(item):
#     conn = sqlite3.connect('contacts.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM contacts WHERE id LIKE ?", (item,))
#     result = c.fetchall()
#     c.close()

#     if not result:
#         return 'This item number does not exist!'
#     else:
#         return 'Task: %s' % result[0]

@route('/add', method=["GET"])
def new_item():
    #  if request.GET.get('add','').strip():
          # return 'ok'
        ID = request.GET.get('ID', '').strip()
        firstname = request.GET.get('firstname', '').strip()
        lastname = request.GET.get('lastname', '').strip()
        cellnumber = request.GET.get('cellnumber', '').strip()
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute("INSERT INTO contacts (id,firstname,lastname,cellnumber) VALUES  (?,?,?,?)", (ID,firstname,lastname,cellnumber))
        # new_id = c.lastrowid
        conn.commit()
        c.close()
        return redirect('/contacts')
      # else:
      #      # return template('add_item.tpl')
      #       # return redirect('/contacts')
      #    return 'NOt ok'



# @route('/edit/:no', method='GET')
# def edit_item(no):
#       if request.GET.get('save','').strip():
#           firstname = request.GET.get('firstname', '').strip()
#           lastname = request.GET.get('lastname', '').strip()
#           cellnumber = request.GET.get('cellnumber', '').strip()
#           conn = sqlite3.connect('contacts.db')
#           c = conn.cursor()
#           c.execute("UPDATE contacts SET firstname = ?, lastname = ?,cellnumber=?  \
#                       WHERE id = ?", (firstname,lastname,cellnumber, no))
#           conn.commit()
#           return redirect('/contacts')
#       else:
#           conn = sqlite3.connect('contacts.db')
#           c = conn.cursor()
#           c.execute("SELECT * FROM contacts WHERE id LIKE ?", \
#                       (str(no)))
#           cur_data = c.fetchone()
#           return template('edit_item.tpl', old=cur_data, no=no)
        
@route('/edit', method=["GET"])
def edit_item():
      # if request.GET.get('save','').strip():
          firstname = request.GET.get('firstname', '').strip()
          lastname = request.GET.get('lastname', '').strip()
          cellnumber = request.GET.get('cellnumber', '').strip()
          conn = sqlite3.connect('contacts.db')
          c = conn.cursor()
          c.execute("UPDATE contacts SET firstname = ?, lastname = ?,cellnumber=?  \
                      WHERE id = 43", (firstname,lastname,cellnumber))
          conn.commit()
          return redirect('/contacts')
      # else:
      #     conn = sqlite3.connect('contacts.db')
      #     c = conn.cursor()
      #     c.execute("SELECT * FROM contacts WHERE id LIKE ?", \
      #                 (str(no)))
      #     cur_data = c.fetchone()
      #     return template('edit_item.tpl', old=cur_data, no=no)

# @route('/delete/:no', method=["GET"])
# def delete_item(no):
#       # if request.GET.get('delete','').strip():   
#            conn = sqlite3.connect('contacts.db')
#            c = conn.cursor()         
#            c.execute("DELETE FROM contacts WHERE id =?",(no))
#            conn.commit()
#            return redirect('/contacts')
#       # else:
#       #     return template('delete_item.tpl', no=no)
    

@route('/delete', method=["GET"])
def delete_item():
      # if request.GET.get('delete','').strip():   
           conn = sqlite3.connect('contacts.db')
           c = conn.cursor()         
           c.execute("DELETE FROM contacts WHERE id =985")
           conn.commit()
           return redirect('/contacts')
      # else:
      #     return template('delete_item.tpl', no=no)
    
    
     

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
