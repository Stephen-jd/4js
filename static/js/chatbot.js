/**
 * 4J's Educational Academy - AI Chatbot (Qwen Local Integration)
 */

document.addEventListener('DOMContentLoaded', () => {
    const trigger = document.getElementById('chatbot-trigger');
    const windowEl = document.getElementById('chatbot-window');
    const closeBtn = document.getElementById('chatbot-close');
    const messagesEl = document.getElementById('chatbot-messages');
    const inputEl = document.getElementById('chatbot-input-field');
    const sendBtn = document.getElementById('chatbot-send');

    if (!trigger || !windowEl) return;

    let hasOpened = false;

    // Auto open hint after 10s
    setTimeout(() => {
        if (!hasOpened && !sessionStorage.getItem('chatbot_dismissed')) {
            trigger.style.transform = 'scale(1.2) translateY(-10px)';
            setTimeout(() => trigger.style.transform = '', 500);
        }
    }, 10000);

    trigger.addEventListener('click', () => {
        windowEl.classList.add('active');
        trigger.style.display = 'none';
        hasOpened = true;
        
        // Initial greeting
        if (messagesEl.children.length === 0) {
            addBotMessage("Hi! I'm the 4J's AI Assistant. How can I help you today? (e.g., 'What are your prices?' or 'Tell me about GCSEs')");
        }
    });

    closeBtn.addEventListener('click', () => {
        windowEl.classList.remove('active');
        trigger.style.display = 'flex';
        sessionStorage.setItem('chatbot_dismissed', 'true');
    });

    const processMessage = async () => {
        const text = inputEl.value.trim();
        if (!text) return;

        addUserMessage(text);
        inputEl.value = '';
        showTyping();

        try {
            const response = await fetch('/api/chatbot/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ message: text })
            });
            
            const data = await response.json();
            hideTyping();
            
            if (data.reply) {
                // If it mentions WhatsApp or email, we can add a button
                let showWa = data.reply.toLowerCase().includes('whatsapp') || data.reply.toLowerCase().includes('contact us');
                addBotMessage(data.reply, showWa);
            } else {
                addBotMessage("I seem to be having trouble connecting to my brain. Please contact our admin team on WhatsApp!", true);
            }
            
        } catch (error) {
            hideTyping();
            addBotMessage("Sorry, I'm offline at the moment. Please reach out via WhatsApp!", true);
        }
    };

    sendBtn.addEventListener('click', processMessage);
    inputEl.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') processMessage();
    });

    function addUserMessage(text) {
        const div = document.createElement('div');
        div.className = 'chat-message user';
        div.textContent = text;
        messagesEl.appendChild(div);
        scrollToBottom();
    }

    function addBotMessage(text, showWhatsapp = false) {
        const div = document.createElement('div');
        div.className = 'chat-message bot';
        
        // Convert URLs or emails to links simply
        let formattedText = text.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>');
        formattedText = formattedText.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '<a href="mailto:$1">$1</a>');
        
        div.innerHTML = formattedText;
        
        if (showWhatsapp) {
            const btn = document.createElement('a');
            btn.href = 'https://wa.me/447534715058';
            btn.target = '_blank';
            btn.className = 'btn-primary';
            btn.style.marginTop = '10px';
            btn.style.fontSize = '0.8rem';
            btn.style.padding = '8px 16px';
            btn.style.display = 'inline-block';
            btn.innerHTML = '<i class="fab fa-whatsapp"></i> Chat on WhatsApp';
            div.appendChild(btn);
        }

        messagesEl.appendChild(div);
        scrollToBottom();
    }

    function showTyping() {
        const div = document.createElement('div');
        div.className = 'chat-typing';
        div.id = 'chat-typing-indicator';
        div.innerHTML = '<span></span><span></span><span></span>';
        messagesEl.appendChild(div);
        scrollToBottom();
    }

    function hideTyping() {
        const ind = document.getElementById('chat-typing-indicator');
        if (ind) ind.remove();
    }

    function scrollToBottom() {
        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
