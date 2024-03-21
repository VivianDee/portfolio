function handleCommand(event) {
    if (event.keyCode === 13) {
        var commandInput = $("#command");
        var command = commandInput.val().trim();
        commandInput.val("");

        var output = $("#output");
        output.append("<div style='color: white;'><span>$</span> " + command + "</div>");

        switch (command) {
            case "clear":
                output.html("");
                break;
            case "help":
                displayHelp();
                break;
            case "1": case "2":
                getInfo(command);
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
    output.scrollTop(output.prop("scrollHeight"));
}

function getInfo(section) {
    var commandInput = $("#command");
    var output = $("#output");
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "/get_info?section=" + section, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = xhr.responseText;
            output.append("<div id='temp'></div>");  // Create a temporary div to hold the content

            // Split the response text into sentences (you can modify this logic as needed)
            var sentences = response.split('.');
            var currentIndex = 0;

            output.append("<div>" + sentences[currentIndex++] + "." + "</div>");

            commandInput.prop("disabled", true);

            // Display each sentence gradually
            var interval = setInterval(function() {
                if (currentIndex < sentences.length) {
                    var fullstop = currentIndex === sentences.length - 1 ? "" : ".";
                    output.append("<div>" + sentences[currentIndex++] + fullstop + "</div>");
                    output.scrollTop(output.prop("scrollHeight")); // Scroll to the bottom
                } else {
                    commandInput.prop("disabled", false);
                    clearInterval(interval); // Stop the interval when all sentences are displayed
                }
            }, 4000); // Adjust the interval duration (milliseconds) as needed
        }
    };
    xhr.send();
}

function getInfoWithDelay(section) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_info?section=" + section, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var output = $("#output");
            var response = xhr.responseText;
            var words = response.split(" ");
            var i = 0;
            var interval = setInterval(function() {
                output.append(words[i] + " ");
                output.scrollTop(output.prop("scrollHeight"));
                i++;
                if (i >= words.length) {
                    clearInterval(interval);
                }
            }, 300); // Change the delay as needed (in milliseconds)
        }
    };
    xhr.send();
}
