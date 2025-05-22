$(document).ready(function () {
  function appendMessage(role, message) {
    let imgSrc =
      role === "user"
        ? "https://img.icons8.com/material-sharp/96/user.png"
        : "https://img.icons8.com/ios-filled/100/bot.png";

    let alignmentClass = role === "user" ? "user-message" : "chatbot-message";

    // 🔹 Aplica `marked.parse()` apenas nas mensagens do chatbot
    let formattedMessage = role === "chatbot" ? marked.parse(message) : message;

    let messageHtml = `
          <div class="message ${alignmentClass}">
              ${
                role === "user"
                  ? `<div class="text">${formattedMessage}</div><img src="${imgSrc}" alt="${role}">`
                  : `<img src="${imgSrc}" alt="${role}"><div class="text">${formattedMessage}</div>`
              }
          </div>
      `;

    $("#chat-box").append(messageHtml);
    $("#chat-box").scrollTop($("#chat-box")[0].scrollHeight);
  }

  async function fetchStreamedResponse(userMessage) {
    appendMessage("user", userMessage);

    const response = await fetch(
      `/chatia_response/?message=${encodeURIComponent(userMessage)}`
    );
    if (!response.ok) {
      appendMessage("chatbot", "Erro ao obter resposta do servidor.");
      return;
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let botMessage = "";

    let assistantMessageElement = $(`
      <div class="message chatbot-message">
        <img src="https://img.icons8.com/ios-filled/100/bot.png">
        <div class="text"></div>
      </div>
    `);

    $("#chat-box").append(assistantMessageElement);
    let textContainer = assistantMessageElement.find(".text");

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      const textChunk = decoder.decode(value, { stream: true });
      botMessage += textChunk;

      // 🔹 Aplica Markdown corretamente
      textContainer.html(marked.parse(botMessage));

      $("#chat-box").scrollTop($("#chat-box")[0].scrollHeight);
    }
  }

  $("#send-btn").click(function () {
    let userMessage = $("#user-input").val().trim();
    if (userMessage !== "") {
      $("#user-input").val("");
      fetchStreamedResponse(userMessage);
    }
  });

  $("#user-input").keypress(function (event) {
    if (event.which == 13) {
      event.preventDefault();
      $("#send-btn").click();
    }
  });
});
