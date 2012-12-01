$(document).ready(function() {
	$('#login-button').click(function(){
		var username_text = $('#username').val(),
			password_text = $('#password').val();
		if (username_text === '' || password_text === ''){
			return;
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
					window.location.replace("/home");
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

function replaceAbout(){
    var aboutString = '<div class="navbar navbar navbar-fixed-top"> \
            <div class="navbar-inner"> \
                <div class="container"> \
                    <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse"> \
                        <span class="icon-bar"></span> \
                        <span class="icon-bar"></span> \
                        <span class="icon-bar"></span> \
                    </a> \
                    <a class="brand" href="/">cucket</a> \
                    <div class="nav-collapse collapse"> \
                        <ul class="nav"> \
                            <li><a href="#">About</a></li> \
                        </ul> \
                    </div><!--/.nav-collapse --> \
                 </div> \
            </div> \
        </div><div id="about-body" class="container overlap-fix about" style="top: 100px;"> \
        <h1>About Cucket</h1> \
        <p>A lot of students go through school only experiencing academics and missing all the great things there are to do on campus. CU-Bucket is a "bucket list" where one can add, discover, and complete activites before graduation. When you have completed 100 activities you are ready to graduate!</p> \
        <h1>What should you do?</h1> \
        <p>On this site, you can create new activities, perform searches on activites, and create and complete activities on the go with our mobile app. So stop sitting there and cucket! Begin by clicking cucket on the top!</p> \
        <h1>Meet the Team!</h1> \
        <ul> \
            <li>Greg Blazczuk</li> \
            <li>Irteza Farhat</li> \
            <li>Suharsh Sivakumar</li> \
            <li>Martin Wozniewicz</li> \
        </ul> \
    </div>';

    $("#body").html(aboutString);
}