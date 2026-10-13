const chatBox = document.getElementById("chatBox");
const messageInput = document.getElementById("message");
const sendBtn = document.getElementById("sendBtn");
let responseOptions = null;
let currentOptions = [];
let selectedOptions = new Set();
let optionsRequestInProgress = false;
let optionsRefreshQueued = false;


// ==========================================================
// SCROLL TO BOTTOM
// ==========================================================

function scrollToBottom() {

    if (!chatBox) {
        return;
    }

    chatBox.scrollTo({
        top: chatBox.scrollHeight,
        behavior: "smooth"
    });
}


// ==========================================================
// ADD MESSAGE
// ==========================================================

function addMessage(text, sender) {

    if (!chatBox) {
        return;
    }

    const row = document.createElement("div");

    row.className =
        "message-row " + sender;

    const bubble = document.createElement("div");

    bubble.className =
        "message-bubble";

    bubble.textContent = text;

    row.appendChild(bubble);

    chatBox.appendChild(row);

    scrollToBottom();
}


// ==========================================================
// SHOW RESULTS BUTTON
// ==========================================================

function showResultsButton() {

    if (!chatBox) {
        return;
    }

    // Don't create it twice
    if (
        document.getElementById("resultsButton")
    ) {
        return;
    }

    const button =
        document.createElement("a");

    button.id =
        "resultsButton";

    button.href =
        "/results";

    button.className =
        "results-button";

    button.textContent =
        "View My Recommendations";

    chatBox.appendChild(button);

    scrollToBottom();
}




// ==========================================================
// GUIDED RESPONSE OPTIONS
// ==========================================================

function clearResponseOptions() {
    if (responseOptions) {
        responseOptions.remove();
        responseOptions = null;
    }
    currentOptions = [];
    selectedOptions.clear();
}

function createOptionsBubble() {
    const row = document.createElement("div");
    row.className = "message-row bot guided-options-row";
    row.id = "guidedOptionsRow";

    const bubble = document.createElement("div");
    bubble.className = "message-bubble guided-options-bubble";
    bubble.setAttribute("aria-live", "polite");

    row.appendChild(bubble);
    chatBox.appendChild(row);
    responseOptions = bubble;
    return bubble;
}

async function loadResponseOptions() {
    if (!chatBox) return;

    try {
        const response = await fetch("/question-options", {
            headers: { "Accept": "application/json" },
            cache: "no-store"
        });
        if (!response.ok) return;

        const data = await response.json();

        // A new question gets a new in-chat options bubble. The name question
        // intentionally has no choices because names are personal text input.
        clearResponseOptions();
        currentOptions = Array.isArray(data.options) ? data.options : [];

        // Name is intentionally free text. Do not add an extra hint bubble;
        // guided choices appear naturally after the student answers the name question.
        if (!currentOptions.length) {
            return;
        }

        const bubble = createOptionsBubble();
        const hint = document.createElement("p");
        hint.className = "options-hint";
        hint.textContent = data.multi_select
            ? "Tap every answer that fits you, then send your selection."
            : "Tap the answer that fits you best.";
        bubble.appendChild(hint);

        const chips = document.createElement("div");
        chips.className = "option-chips";
        const visibleOptionCount = 6;
        let showAllOptions = false;
        const optionButtons = [];

        // Create submit button early so multi-select chip clicks can enable it.
        let submitButton = null;
        if (data.multi_select === true) {
            submitButton = document.createElement("button");
            submitButton.type = "button";
            submitButton.className = "option-submit";
            submitButton.textContent = "Use selected answers";
            submitButton.disabled = false;
            submitButton.setAttribute("aria-label", "Use selected answers");
            submitButton.addEventListener("click", async () => {
                if (messageInProgress) return;
                const chosen = Array.from(selectedOptions)
                    .map(key => currentOptions[Number(key)])
                    .filter(Boolean);
                if (!chosen.length) {
                    const existingNotice = bubble.querySelector(".options-selection-notice");
                    if (!existingNotice) {
                        const notice = document.createElement("p");
                        notice.className = "options-selection-notice";
                        notice.textContent = "Choose at least one option above, then click this button.";
                        bubble.insertBefore(notice, chips);
                    }
                    return;
                }

                const values = chosen.map(option => option.value);
                const labels = chosen.map(option => option.label);
                clearResponseOptions();
                await sendMessage(values.join(", "), labels.join(", "));
            });
        }

        currentOptions.forEach((option, index) => {
            const button = document.createElement("button");
            button.type = "button";
            button.className = "option-chip";
            button.textContent = option.label;
            button.dataset.optionIndex = String(index);
            button.setAttribute("aria-pressed", "false");
            if (index >= visibleOptionCount) button.hidden = true;

            button.addEventListener("click", async () => {
                if (messageInProgress) return;

                // Single-choice answers behave like clickable chat replies.
                if (data.multi_select !== true) {
                    const value = option.value;
                    const label = option.label;
                    clearResponseOptions();
                    await sendMessage(value, label);
                    return;
                }

                const key = String(index);
                if (selectedOptions.has(key)) {
                    selectedOptions.delete(key);
                    button.classList.remove("selected");
                    button.setAttribute("aria-pressed", "false");
                } else {
                    selectedOptions.add(key);
                    button.classList.add("selected");
                    button.setAttribute("aria-pressed", "true");
                }
                if (submitButton) {
                    submitButton.textContent = selectedOptions.size
                        ? `Use selected answers (${selectedOptions.size})`
                        : "Use selected answers";
                    submitButton.classList.toggle("has-selection", selectedOptions.size > 0);
                    const notice = bubble.querySelector(".options-selection-notice");
                    if (notice) notice.remove();
                }
            });
            optionButtons.push(button);
            chips.appendChild(button);
        });
        bubble.appendChild(chips);

        if (currentOptions.length > visibleOptionCount) {
            const moreButton = document.createElement("button");
            moreButton.type = "button";
            moreButton.className = "options-show-more";
            const remainingCount = currentOptions.length - visibleOptionCount;
            moreButton.textContent = `Show more options (${remainingCount})`;
            moreButton.setAttribute("aria-expanded", "false");
            moreButton.addEventListener("click", () => {
                showAllOptions = !showAllOptions;
                optionButtons.forEach((button, index) => {
                    button.hidden = !showAllOptions && index >= visibleOptionCount;
                });
                moreButton.textContent = showAllOptions
                    ? "Show fewer options"
                    : `Show more options (${remainingCount})`;
                moreButton.setAttribute("aria-expanded", String(showAllOptions));
            });
            bubble.appendChild(moreButton);
        }

        if (data.multi_select === true && submitButton) {
            const actions = document.createElement("div");
            actions.className = "option-actions";
            actions.appendChild(submitButton);
            bubble.appendChild(actions);
        }

        scrollToBottom();
    } catch (error) {
        console.error("Course Compass could not load response options:", error);
    }
}

