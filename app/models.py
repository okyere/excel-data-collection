# -*- coding: utf-8 -*-

from app import db, theapp
from sqlalchemy.schema import Sequence, CreateSequence
#from sqlalchemy.sql import text
from sqlalchemy import asc

# def _create_sequence(name):
#     # if db is Oracle create the sequence
#     if db.engine.name.upper() == 'ORACLE':
#         query = "SELECT * FROM user_sequences WHERE sequence_name = '{}'".format(name.upper())
#         result = db.session.execute(query)
#
#         if not result.scalar():
#             db.session.execute('CREATE SEQUENCE {}'.format(name.upper()))
#             db.session.commit()
#
# def _drop_sequence(name):
#     # if db is Oracle create the sequence
#     if db.engine.name.upper() == 'ORACLE':
#         sql = 'DROP SEQUENCE {}'.format(name.upper())
#         db.session.execute(sql)
#         db.session.commit()
#

class FieldType(db.Model): # one to field
    __tablename__ = 'dut_field_types'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    python_type = db.Column(db.String(120))
    python_import = db.Column(db.String(120))
    fields = db.relationship("Field", backref = "type", lazy = 'dynamic')

    #_create_sequence('DUT_FIELD_TYPES_SEQ')

    def __str__(self):
        return self.name

def possible_types():
    return FieldType.query.order_by("id")

class Field(db.Model): # many to field type
    __tablename__ = 'dut_fields'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)

    fieldtype_id = db.Column(db.Integer, db.ForeignKey("dut_field_types.id"))
    tableinfo_id = db.Column(db.Integer, db.ForeignKey('dut_tables_info.id'))

    # _create_sequence('DUT_FIELDS_SEQ')

    def __str__(self):
        return self.name

class TableInfo(db.Model):
    __tablename__ = 'dut_tables_info'

    id = db.Column(db.Integer, primary_key = True)
    descriptive_name = db.Column(db.String(120), unique = True, nullable=False) # name for user to identify table
    table_name = db.Column(db.String(30), unique = True, nullable=False) # database table name
    fields = db.relationship('Field', backref='table_info', lazy='dynamic')
    department_id = db.Column(db.Integer, db.ForeignKey('dut_departments.id'))
    table_status = db.Column(db.String(1))

    # _create_sequence('DUT_TABLES_INFO_SEQ')

    def __str__(self):
        return self.descriptive_name

def possible_tableinfos():
    return TableInfo.query.filter(TableInfo.table_status == "1").order_by(asc("descriptive_name"))

class Department(db.Model):
    __tablename__ = 'dut_departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    # one-to-many relationship (a Department can have several associated TableInfos)
    tables_info = db.relationship('TableInfo', backref = 'department', lazy='joined')

    # _create_sequence('DUT_DEPARTMENTS_SEQ')

    def __str__(self):
        return self.name

class UploadsLog(db.Model):
    __tablename__ = 'dut_uploadslog'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), nullable=False)
    user_cwsid = db.Column(db.String(120), nullable=False)
    file_name = db.Column(db.String(120), nullable=False)
    destination_table = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)

    # _create_sequence('DUT_UPLOADSLOG_SEQ')

def possible_departments():
    return Department.query
