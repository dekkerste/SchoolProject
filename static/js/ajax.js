// https://www.w3schools.com/js/js_ajax_intro.asp
// AJAX fixes the problem that the page reloads.


$(document).ready(function () { //Executes when the page is fully loaded.

    var datastring = $(this).serialize();

    // Connect drone
    $('button#connect').bind('click', function (e) {
        // prevents the default action that belongs to the event, like page reload, event calls
        e.preventDefault();
        $.ajax({
            contentType: 'application/json;charset=UTF-8',
            // The flask route to be called upon
            type: 'POST',
            url: '/connectt',
            data: datastring,
            // Returns the result as JSON
            dataType: "json",
            // function that will run if ajax has run with no errors
            success: function (response_data) {
                // Logs the JSON object to the browser console for debug purposes
                console.log(response_data);
                // Updates the html with a message. We use JSON here, so we need to call the first layer message
                document.getElementById("message").innerHTML = response_data.message;
            },
            error: function (request, error) {
                // Pops out an alert box if AJAX fails to run. If you rename the ajax post url to something that does
                // not exist, you get the alert error message.
                alert("request failed");
            }
        })
    });
})