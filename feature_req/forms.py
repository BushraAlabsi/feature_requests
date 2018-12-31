from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,IntegerField,SubmitField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    client = SelectField('Client',
    	choices=[('1', 'client A'), ('2', 'client B'), ('3', 'client C')], 
    	validators=[DataRequired()])
    clientPriority = IntegerField('Client Priority', validators=[DataRequired()])
    productArea = SelectField('Product Area',
    	choices=[('1', 'Policies'), ('2', 'Billing'), ('3', 'Claims'),('4','Reports')]
    	,validators=[DataRequired()])
    description = StringField('Description')
    targetDate = DateField('Target Date',format='%Y-%m-%d',validators=[DataRequired()])
    submit = SubmitField('Submit')
