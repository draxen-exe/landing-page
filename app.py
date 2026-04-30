from flask import Flask, render_template, request, jsonify
import os
import requests

# Try to load dotenv if available, useful for local development
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)

# Fetch Telegram credentials from environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TELEGRAM_TOPIC_ID = os.getenv('TELEGRAM_TOPIC_ID')

# Temporary in-memory counter since JSON storage is removed
in_memory_visits = 0

def send_telegram_message(text):
    """Helper function to send a message to a Telegram chat."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials not set in .env. Skipping message.")
        return False
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    
    # If a topic ID is provided, route the message to that specific thread
    if TELEGRAM_TOPIC_ID:
        payload["message_thread_id"] = TELEGRAM_TOPIC_ID
        
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code != 200:
            print(f"Failed to send Telegram message: {response.text}")
            return False
        return True
    except Exception as e:
        print(f"Error sending Telegram message: {e}")
        return False

@app.route('/')
def home():
    global in_memory_visits
    in_memory_visits += 1
    
    # Send an alert to Telegram on every new visit
    visit_msg = f"🚀 <b>New Visitor Alert!</b>\n\nSomeone just landed on Draxen.exe.\nTotal active session visits: {in_memory_visits}"
    send_telegram_message(visit_msg)
    
    return render_template('index.html', visits=in_memory_visits)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name', 'Unknown')
    email = data.get('email', 'No Email')
    message = data.get('message', '')
    
    # Format the message nicely for Telegram
    tg_text = (
        f"🚨 <b>New Transmission Received!</b>\n\n"
        f"👤 <b>ID:</b> {name}\n"
        f"📧 <b>Comms:</b> {email}\n\n"
        f"💬 <b>Payload:</b>\n{message}"
    )
    
    # Send it directly to Telegram instead of saving to JSON
    success = send_telegram_message(tg_text)
    
    # Also log to console for terminal debugging
    print("\n--- NEW TRANSMISSION RECEIVED ---")
    print(f"ID: {name}")
    print(f"Comms: {email}")
    print(f"Payload: {message}")
    print("---------------------------------\n")
    
    if success or (not TELEGRAM_BOT_TOKEN):
        # Return success if sent successfully OR if Telegram isn't configured yet (so frontend still works locally)
        return jsonify({'success': True, 'message': 'Message Sent ✅'})
    else:
        return jsonify({'success': False, 'message': 'Telegram API Error ❌'}), 500

if __name__ == '__main__':
    print("Initializing Draxen.exe Backend Server...")
    print(f"Telegram Integration: {'🟢 ACTIVE' if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID else '🔴 INACTIVE (Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env)'}")
    app.run(debug=True, port=5000)
