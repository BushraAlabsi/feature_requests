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
