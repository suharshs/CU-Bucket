$(document).ready(function() {
	$('#login_button').click(function(){
		var username_text = $('#username').val(),
			password_text = $('#password').val(),
			cur_url = document.URL;
		$.ajax({
			type: 'POST',
			url:  cur_url + 'login',
			data: {
				username: username_text,
				password: password_text,
				_xsrf: getCookie("_xsrf")
			},
			dataType: 'json',
			success: function(data){
				if (data['passed'] === 'true'){
					window.location.replace(cur_url + "user/" + username_text);
				} else if (data['passed'] === 'false'){
					clear();
					alert('Password Wrong');
				}
			}
		});
	});
});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function clear(){
	$('password').val('');
}