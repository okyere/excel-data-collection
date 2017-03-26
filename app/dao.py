# -*- coding: utf-8 -*-


from app.models import *
from app import theapp, db


# Common CRUD operations
def commit():
    db.session.commit()

def add(instance):
    db.session.add(instance)
    db.session.commit()

def delete(instance):  # for internal use only
    db.session.delete(instance)
    db.session.commit()

def delete_field(field,tableinfo):
    db.session.delete(field)
    db.engine.execute("ALTER TABLE {} DROP COLUMN {}".format(tableinfo.table_name.lower(), field.name.lower()))
    db.session.commit()

def stripinputstring(inputstring):
    return " ".join(inputstring.split())

def delete_tableinfo(tableinfo):
    table_name = tableinfo.table_name.lower()
    Field.query.filter_by(tableinfo_id = tableinfo.id).delete() # delete field entries for this tableinfo object
    db.session.execute('DROP TABLE {}'.format(table_name))
    db.session.commit()
    delete(tableinfo) # delete the entry

def add_field(tableinfo, name, fieldtype):
    new_field = Field(name = name, tableinfo_id = tableinfo.id, fieldtype_id = fieldtype.id)
    db.session.add(new_field)

    if fieldtype.name == "Text":
        typestring = "text"
    elif fieldtype.name == "Number":
        typestring = "numeric(15,5)"
    elif fieldtype.name == "Date":
        typestring = "date"

    db.engine.execute("ALTER TABLE {} ADD {} {}".format(tableinfo.table_name.lower(), name.lower(), typestring))
    db.session.commit()

def isnumber(s):
 try:
  float(s)
  return True
 except(ValueError, TypeError):
  return False
