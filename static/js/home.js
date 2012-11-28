$(document).ready(function(){
    // create the function for the button rating
    $(".add-to-my-bucket").live("click", function(){
        var toRemove = $(this);
        console.log("click the add to my bucket button");
        $.ajax({
            type: 'GET',
            url:  '/activity/add/' + toRemove.parent().attr('id'),
            success: function(){
                toRemove.remove();
            }
        });
    });

    $(".delete-button").live("click", function(){
        var toRemove = $(this).parent();
        console.log("click the close button");
        $.ajax({
            type: 'GET',
            url:  '/activity/delete/' + toRemove.attr('id'),
            success: function(){
                toRemove.remove();
            }
        });
    });
});
