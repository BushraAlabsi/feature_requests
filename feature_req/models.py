from datetime import datetime
from feature_req import db


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(120), default='')
    product_area_id = db.Column(db.Integer, db.ForeignKey('product_area.id'), nullable=False)
    target_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    client_priority = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)



    def __repr__(self):
        return 'title: %s  priority %s  client_id %s' % (self.title, self.client_priority, self.client_id)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    #define a one-to-many relation between client and request tables
    requests = db.relationship('Request', backref='client', lazy=True)


    def __repr__(self):
        return '%s' % self.name




class ProductArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    #define a one-to-many relation between product_area and request tables
    requests = db.relationship('Request', backref='area', lazy=True)


    def __repr__(self):
        return '%s' % self.name