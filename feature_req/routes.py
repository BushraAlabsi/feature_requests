from flask import render_template, redirect,url_for
from feature_req import app, db
from feature_req.forms import RequestForm
from feature_req.models import Request


@app.route("/")
@app.route("/requests")
def requests():
    return render_template('requests.html')
    

@app.route("/getRequests", methods=['GET'])
def getRequests():
    return Request.query.all()

#create a new feature request
@app.route('/addRequest', methods=['GET','POST'])
def add():
    form = RequestForm()
    if form.validate_on_submit():
        request=Request(title= form.title.data, 
            description=form.description.data,
            product_area_id =form.productArea.data,
            client_id= form.client.data,
            target_date =form.targetDate.data,
            client_priority= form.clientPriority.data
            )
        db.session.add(request)
        db.session.commit()
        return redirect(url_for('requests'))
    return render_template('requestForm.html', title='add new', form=form)