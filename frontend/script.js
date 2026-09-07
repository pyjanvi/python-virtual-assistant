async function sendMessage() {
    const input = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    // Show user's message
    chatBox.innerHTML += `
        <div class="user-message">
            <strong>You:</strong> ${message}
        </div>
    `;

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error("Backend error");
        }

        const data = await response.json();

        // Show assistant response
        chatBox.innerHTML += `
            <div class="bot-message">
                <strong>Assistant:</strong> ${data.response}
            </div>
        `;

    } catch (error) {
        chatBox.innerHTML += `
            <div class="bot-message">
                <strong>Assistant:</strong> Backend is not running.
            </div>
        `;

        console.error(error);
    }

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}


// 🎤 Voice Recognition
function startListening() {

    const input = document.getElementById("message");

    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Speech recognition is not supported in this browser.");
        return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-IN";
    recognition.interimResults = false;
    recognition.continuous = false;

    recognition.onstart = function () {
        console.log("Listening...");
    };

    recognition.onresult = function (event) {

        const transcript = event.results[0][0].transcript;

        console.log("You said:", transcript);

        input.value = transcript;

        // Automatically send the recognized message
        sendMessage();
    };

    recognition.onerror = function (event) {
        console.error("Speech recognition error:", event.error);
    };

    recognition.onend = function () {
        console.log("Stopped listening.");
    };

    recognition.start();
}


// Press Enter to send
document.getElementById("message").addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }

});