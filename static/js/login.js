$(document).ready(function() {
	$('#login_button').click(function(){
		var username_text=$('#username').text(),
			password_text=$('#password').text();
		$.ajax({
			type: 'POST',
			url:  '/login',
			data: {username: username_text, password: password_text},
			dataType: 'json',
			success: function(data){
				alert('success');
			}
		});
	});
});