from feature_req import db
from feature_req.models import Request, ProductArea,Client
from datetime import datetime

def adjustPriority(form,id):
	priority= form.clientPriority.data
	record =  queryPriorityMatchingReq(Client.query.filter(Client.name == str(form.client.data)).first().id, form.clientPriority.data,id)
	while record:
		print(record.title)
		record.client_priority += 1
		db.session.commit() 
		record =queryPriorityMatchingReq(Client.query.filter(Client.name == str(form.client.data)).first().id, record.client_priority,record.id)
	

def queryPriorityMatchingReq(client, priority, reqId):
	return Request.query.filter(Request.client_id == client)\
	.filter(Request.client_priority == priority)\
	.filter(Request.id != reqId).first()

def addRequest(form):
	print(form.productArea)
	request=Request(title= form.title.data, 
            description=form.description.data,
            product_area_id =ProductArea.query.filter(ProductArea.name == str(form.productArea.data)).first().id,
            client_id=Client.query.filter(Client.name == str(form.client.data)).first().id,
            target_date =datetime.strptime(form.targetDate.data.strftime('%Y-%m-%d'),'%Y-%m-%d'),
            client_priority= form.clientPriority.data
            )
        db.session.add(request)
        db.session.commit()
        adjustPriority(form, request.id)

def deleteRequest(id):
	print(id)
	req = Request.query.filter_by(id=id).first()
        db.session.delete(req)
        try: 
            db.session.commit()
            return "success"
        except Exception as inst:
            return inst 


def editRequest(form,id):
	req = Request.query.filter(Request.id == id).first()
	req.title = form.title.data
	req.description= form.description.data
	req.product_area_id =ProductArea.query.filter(ProductArea.name == str(form.productArea.data)).first().id
	req.client_priority =form.clientPriority.data 
	req.client_id=Client.query.filter(Client.name == str(form.client.data)).first().id
	req.target_date =datetime.strptime(form.targetDate.data.strftime('%Y-%m-%d'),'%Y-%m-%d')
	db.session.commit()
	adjustPriority(form, req.id)

#pass the values for edit to the form
def passValuesToForm(form,id):
	req = Request.query.filter_by(id=id).first()
	form.title.data = req.title
	form.description.data = req.description
	form.productArea.data = req.area.name
	form.clientPriority.data = req.client_priority
	form.client.data = req.client.name
	form.targetDate.data = req.target_date