from feature_req import db
from feature_req.models import Request



def adjustPriority(form,id):
	priority= form.clientPriority.data
	record =  queryPriorityMatchingReq(form.client.data, form.clientPriority.data,id)
	while record:
		print(record.title)
		record.client_priority += 1
		db.session.commit() 
		record =queryPriorityMatchingReq(form.client.data, record.client_priority,record.id)
	

def queryPriorityMatchingReq(client, priority, reqId):
	return Request.query.filter(Request.client_id == client)\
	.filter(Request.client_priority == priority)\
	.filter(Request.id != reqId).first()

def addRequest(form):
	request=Request(title= form.title.data, 
            description=form.description.data,
            product_area_id =form.productArea.data,
            client_id= form.client.data,
            target_date =form.targetDate.data,
            client_priority= form.clientPriority.data
            )
        db.session.add(request)
        db.session.commit()
        adjustPriority(form, request.id)
