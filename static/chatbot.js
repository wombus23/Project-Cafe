document.addEventListener("DOMContentLoaded", function () {
    const chatMessages = document.getElementById("chat-messages");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    // Function to add a message to the chat-messages div
    function addMessage(message, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.className = sender === "user" ? "user-message" : "bot-message";
        messageDiv.textContent = message;
        chatMessages.appendChild(messageDiv);
    }

    async function handleUserInput() {
        const userMessage = userInput.value.trim();
        if (userMessage !== "") {
            addMessage(userMessage, "user");
    
            // Retrieve the CSRF token from a cookie
            const csrftoken = getCookie('csrftoken');
    
            try {
                // Send user message to the server and get the chatbot response
                const response = await fetch("/chatbot/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrftoken, // Include the correct CSRF token in the header
                    },
                    body: JSON.stringify({ user_message: userMessage }),
                });
    
                if (response.ok) {
                    const data = await response.json();
                    const chatbotResponse = data.response;
                    addMessage(chatbotResponse, "bot");
                } else {
                    addMessage("An error occurred while processing your request.", "bot");
                }
            } catch (error) {
                console.error(error);
                addMessage("An error occurred while processing your request.", "bot");
            }
    
            // Clear the input field
            userInput.value = "";
        }
    }
    

    // Event listener for the send button
    sendButton.addEventListener("click", handleUserInput);

    // Event listener for pressing Enter key in the input field
    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            handleUserInput();
        }
    });

    // Implement your getCookie function here if needed
    function getCookie(name) {
        const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    }
});
