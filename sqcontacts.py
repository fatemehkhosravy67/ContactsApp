# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:03:11 2020

@author: fatemeh
"""


import sqlite3
conn = sqlite3.connect("contacts.db")
conn.execute("CREATE TABLE contacts(personID INT PRIMARY key Identity, firstname nvarchar(50)), lastname nvarchar(50), cellnumber nvarchar(50)")
conn.execute("INSERT INTO contacts (firstname,lastname,cellnumber) VALUES ('fateme','khosravy','091111111')")
conn.commit()
