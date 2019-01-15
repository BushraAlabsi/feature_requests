from datetime import datetime
from feature_req import db

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d")]

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(2000), default='')
    product_area_id = db.Column(db.Integer, db.ForeignKey('product_area.id'), nullable=False)
    target_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    client_priority = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)



    def __repr__(self):
        return 'title: %s  priority %s  client_id %s' % (self.title, self.client_priority, self.client_id)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'target_date': dump_datetime(self.target_date),
           'priority'   :self.client_priority,
           'title'      :self.title,
           'description':self.description,
           'product_area':self.area.name,
           'client_id'  :self.client_id,
           # This is an example how to deal with One2Many relations
           'client'  : self.client.name
       }

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    #define a one-to-many relation between client and request tables
    requests = db.relationship('Request', backref='client', lazy=True)


    def __repr__(self):
        return '%s' % self.name
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'name'       :self.name,
           'requests'   :self.requests
        }



class ProductArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    #define a one-to-many relation between product_area and request tables
    requests = db.relationship('Request', backref='area', lazy=True)


    def __repr__(self):
        return '%s' % self.name