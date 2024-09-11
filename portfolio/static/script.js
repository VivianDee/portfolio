function handleCommand(event) {
    if (event.keyCode === 13) {
        var commandInput = $("#command");
        var command = commandInput.val().trim();
        commandInput.val("");
        $(".chatbox").hide();

        var output = $("#output");
        output.append("<div style='color: white;'><span>$</span> " + command + "</div>");

        switch (command) {
            case "clear":
                output.html("");
                break;
            case "help":
                displayHelp();
                break;
            case "1": case "intro":
                getInfo(command, ".");
                break;
            case "5": case "projects":
                getInfo(command, "<br>");
                break;
            case "7": case "chat":
                getInfo(command, "<br>");
                break;
            default:
                if (!command) {
                    displayHelp();
                } else {
                    getInfoWithDelay(command);
                }
                break;
        }
    }
}

function displayHelp() {
    var output = $("#output");
    output.append("<div>Available commands:</div>");
    output.append("<div>- 1: Intro</div>");
    output.append("<div>- 2: Experience</div>");
    output.append("<div>- 3: Education</div>");
    output.append("<div>- 4: Skills</div>");
    output.append("<div>- 5: Projects</div>");
    output.append("<div>- 6: Interests</div>");
    output.append("<div>- clear: Clear the screen</div>");
    output.append("<div>- help: Display this help message</div>");
    $('#shell').scrollTop($('#shell')[0].scrollHeight);
}

function getInfo(section, delimeter) {
    var commandInput = $("#command");
    var output = $("#output");
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "/get_info?section=" + section, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = xhr.responseText;
            output.append("<div id='temp'></div>");  // Create a temporary div to hold the content

            // Split the response text into sentences (you can modify this logic as needed)
            var sentences = response.split(delimeter);
            var currentIndex = 0;

            output.append("<div>" + sentences[currentIndex++] + "</div>");
            $('#shell').scrollTop($('#shell')[0].scrollHeight);
            $('#prompt').hide();

            commandInput.prop("disabled", true);

            // Display each sentence gradually
            var interval = setInterval(function() {
                if (currentIndex < sentences.length) {
                    var fullstop = currentIndex === sentences.length - 1 ? "" : delimeter;
                    output.append("<div>" + sentences[currentIndex++] + fullstop + "</div>");
                    $('#shell').scrollTop($('#shell')[0].scrollHeight);
                } else {
                    commandInput.prop("disabled", false);
                    clearInterval(interval); // Stop the interval when all sentences are displayed
                    $('#prompt').show();
                    commandInput.focus();
                }
            }, 4000); // Adjust the interval duration (milliseconds) as needed
        }
    };
    xhr.send();
}

function getInfoWithDelay(section) {
    var commandInput = $("#command");
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_info?section=" + section, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            $('#shell').scrollTop($('#shell')[0].scrollHeight);
            commandInput.prop("disabled", true);
            $('#prompt').hide();
            var output = $("#output");
            var response = xhr.responseText;
            var words = response.split(" ");
            var i = 0;
            var interval = setInterval(function() {
                output.append(words[i] + " ");
                $('#shell').scrollTop($('#shell')[0].scrollHeight);
                i++;
                if (i >= words.length) {
                    commandInput.prop("disabled", false);
                    clearInterval(interval);
                    $('#prompt').show();
                    commandInput.focus();
                }
            }, 300); // Change the delay as needed (in milliseconds)
        }
    };
    xhr.send();
}

function updateScroll(){
    $("#output").scrollTop($("#output").prop("scrollHeight"));
}

