from flask import render_template, redirect,url_for, jsonify, request, Blueprint
from feature_req import db
from feature_req.forms import RequestForm
from feature_req.models import Request,Client, ProductArea
from feature_req.utils import addRequest,deleteRequest, editRequest, passValuesToForm

featRequests = Blueprint('featRequests', __name__, static_folder= './feature_req/static')



@featRequests.route("/")
@featRequests.route("/requests")
def requests():
    return render_template('requests.html')


@featRequests.route("/request/getAll", methods=['GET'])
def getRequests():
    return jsonify([i.serialize for i in Request.query.all()])

#create a new feature request
@featRequests.route('/request/add', methods=['GET','POST'])
def add():
    clients = [(c.id, c.name) for c in Client.query.all()]
    productAreas = [(pa.id, pa.name) for pa in ProductArea.query.all()]

    print(clients)
    form = RequestForm()
    if form.validate_on_submit():
        print(form.title)
        addRequest(form)
        return redirect (url_for('featRequests.requests'))
    form.client.choices = clients
    form.productArea.choices = productAreas
    return render_template('requestForm.html', title='add new', form=form)

#delete or edit a request
@featRequests.route("/request/delete/<id>", methods=['DELETE'])
def delete(id):
    if request.method == 'DELETE':
        if deleteRequest(id) =='success':
            return 'no_content',204
        return deleteRequest(id)


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
        