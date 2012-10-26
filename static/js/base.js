$(document).ready(function(){
    $("#new-activity #submit").click(function(){
        //validate if form is filled out
        var name = $('#name').val(),
            description = $('#description').val(),
            category = $('#category').val(),
            location = $('#location').val();
        //just for now, will need to make this validation better later
        if (name === '' || description === '' || category === '' || location === ''){
            alert("Need to fill in all of the fields");
        }
        $.ajax({
            type: 'POST',
            url:  '/activity/new',
            data: {
                name: name,
                description: description,
                category: category,
                location: location,
                _xsrf: getCookie("_xsrf")
            },
            datatype: 'json',
            success: function(data){
                $('#activity-modal').modal('hide');
                $('#activity-board').prepend(postMaker(name, description, location));
            }
        });
    });
});

function postMaker(name, description, location){
    var postString =
        ['<div class="activity">',
        '<div class="description">' + description + '</div>',
        '<div class="location">' + location + '</div>',
        '<div class="name">by' + name + '</div>',
        '<a href="/activity/add/""><img src="../static/img/bucketIcon2.png" class="add-to-my-bucket" id="add-to-my-bucket"></a>',
        '</div>',
        '<div class="hr"></div>'].join('\n');
    return postString;
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}