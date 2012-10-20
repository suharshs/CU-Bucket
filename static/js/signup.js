$(document).ready(function() {
	$('#signup-button').click(function(){
		var username_text = $('#username').val(),
			password_text = $('#password').val(),
			cur_url = window.location.host;
		$.ajax({
			type: 'POST',
			url:  '/signup',
			data: {
				username: username_text,
				password: password_text,
				_xsrf: getCookie("_xsrf")
			},
			dataType: 'json',
			success: function(data){
				if (data['passed'] === 'true'){
					window.location.replace("/user/" + username_text);
				} else if (data['passed'] === 'false'){
					alert('Username is already taken');
				}
			}
		});
	});
});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}