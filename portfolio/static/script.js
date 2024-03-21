function handleCommand(event) {
    if (event.keyCode === 13) {
        var commandInput = document.getElementById("command");
        var command = commandInput.value.trim();
        commandInput.value = "";

        var output = document.getElementById("output");
        output.innerHTML += "<div style='color: white;'><span>$</span> " + command + "</div>";

        if (command === "clear") {
            output.innerHTML = "";
        } else if (command === "help") {
            displayHelp();
        } else {
            getInfo(command);
        }
    }
}

function displayHelp() {
    var output = document.getElementById("output");
    output.innerHTML += "<div>Available commands:</div>";
    output.innerHTML += "<div>- clear: Clear the screen</div>";
    output.innerHTML += "<div>- help: Display this help message</div>";
    output.scrollTop = output.scrollHeight;
}

function getInfo(section) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_info?section=" + section, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var output = document.getElementById("output");
            output.innerHTML += xhr.responseText;
            output.scrollTop = output.scrollHeight;
        }
    };
    xhr.send();
}
