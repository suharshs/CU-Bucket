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
                $('#activity-board').prepend(postMaker(data['results'][0]['ID'],name, description, location, data['results'][0]['creator']));
            }
        });
    });
});

function postMaker(id, name, description, location, creator){
    var postString =
        ['<div class="activity" id=' + id + '>',
            '<div class="activity-name">' + name + '</div>',
            '<div class="description">' + description + '</div>',
            '<div class="location">' + location + '</div>',
            '<div class="creator">by' + creator + '</div>',
            '<img src="../static/img/close.png" class="delete-button" id="delete-button">',
            '<img src="../static/img/bucketIcon2.png" class="add-to-my-bucket" id="add-to-my-bucket">',
        '</div>',
        '<div class="hr"></div>'].join('\n');
    return postString;
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}