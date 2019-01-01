from flask import render_template, redirect,url_for, jsonify, request
from feature_req import app, db
from feature_req.forms import RequestForm
from feature_req.models import Request
from feature_req.utils import addRequest,deleteRequest, editRequest, passValuesToForm


@app.route("/")
@app.route("/requests")
def requests():
    return render_template('requests.html')


@app.route("/getRequests", methods=['GET'])
def getRequests():
    return jsonify([i.serialize for i in Request.query.all()])

#create a new feature request
@app.route('/addRequest', methods=['GET','POST'])
def add():
    form = RequestForm()
    if form.validate_on_submit():
        addRequest(form)
        return redirect(url_for('requests'))
    return render_template('requestForm.html', title='add new', form=form)

#delete or edit a request
@app.route("/req/<id>", methods=['DELETE', 'GET','POST'])
def req(id):
    if request.method == 'DELETE':
        return deleteRequest(id)

    if request.method == 'GET':
        form = RequestForm()
        passValuesToForm(form,id)
        return render_template('requestForm.html', title = 'edit', form = form)

    if request.method == 'POST':
        form = RequestForm()
        if form.validate_on_submit():
            editRequest(form,id)
        return redirect(url_for('requests'))   
        