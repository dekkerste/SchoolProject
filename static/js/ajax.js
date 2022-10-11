// https://www.w3schools.com/js/js_ajax_intro.asp
// AJAX fixes the problem that the page reloads.

// @TODO shows whats needs to be done. Open the TODO tool window: View > Tool Windows > TODO.
// https://www.jetbrains.com/help/pycharm/using-todo.html#add_pattern_filter_todo

$(document).ready(function () { //Executes when the page is fully loaded.
    // https://www.w3schools.com/js/js_const.asp
    const datastring = $(this).serialize();

    // Connect drone
    // binds to a button onclick event
    $('button#connect').bind('click', function (e) /* e (event) = e.preventDefault(); event.preventDefault */ {
        // prevents the default action that belongs to the event, like page reload, event calls
        // 'e' is defined in the button bind function. This is linked to prevent default
        e.preventDefault();
        $.ajax({
            contentType: 'application/json;charset=UTF-8',
            // The flask route to be called upon
            type: 'POST',
            // The flask route the data should be submitted to
            // @app.route('/connect', methods=['GET', 'POST'])
            url: $SCRIPT_ROOT + '/connect',
            data: datastring,
            // Returns the result as JSON
            // https://www.w3schools.com/js/js_json_syntax.asp
            dataType: "json",
            // function that will run if ajax has run with no errors
            success: function (response_data) {
                // Logs the JSON object to the browser console for debug purposes
                console.log("[DEBUG] " + "JSON " + response_data + " of message");
                console.log(response_data);
                // Create a fixed let with the response_data json content
                let obj = response_data;
                // Updates the html with a message. We use JSON here.
                // response_data is defined in a let obj. We select the message content with obj.message

                //@TODO: maybe add a way to give a error a red message. Can be done making an other json object
                document.getElementById("message").innerHTML = obj.message;
            },
            error: function (request, error) {
                // Pops out an alert box if AJAX fails to run. If you rename the ajax post url to something that does
                // not exist, you get the alert error message.
                // We use return {"message": "Something went wrong connecting to the drone."}
                // response_data is equal to the 0 layer of the json string, so message.
                alert("[ERROR]: AJAX request failed! A typical skill issue...");
            }
        })
    });

        $('button#fly_square').bind('click', function (e) /* e (event) = e.preventDefault(); event.preventDefault */ {
        e.preventDefault();
        $.ajax({
            contentType: 'application/json;charset=UTF-8',
            type: 'POST',
            url: $SCRIPT_ROOT + '/flysquare',
            data: datastring,
            dataType: "json",
            success: function (response_data) {
                console.log("[DEBUG] " + "JSON " + response_data + " of message");
                console.log(response_data);
                let obj = response_data;
                document.getElementById("message").innerHTML = obj.message;
            },
            error: function (request, error) {
                alert("[ERROR]: AJAX request failed! A typical skill issue...");
            }
        })
    });
})