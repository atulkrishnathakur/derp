
function getStateByAjax(thisobj){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
	var get_state_ajax_url = $("#get_state_ajax_url").val();
	var country_id = thisobj.value;
     $.ajaxSetup({
            headers: {
                "X-CSRFToken": csrftoken,
            }
     });  	
	 $.ajax({
	   type : 'POST',
	   url : get_state_ajax_url,
	   data : {country_id:country_id},
	   success : function(res){
		console.log(res);
	         //var catcode = res.catcode;
			
			//$("#catcode").val(catcode);
	    },
	 });
}
