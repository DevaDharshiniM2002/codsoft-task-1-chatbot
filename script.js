// ======================================================
// DAILY LIFE CHATBOT - GUIDED CONVERSATION
// ======================================================

let currentQuestion = 0;
let userName = "";

const questions = [
    {
        question: "What's your name?",
        response: function(answer) {
            userName = answer;
            return `Nice to meet you, ${capitalize(answer)}! 😊`;
        }
    },

    {
        question: "How was your day today?",
        response: function(answer) {
            if (
                answer.includes("good") ||
                answer.includes("great") ||
                answer.includes("nice") ||
                answer.includes("awesome") ||
                answer.includes("fine")
            ) {
                return "That's wonderful to hear! 😄";
            }

            if (
                answer.includes("bad") ||
                answer.includes("sad") ||
                answer.includes("tired")
            ) {
                return "I'm sorry to hear that. ❤️ I hope tomorrow is better!";
            }

            return "Thanks for sharing that with me! 😊";
        }
    },

    {
        question: "What did you do today?",
        response: function(answer) {
            if (answer.includes("college")) {
                return "Nice! 📚 How was college today?";
            }

            if (answer.includes("school")) {
                return "That's nice! 🏫 How was school today?";
            }

            if (answer.includes("home")) {
                return "Staying at home can be relaxing! 🏠";
            }

            return "Sounds interesting! 👍";
        }
    },

    {
        question: "Did you enjoy your day? (yes/no)",
        response: function(answer) {
            if (
                answer === "yes" ||
                answer === "yeah" ||
                answer === "yep"
            ) {
                return "That's great! I'm happy for you. 😊";
            }

            return "I hope tomorrow will be a better day! 🌟";
        }
    },

    {
        question: "What do you usually do in the morning?",
        response: function(answer) {
            return "Nice morning routine! ☀️";
        }
    },

    {
        question: "What is your favorite food?",
        response: function(answer) {
            if (answer.includes("biryani")) {
                return "Wow! Biryani sounds delicious! 🍛";
            }

            if (answer.includes("dosa")) {
                return "Dosa is a tasty choice! 😋";
            }

            return `${capitalize(answer)} sounds delicious! 🍴`;
        }
    },

    {
        question: "What is your favorite drink?",
        response: function(answer) {
            return `${capitalize(answer)} sounds refreshing! 🥤`;
        }
    },

    {
        question: "What is your favorite color?",
        response: function(answer) {
            return `${capitalize(answer)} is a beautiful choice! 🎨`;
        }
    },

    {
        question: "What do you like to do in your free time?",
        response: function(answer) {
            if (answer.includes("music")) {
                return "That's nice! Music is a great way to relax. 🎵";
            }

            if (answer.includes("tv") || answer.includes("watch")) {
                return "Watching TV is a nice way to relax! 📺";
            }

            if (answer.includes("game")) {
                return "Gaming sounds fun! 🎮";
            }

            if (answer.includes("read")) {
                return "Reading is a wonderful hobby! 📚";
            }

            return "That's a great hobby! 😊";
        }
    },

    {
        question: "What kind of music do you like?",
        response: function(answer) {
            return `${capitalize(answer)} music sounds interesting! 🎵`;
        }
    },

    {
        question: "What is your favorite movie?",
        response: function(answer) {
            return `Nice choice! 🎬 ${capitalize(answer)} sounds interesting.`;
        }
    },

    {
        question: "Are you studying, working, or doing something else?",
        response: function(answer) {
            if (answer.includes("study")) {
                return "That's great! 📚 Keep learning and growing!";
            }

            if (answer.includes("work")) {
                return "Sounds good! 💼 Keep doing your best!";
            }

            return "Sounds good! 😊";
        }
    },

    {
        question: "Do you like traveling? (yes/no)",
        response: function(answer) {
            if (
                answer === "yes" ||
                answer === "yeah" ||
                answer === "yep"
            ) {
                return "That's wonderful! Traveling is exciting! 🌍";
            }

            return "That's okay! Staying home can be fun too. 🏠";
        }
    },

    {
        question: "Where would you like to travel?",
        response: function(answer) {
            if (answer.includes("ooty")) {
                return "Ooty sounds like a beautiful place to visit! 🏔️";
            }

            if (answer.includes("bali")) {
                return "Bali would be an amazing place to visit! 🌴";
            }

            return `${capitalize(answer)} sounds like a great place to visit! 🌍`;
        }
    },

    {
        question: "What do you usually do on weekends?",
        response: function(answer) {
            if (answer.includes("sleep")) {
                return "Sounds relaxing! 😴 Everyone needs some rest.";
            }

            if (answer.includes("play")) {
                return "Sounds fun! 🎮 Enjoy your weekend!";
            }

            return "Sounds like a nice weekend! 😊";
        }
    },

    {
        question: "What do you usually do in the evening?",
        response: function(answer) {
            return "Sounds like a nice evening routine! 🌆";
        }
    },

    {
        question: "What time do you usually go to sleep?",
        response: function(answer) {
            return "Getting enough sleep is important. 😴";
        }
    },

    {
        question: "What is something that makes you happy?",
        response: function(answer) {
            return "That's wonderful! 😊 It's important to enjoy the little things in life.";
        }
    },

    {
        question: "What is your favorite season?",
        response: function(answer) {
            if (answer.includes("winter")) {
                return "Winter can be cozy and relaxing! ❄️";
            }

            if (answer.includes("summer")) {
                return "Summer is full of fun and sunshine! ☀️";
            }

            if (answer.includes("rain")) {
                return "Rainy days can feel so peaceful! 🌧️";
            }

            return `${capitalize(answer)} sounds like a lovely season! 🌿`;
        }
    }
];


