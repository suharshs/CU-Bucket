$(document).ready(function() {
	$('#login-button').click(function(){
		var username_text = $('#username').val(),
			password_text = $('#password').val();
		if (username_text === '' || password_text === ''){
			alert('Must input username and password');
		}

		$.ajax({
			type: 'POST',
			url:  '/login',
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
					clear();
					alert('Password Wrong');
				}
			}
		});
	});

	$('#new-user-button').click(function(){
		window.location.replace('/signup');
	});
});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function clear(){
	$('password').val('');
}
