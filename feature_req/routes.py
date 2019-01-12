from flask import render_template, redirect,url_for, jsonify, request, Blueprint
from feature_req import db
from feature_req.forms import RequestForm
from feature_req.models import Request,Client, ProductArea
from feature_req.utils import addRequest,deleteRequest, editRequest, passValuesToForm

featRequests = Blueprint('featRequests', __name__, static_folder= './feature_req/static')



@featRequests.route("/")
@featRequests.route("/requests")
@featRequests.route("/request/clientRequests/<clientId>")
def requests(clientId=None):
    return render_template('requests.html')


@featRequests.route("/request/getAll", methods=['GET'])
def getRequests():
    return jsonify([r.serialize for r in Request.query.all()])

#create a new feature request
@featRequests.route('/request/add', methods=['GET','POST'])
def add():
    form = RequestForm()
    if form.validate_on_submit():
        addRequest(form)
        return redirect (url_for('featRequests.requests'))
    return render_template('requestForm.html', title='add new', form=form)

#delete a request
@featRequests.route("/request/delete/<id>", methods=['DELETE'])
def delete(id):
    if request.method == 'DELETE':
        if deleteRequest(id) =='success':
            return 'no_content',204
        return deleteRequest(id)

# edit a request
@featRequests.route("/request/edit/<id>", methods=['GET','POST'])
def edit(id):
    if request.method == 'GET':
        form = RequestForm()
        passValuesToForm(form,id)
        return render_template('requestForm.html', title = 'edit', form = form)

    if request.method == 'POST':
        form = RequestForm()
        if form.validate_on_submit():
            editRequest(form,id)
        return redirect(url_for('featRequests.requests')) 

# get client requests
@featRequests.route("/request/get/<clientId>", methods = ['GET'])
def getClientRequest(clientId):
      return jsonify([c.serialize for c in Client.query.filter_by(id = clientId).first().requests]);
        