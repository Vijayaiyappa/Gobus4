$(document).ready( function(){

$(".add1,.add2").click(function(e) {
    e.preventDefault();

  if($(this).hasClass("color1"))
  {
  
  $(this).removeClass("color1");
  
  }
  else
  {
 if($(this).val()=="like")
 {
 $(this).addClass("color1");
  $(this).next().removeClass("color1")
 }
 else
 if($(this).val()=="dislike")
 {
    $(this).addClass("color1");
    $(this).prev().removeClass("color1");
 }
  }
var checkauth=$("#auth").val()

 if(checkauth=="True")
 {
   alert("iam rock")
$.ajax({
    type: "POST",
    url:"data_get",
    data: {
        likedis:$(this).val(),
        idval:$(this).attr("id"),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    
    },
   dataType: "dataType",
    success: function (response) {
        alert("worked")
    }
});
}
else
{
  location.href="accounts/login/"
}

})
});
