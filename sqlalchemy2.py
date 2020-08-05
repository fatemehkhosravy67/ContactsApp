from sqlalchemy import create_engine

db_uri = "sqlite:///db.sqlite"
engine = create_engine(db_uri)

# DBAPI - PEP249
# create table
engine.execute('CREATE TABLE "contacts" ('
               'id INTEGER NOT NULL,'
               'firstname VARCHAR, '
               'lastname VARCHAR, '
               'cellnumber VARCHAR, '
               'PRIMARY KEY (id));')
# insert a raw
engine.execute('INSERT INTO "contacts" '
               '(id, firstname, lastname, cellnumber) '
               'VALUES (1 , "fatemeh" ,"khosravy" ,"0911525853")')

# select *
result = engine.execute('SELECT * FROM '
                        '"contacts"')
for _r in result:
   print(_r)

# delete *
engine.execute('DELETE from "contacts" where id=1;')
result = engine.execute('SELECT * FROM "contacts"')
print(result.fetchall())