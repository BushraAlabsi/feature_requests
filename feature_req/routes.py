from flask import render_template, redirect,url_for, jsonify, request, Blueprint
from feature_req import db
from feature_req.forms import RequestForm
from feature_req.models import Request,Client
from feature_req.utils import addRequest,deleteRequest, editRequest, passValuesToForm

featRequests = Blueprint('featRequests', __name__, static_folder= './feature_req/static')



@featRequests.route("/")
@featRequests.route("/requests")
def requests():
    return render_template('requests.html')


@featRequests.route("/getRequests", methods=['GET'])
def getRequests():
    return jsonify([i.serialize for i in Request.query.all()])

#create a new feature request
@featRequests.route('/addRequest', methods=['GET','POST'])
def add():
    clients = [i.serialize for i in Client.query.all()]
    form = RequestForm()
    if form.validate_on_submit():
        print(form.title)
        addRequest(form)
        return redirect (url_for('featRequests.requests'))
    form.client.choices = clients
    return render_template('requestForm.html', title='add new', form=form)

#delete or edit a request
@featRequests.route("/req/<id>", methods=['DELETE', 'GET','POST'])
def req(id):
    if request.method == 'DELETE':
        if deleteRequest(id) =='success':
            return 'no_content',204
        return deleteRequest(id)

    if request.method == 'GET':
        form = RequestForm()
        passValuesToForm(form,id)
        return render_template('requestForm.html', title = 'edit', form = form)

    if request.method == 'POST':
        form = RequestForm()
        if form.validate_on_submit():
            editRequest(form,id)
        return redirect(url_for('featRequests.requests'))   
        