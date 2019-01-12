let viewModel = {
	requests: ko.observableArray(),
	currentClient:ko.observable(undefined),
	getRequests: ()=> {
	 $.ajax({
			url: "request/getAll",
			type: 'GET',
			success: (data)=>{
				console.log(data);
				ko.utils.arrayPushAll(viewModel.requests, data);
				viewModel.requests.valueHasMutated();
			}
    	})	
	},
	deleteReq: (req)=> {
		console.log('delete',req)
		$.ajax({
			url: `/request/delete/${req.id}`,
			type: 'DELETE',
			success: (data)=>{
			viewModel.requests.remove(req);
			}
		})
	},
	editReq: (req)=> {
		window.location.href = "/request/edit/"+req.id;
	},
	getClientRequests: (client_id)=> {
		$.ajax({
			url: `/request/get/${client_id}`,
			type: 'GET',
			success: (data)=>{
				viewModel.requests([]);
				ko.utils.arrayPushAll(viewModel.requests, data);
				viewModel.currentClient(data[0].client);
				viewModel.requests.valueHasMutated();
			}
    	})
	},
	changeToClientRoute: (req)=>{
		window.location.href = "/request/clientRequests/"+req.client_id;
	}
}

ko.applyBindings(viewModel);
let path = window.location.pathname;
if(path == "/" || path == "/requests"){
	viewModel.getRequests()
}
if(path.includes("/request/clientRequests")){
	id = path.slice(path.lastIndexOf("/")+1,path.length)
	viewModel.getClientRequests(id)	
}
