from feature_req import app,db



app.app_context().push()
with app.app_context():
    db.create_all(None)