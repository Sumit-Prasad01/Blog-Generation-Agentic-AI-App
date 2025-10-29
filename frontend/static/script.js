const sidebar = document.getElementById("sidebar");
const toggleBtn = document.getElementById("toggleSidebar");
const sidebarTitle = document.getElementById("sidebarTitle");
const navLinks = document.getElementById("navLinks");
const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");

let isCollapsed = false;

// Toggle sidebar
toggleBtn.addEventListener("click", () => {
  isCollapsed = !isCollapsed;

  if (isCollapsed) {
    sidebar.style.width = "80px";
    sidebarTitle.style.opacity = "0";
    navLinks.style.opacity = "0";
    setTimeout(() => {
      sidebarTitle.style.display = "none";
      navLinks.style.display = "none";
    }, 300);
  } else {
    sidebar.style.width = "256px";
    sidebarTitle.style.display = "block";
    navLinks.style.display = "block";
    setTimeout(() => {
      sidebarTitle.style.opacity = "1";
      navLinks.style.opacity = "1";
    }, 10);
  }
});

// Send message function
function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  // Add user message
  const userMsg = document.createElement("div");
  userMsg.className = "text-right";
  userMsg.innerHTML = `
          <div class="bg-indigo-600 text-white inline-block rounded-lg px-4 py-2 shadow max-w-xl">
            ${message}
          </div>
        `;
  chatBox.appendChild(userMsg);

  // Clear input
  userInput.value = "";

  // Scroll to bottom
  chatBox.scrollTop = chatBox.scrollHeight;

  // Simulate AI response
  setTimeout(() => {
    const aiMsg = document.createElement("div");
    aiMsg.className = "text-left";
    aiMsg.innerHTML = `
            <div class="bg-white text-[#0a1a2f] inline-block rounded-lg px-4 py-2 shadow max-w-xl">
              ✨ Great topic! Let me help you create content about "${message}". Here's a draft outline...
            </div>
          `;
    chatBox.appendChild(aiMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }, 1000);
}

// Event listeners
sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    sendMessage();
  }
});

