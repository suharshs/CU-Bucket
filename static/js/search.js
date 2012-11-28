
$(document).ready(function(){
    $("#search").keyup(function(){
        $.ajax({
            type: 'POST',
            url:  '/search',
            data: {
                user_string: $("#search").val(),
                _xsrf: getCookie("_xsrf")
            },
            success: function(response){
                console.log(response.closest_word);
            }
        });
    });
});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