// ======================================================
// START CHAT
// ======================================================

function startChat() {

    currentQuestion = 0;
    userName = "";

    const chatArea = document.getElementById("chatArea");

    chatArea.innerHTML = "";

    addBotMessage(
        "Hi! 👋 Welcome to my Daily Life Chatbot!"
    );

    setTimeout(function() {

        askNextQuestion();

    }, 500);
}


// ======================================================
// ASK NEXT QUESTION
// ======================================================

function askNextQuestion() {

    if (currentQuestion >= questions.length) {

        finishChat();

        return;
    }

    const question = questions[currentQuestion].question;

    setTimeout(function() {

        addBotMessage(question);

    }, 350);
}


// ======================================================
// SEND MESSAGE
// ======================================================

function sendMessage() {

    const input = document.getElementById("messageInput");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    addUserMessage(message);

    input.value = "";

    // Goodbye
    if (
        message.toLowerCase() === "bye" ||
        message.toLowerCase() === "exit"
    ) {

        setTimeout(function() {

            addBotMessage(
                "It was really nice talking with you! 👋 Have a wonderful day!"
            );

        }, 400);

        return;
    }

    // Current question response
    if (currentQuestion < questions.length) {

        const response =
            questions[currentQuestion].response(
                message.toLowerCase()
            );

        currentQuestion++;

        setTimeout(function() {

            addBotMessage(response);

            setTimeout(function() {

                askNextQuestion();

            }, 450);

        }, 400);

    }
}


// ======================================================
// ADD USER MESSAGE
// ======================================================

function addUserMessage(message) {

    const chatArea =
        document.getElementById("chatArea");

    const messageElement =
        document.createElement("div");

    messageElement.className =
        "message user-message";

    messageElement.innerHTML = `

        <div class="message-content">

            <div class="message-name">
                You
            </div>

            <div class="bubble">
                ${escapeHTML(message)}
            </div>

            <div class="time">
                ${getCurrentTime()}
            </div>

        </div>
    `;

    chatArea.appendChild(messageElement);

    scrollToBottom();
}


// ======================================================
// ADD BOT MESSAGE
// ======================================================

function addBotMessage(message) {

    const chatArea =
        document.getElementById("chatArea");

    const messageElement =
        document.createElement("div");

    messageElement.className =
        "message bot-message";

    messageElement.innerHTML = `

        <div class="message-avatar">
            🤖
        </div>

        <div class="message-content">

            <div class="message-name">
                Bot
            </div>

            <div class="bubble">
                ${escapeHTML(message)}
            </div>

            <div class="time">
                ${getCurrentTime()}
            </div>

        </div>
    `;

    chatArea.appendChild(messageElement);

    scrollToBottom();
}


// ======================================================
// FINISH CHAT
// ======================================================

function finishChat() {

    setTimeout(function() {

        addBotMessage(
            `It was really nice chatting with you, ${
                userName ? capitalize(userName) : "friend"
            }! 😊`
        );

    }, 400);

    setTimeout(function() {

        addBotMessage(
            "Have a wonderful day! Take care! 👋"
        );

    }, 900);
}


// ======================================================
// CLEAR CHAT
// ======================================================

function clearChat() {

    startChat();
}


// ======================================================
// CURRENT TIME
// ======================================================

function getCurrentTime() {

    const now = new Date();

    return now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}


// ======================================================
// CAPITALIZE
// ======================================================

function capitalize(text) {

    if (!text) {
        return "";
    }

    return text.charAt(0).toUpperCase() + text.slice(1);
}


// ======================================================
// SCROLL
// ======================================================

function scrollToBottom() {

    const chatArea =
        document.getElementById("chatArea");

    chatArea.scrollTop =
        chatArea.scrollHeight;
}


// ======================================================
// ENTER KEY
// ======================================================

document
    .getElementById("messageInput")
    .addEventListener("keydown", function(event) {

        if (event.key === "Enter") {

            event.preventDefault();

            sendMessage();
        }
    });


// ======================================================
// SECURITY
// ======================================================

function escapeHTML(text) {

    const div =
        document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}


// ======================================================
// START
// ======================================================

startChat();