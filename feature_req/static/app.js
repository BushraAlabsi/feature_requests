let viewModel = {
	requests: ko.observableArray(),
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
				console.log(data)
			// var array1 = viewModel.array();
			viewModel.requests.remove(req);
			}
		})
	},
	editReq: (req)=> {
		console.log('edittttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt',req)
		window.location.href = "/request/edit/"+req.id;
	}
}

ko.applyBindings(viewModel);
viewModel.getRequests()