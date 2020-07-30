# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:03:11 2020

@author: fatemeh
"""

import sqlite3
from random import randint

conn = sqlite3.connect("contacts.db")
table_query = '''CREATE TABLE IF NOT EXISTS contacts (
	id INT PRIMARY KEY,
   	firstname nvarchar(50) ,
	lastname nvarchar(50),
	cellnumber nvarchar(50)
) ;'''
insert_query = '''INSERT INTO contacts (id,firstname,lastname,cellnumber)
                VALUES ({},'fateme','khosravy','091111111');'''.format(randint(1, 10000))
conn.execute(table_query)
print('table generated successfully')
conn.execute(insert_query)
print('insert in table runned successfully')
conn.commit()
