

#from flask_wtf import Form
from flask_wtf import FlaskForm as Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, Required
from wtforms import StringField, IntegerField, SelectField
from .models import possible_types, possible_departments, possible_tableinfos
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class UploadForm(Form):
    targettableinfo = QuerySelectField('Select Target Table', query_factory = possible_tableinfos, blank_text = 'Select One')
    upload = FileField('Select Excel File', validators=[FileRequired(), FileAllowed(['xlsx','xlsm','xltx','xltm'], 'Excel workbooks only!')])

class NewDepartmentForm(Form):
    departmentname = StringField('departmentname', validators=[DataRequired(), Length(max=50)])

class NewTableInfoForm(Form):
    descriptive_name = StringField('descriptive_name', validators=[DataRequired(), Length(max=50)])
    table_name = StringField('table_name', validators=[DataRequired(), Length(max=50)])

class NewFieldForm(Form):
    fieldname = StringField('Field Name', validators=[DataRequired(), Length(max=30)])
    fieldtype = QuerySelectField('Field Type', query_factory = possible_types)

class BulkFieldsForm(Form):
    upload = FileField('Select File', validators=[FileRequired(), FileAllowed(['xlsx','xlsm','xltx','xltm'], 'Excel workbooks only!')])
