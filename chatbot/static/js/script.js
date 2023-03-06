const chatLog = document.getElementById("chat-log");
const chatbotLog = document.getElementById("chatbot-log");
const questionInput = document.getElementById("question");

document.querySelector("form").addEventListener("submit", (event) => {
  event.preventDefault();
  const question = questionInput.value;
  if (question !== "") {
    chatLog.innerHTML += `<p><strong>User:</strong> ${question}</p>`;
    questionInput.value = "";
    // Send question to server
    fetch(`/chatbot?question=${question}`)
      .then((response) => response.json())
      .then((data) => {
        const answer = data.answer;
        chatLog.innerHTML += `<p><strong>Chatbot:</strong> ${answer}</p>`;
      })
      .catch((error) => {
        console.error(error);
      });
  }
});

chatbotLog.innerHTML += `<p><strong>Chatbot:</strong> Hi, I'm WikiLookup. I can help you find information on Wikipedia. Ask me a question!</p>`;
