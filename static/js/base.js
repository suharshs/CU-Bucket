$(document).ready(function(){
    $("#new-activity #submit").click(function(){
        //validate if form is filled out
        console.log($("#new-activity").serialize());
        $.ajax({
            type: 'POST',
            url:  '/activity/new',
            data: $("#new-activity").serialize(),
            success: function(data){
                console.log("success = ", data["success"]);
            }
        });
    });
});