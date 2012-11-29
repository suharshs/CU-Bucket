
$(document).ready(function(){
    var position=0;
    var suggestionsNum=2;
    $("#searchInput").keydown(function(e){
        //on down arrow click
        if(e.keyCode == 40){
            if(position!==suggestionsNum){
                if(position!==0){
                 $("[id*=suggestion_"+position+"]").css('background-color', 'white');
                }
                position=position+1;
              $("[id*=suggestion_"+position+"]").css('background-color', '#eee9e9');
              
           
            }
            return true;
        }
        //on up arrow click
        if(e.keyCode == 38){
            if(position!==0){
                if(position!==suggestionsNum+1){
                 $("[id*=suggestion_"+position+"]").css('background-color', 'white');
                }
                position=position-1;
              $("[id*=suggestion_"+position+"]").css('background-color', '#eee9e9');
              
           
            }
            return true;
        }

        if(e.keyCode == 13){
            // user has highlighted a choice
            if(position!==0){
                alert($("[id*=suggestion_"+position+"_link]").text());
            }
        }
    });

    $("#searchInput").keyup(function(e){
        if(e.keyCode== 38 || e.keyCode == 40 || e.keyCode == 13){
            return;
        }
        if(!$(this).val()){
            $('.suggestions').css('display', 'none');
            return;
        }
        $.ajax({
            type: 'POST',
            url:  '/search',
            data: {
                user_string: $("#searchInput").val(),
                _xsrf: getCookie("_xsrf")
            },
            success: function(response){
                console.log(response);
            }
        });
    });
});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function renderSuggestion(suggestion){
    $('#suggestion_1_link').text(suggestion);
    $('.suggestions').css('display', 'block');

}
