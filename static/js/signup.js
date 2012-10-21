$(document).ready(function() {
	$('#signup-button').click(function(){
		if(!$(this).hasClass('disabled')){
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
		}
	});
	//checks if the password match and applies apropriate styling
	$('#password_check').keyup(function(){
		//if password does not match password_check
		if(!password_checker()){
			$('#password_check').popover('show');
			$('#signup-button').addClass('disabled');

		}else{
			$('#password_check').popover('hide');
			$('#signup-button').removeClass('disabled');	
		}
	});	
	//password_checker function that compares the strings 
	var password_checker =function() {
		var password=$('#password').val(),
			password_again=$('#password_check').val();
			if(password.length !=0 && password === password_again){
				return true;
			} else return false;
	}

});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


