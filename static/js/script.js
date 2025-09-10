$(document).ready(function () {
  $("#send-btn").click(function () {
    let message = $("#user-input").val().trim();
    if (message === "") return;

    // ✅ Show user message
    $("#chat-box").append(
      `<div class="user-message">You: ${message}</div>`
    );
    $("#user-input").val("");

    // ✅ Send to Flask
    $.ajax({
      url: "/chat",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({ message: message }),
      success: function (response) {
        // ✅ Show bot reply
        $("#chat-box").append(
          `<div class="bot-message">Bot: ${response.reply}</div>`
        );
        $("#chat-box").scrollTop($("#chat-box")[0].scrollHeight); // auto scroll
      }
    });
  });

  // ✅ Enter key support
  $("#user-input").keypress(function (e) {
    if (e.which == 13) {
      $("#send-btn").click();
    }
  });
});
