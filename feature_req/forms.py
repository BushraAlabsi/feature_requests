from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, EqualTo

class RequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    client = SelectField('Client',choices=[], coerce=int,validators=[DataRequired()])
    clientPriority = IntegerField('Client Priority', validators=[DataRequired()])
    productArea = SelectField('Product Area',
    	choices=[('1', 'Policies'), ('2', 'Billing'), ('3', 'Claims'),('4','Reports')]
    	,validators=[DataRequired()])
    description = StringField('Description')
    targetDate = DateField('DatePicker',format='%Y-%m-%d',validators=[DataRequired()])
    submit = SubmitField('Submit')
