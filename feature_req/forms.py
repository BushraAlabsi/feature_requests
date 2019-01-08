from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField
from feature_req.models import Client, ProductArea


def get_clients():
	return Client.query

def get_areas():
	return ProductArea.query

class RequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    client = QuerySelectField(query_factory=get_clients,
                            get_pk=lambda c: c.id,
                            get_label=lambda c: c.name)
    clientPriority = IntegerField('Client Priority', validators=[DataRequired()])
    productArea = QuerySelectField(query_factory=get_areas,
                            get_pk=lambda pa: pa.id,
                            get_label=lambda pa: pa.name)

    description = StringField('Description')
    targetDate = DateField('DatePicker',format='%Y-%m-%d',validators=[DataRequired()])
    submit = SubmitField('Submit')