// ==========================================================
// SEND MESSAGE
// ==========================================================

let messageInProgress = false;

async function sendMessage(messageOverride = null, displayOverride = null) {

    if (messageInProgress) {
        return;
    }

    // Make sure the input exists
    if (!messageInput) {
        console.error(
            "Course Compass: message input was not found."
        );
        return;
    }

    const message = (messageOverride !== null ? messageOverride : messageInput.value).trim();
    const displayMessage = displayOverride !== null ? displayOverride : message;

    // Don't send empty messages
    if (!message) {
        return;
    }

    // Remove the current option bubble when an answer is submitted, whether
    // it came from a chip or the text field. New options appear after the bot
    // responds and the next question is known.
    clearResponseOptions();

    // Show user's message immediately
    addMessage(
        displayMessage,
        "user"
    );

    // Clear input
    messageInput.value = "";

    // Prevent duplicate submissions while the server is processing.
    messageInProgress = true;

    if (sendBtn) {
        sendBtn.disabled = true;
    }

    try {

        const response =
            await fetch(
                "/message",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        message: message,
                        display_message: displayMessage
                    })
                }
            );


        // Get response
        const data =
            await response.json();

        // If the server lost this chat's in-memory state (for example, after
        // a restart), start a clean chat instead of applying the answer to the
        // wrong interview question. This does not change the page's appearance.
        if (data.reset_chat) {
            window.location.href = "/start";
            return;
        }

        // --------------------------------------------------
        // SERVER ERROR
        // --------------------------------------------------

        if (!response.ok || !data.success) {

            console.error(
                "Course Compass server error:",
                data
            );

            addMessage(
                data.error ||
                "Sorry, something went wrong. Please try again.",
                "bot"
            );

            return;
        }


        // --------------------------------------------------
        // DISPLAY BOT MESSAGES
        // --------------------------------------------------

        if (Array.isArray(data.messages)) {

            data.messages.forEach(
                function(item) {

                    if (
                        item.sender === "bot"
                    ) {

                        addMessage(
                            item.text,
                            "bot"
                        );
                    }
                }
            );
        }


        // --------------------------------------------------
        // SHOW RECOMMENDATIONS BUTTON
        // --------------------------------------------------

        if (
            data.finished ||
            data.show_results
        ) {
            clearResponseOptions();
            showResultsButton();
        } else {
            await loadResponseOptions();
        }

    }

    catch (error) {

        console.error(
            "Course Compass JavaScript error:",
            error
        );

        addMessage(
            "Sorry, something went wrong while contacting Course Compass. Please try again.",
            "bot"
        );
    }

    finally {

        messageInProgress = false;

        if (sendBtn) {
            sendBtn.disabled = false;
        }

        messageInput.focus();

        scrollToBottom();
    }
}


// ==========================================================
// SEND BUTTON
// ==========================================================

if (sendBtn) {

    sendBtn.addEventListener(
        "click",
        function(event) {

            event.preventDefault();

            sendMessage();
        }
    );

} else {

    console.error(
        "Course Compass: sendBtn was not found."
    );
}


// ==========================================================
// ENTER KEY
// ==========================================================

if (messageInput) {

    messageInput.addEventListener(
        "keydown",
        function(event) {

            if (event.key === "Enter") {

                event.preventDefault();

                sendMessage();
            }
        }
    );

} else {

    console.error(
        "Course Compass: message input was not found."
    );
}


// ==========================================================
// PAGE LOAD
// ==========================================================

window.addEventListener(
    "load",
    function() {

        scrollToBottom();
        loadResponseOptions();

        if (messageInput) {
            messageInput.focus();
        }
    }
);