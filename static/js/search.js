
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
        /*
        if(!$(this).val()){
            $('.suggestions').css('display', 'none');
            return;
        }*/
        $.ajax({
            type: 'POST',
            url:  '/search',
            data: {
                user_string: $("#searchInput").val(),
                _xsrf: getCookie("_xsrf")
            },
            success: function(response){
                console.log(response);
                changeActivites(response);
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

function changeActivites(response){
    var replaceString = '';
    var activities = response.matches;
    for (var i = 0; i < activities.length; i++) {
        replaceString += '<div class="activity" id= ' + activities[i]["ID"] + '><div class="activity-name">' + activities[i]['name'] +
        '</div><div class="description">' + activities[i]['description'] + '</div><div class="location">' + activities[i]['location'] +
        '</div><div class="creator">by ' + activities[i]['creator'] + '</div>';
        if (response['username'] === activities[i]['creator'])
            replaceString += '<img src="../static/img/close.png" class="delete-button" id="delete-button">';
        if (!activities[i]['interestUserName']){
            replaceString += '<img src="../static/img/bucketIcon3.png" class="add-to-my-bucket" id="add-to-my-bucket">';
        }
        if (activities[i]['interestUserName']){
            replaceString += '<img src="../static/img/bucketIcon2.png" class="remove-from-my-bucket" id="remove-from-my-bucket">';
        }
        if (!activities[i]['completedUserName']){
            replaceString += '<img src="../static/img/complete.png" class="complete-activity" id="complete-activity">';
        }
        replaceString += '</div><div class="hr"></div>';
    }
    $("#activity-board").html(replaceString);
}
