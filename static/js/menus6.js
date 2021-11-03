
$(document).ready(function() {
 
	var menu = $(".menu")
    $(".check").click(function() {
		var mopt=menu.eq($(".check").index(this));
        $(mopt).slideToggle(200);
		event.stopPropagation();
		
    });


$(document).click(function()
	{
		     $(".menu").slideUp(200);
			 event.stopPropagation();
			
			 
	}); 


$(".menu label").each(function (){
$(this).click(function(e)
 {    
      var mopt=$(this).closest(".menu")
    var tht=this

	
	  $.ajax({
		  type: "POST",
		  url: "incorrect_data",
		
		  data: {
			  ids:$(tht).parent().children().eq(3).val(),
			  //mid_r:$(this).parent().children().eq(5).val(),
			  comp: $(tht).text(),
			  source:$("#src_id").val(),	
			 // dest:$("#dest_id").val(),
			  csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
		  },
		  dataType: "dataType",
		  
		  
		  
		
	  });
	  $(mopt).slideToggle(200);
	  event.stopPropagation();
	
	

	  
	
 });
}); 

});