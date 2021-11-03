$(document).ready(function () {
 
    $(".likbtn_new").click(function (e) {
        e.preventDefault();
        var likdata;
        var  thisdata= this;
        if($(this).hasClass("1"))
        {
            $(this).attr("class","0");
            $(this).css("color", "black");
            likdata="off";
        }
        else
        if($(this).hasClass("0"))
        {
            $(this).attr("class", "1");
            $(this).css("color","white");
            likdata = "on";

        }
     

        var checkauth = $("#auth").val()

        if (checkauth == "True") {
        
            $.ajax({
                type: "POST",
                url: "data_get",
                data: {
                    likedis: likdata,
                    idval: $(thisdata).val(),
                    source: $("#src_id").val(),

                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

                },
                dataType: "json",
                success: function (response) {
                  
                    const dta= response.data
                    $(thisdata).children().eq(1).text(dta)
                   
                   
                 

                },
            });
        }
        else {
            location.href = "accounts/login/"
        }

    })
});
