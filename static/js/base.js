$(document).ready(function(){
    $("#new-activity #submit").click(function(){
        //validate if form is filled out
        var formdata = $('#new-activity').serialize();
        $.ajax({
            type: 'POST',
            url:  '/activity/new',
            data: formdata,
            datatype: 'json',
            success: function(data){
                $('#activity-modal').modal('hide');

                var form = $('#new-activity');
                var vals = getFormValues(form);
                $('#activity-board').prepend(
                    postMaker(data['results'][0]['ID'],
                    vals.name,
                    vals.description,
                    vals.location,
                    data['results'][0]['creator']));
                $('#new-activity')[0].reset();  // Reset all the fields of the form
                if (location.pathname.indexOf("user") !== -1){
                    location.reload();
                }
            }
        });
    });


    // create the function for the button rating
    $(".add-to-my-bucket").live("click", function(){
        var toChange = $(this);
        console.log("click the add to my bucket button");
        $.ajax({
            type: 'GET',
            url:  '/activity/add/' + toChange.parent().attr('id'),
            success: function(){
                toChange.parent().append('<img src="../static/img/bucketIcon2.png" class="remove-from-my-bucket" id="remove-from-my-bucket">');
                toChange.remove();
                if (location.pathname.indexOf("user") !== -1){
                    location.reload();
                }
            }
        });
        $(this).tooltip('destroy');
    }).tooltip({title: "Add to your bucket!"});

    $(".remove-from-my-bucket").live("click", function(){
        var toChange = $(this);
        console.log("click the remove to my bucket button");
        $.ajax({
            type: 'GET',
            url:  '/activity/remove/' + toChange.parent().attr('id'),
            success: function(){
                toChange.parent().append('<img src="../static/img/bucketIcon3.png" class="add-to-my-bucket" id="add-to-my-bucket">');
                toChange.remove();
                if (location.pathname.indexOf("user") !== -1){
                    location.reload();
                }
            }
        });
        $(this).tooltip('destroy');
    }).tooltip({title: "Remove from your bucket"});

    $(".complete-activity").live("click", function(){
        if (confirm("Confirm that you completed this activity. You break the honor code if you are lying.")){
            var toChange = $(this);
            console.log("click the add to my bucket button");
            $.ajax({
                type: 'GET',
                url:  '/activity/complete/' + toChange.parent().attr('id'),
                success: function(){
                    toChange.remove();
                    if (location.pathname.indexOf("user") !== -1){
                        location.reload();
                    }
                }
            });
        }
        $(this).tooltip('destroy');
    }).tooltip({title: "Finish this activity"});



    $(".delete-button").live("click", function(){
        var toRemove = $(this).parent();
        console.log("click the close button");
        $.ajax({
            type: 'GET',
            url:  '/activity/delete/' + toRemove.attr('id'),
            success: function(){
                toRemove.remove();
                if (location.pathname.indexOf("user") !== -1){
                    location.reload();
                }
            }
        });
        $(this).tooltip('destroy');
    }).tooltip({title: "Delete this activity"});

});


// Key-value pairs of the form inputs
function getFormValues(form) {
    var result = { };
    $.each(form.serializeArray(), function() {
        result[this.name] = this.value;
    });
    return result;
}



function postMaker(id, name, description, location, creator){
    var postString =
        ['<div class="activity" id=' + id + '>',
            '<div class="activity-name">' + name + '</div>',
            '<div class="description">' + description + '</div>',
            '<div class="location">' + location + '</div>',
            '<div class="creator">by ' + creator + '</div>',
            '<img src="../static/img/close.png" class="delete-button" id="delete-button">',
            '<img src="../static/img/bucketIcon2.png" class="add-to-my-bucket" id="add-to-my-bucket">',
            '<img src="../static/img/complete.png" class="complete-activity" id="complete-activity">',
        '</div>',
        '<div class="hr"></div>'].join('\n');
    return postString;
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
