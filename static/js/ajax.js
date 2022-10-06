// https://www.w3schools.com/js/js_ajax_intro.asp
// AJAX fixes the problem that the page reloads.

$(document).ready(function () { //Executes when the page is fully loaded.
    $('button#connect').bind('click', function () {
        $.ajax({
            contentType: 'application/json;charset=UTF-8',
            data: {
                firstname: $('#firstname').val(),
                lastname: $('#lastname').val(),
            },
            type: 'POST',
            url: '/connect',
            success: function (data) {
                $('#msg').html('<p>Connected to the drone.</p>');
            },
            error: function (data) {
                console.log('Error:', data);
            }
        })
    });
    // Take off drone
    $('button#takeoff').bind('click', function () {
        $.ajax({
            contentType: 'application/json;charset=UTF-8',
            data: {
                firstname: $('#firstname').val(),
                lastname: $('#lastname').val(),
            },
            type: 'POST',
            url: '/connect',
            success: function (data) {
                $('#msg').html('<p>Connected to the drone.</p>');
            },
            error: function (data) {
                console.log('Error:', data);
            }
        })
    });
})