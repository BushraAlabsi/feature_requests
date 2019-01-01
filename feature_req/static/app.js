let viewModel = {
	requests: ko.observableArray(),
	getRequests: ()=> {
	 $.ajax({
			url: "/getRequests",
			type: 'GET',
			success: (data)=>{
				console.log(data);
				ko.utils.arrayPushAll(viewModel.requests, data);
				viewModel.requests.valueHasMutated();
			}
    	})	
	}
}

ko.applyBindings(viewModel);
viewModel.getRequests()