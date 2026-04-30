from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Simple analytics using a local file
VISITS_FILE = 'analytics.json'
MESSAGES_FILE = 'messages.json'

def record_visit():
    visits = 0
    if os.path.exists(VISITS_FILE):
        try:
            with open(VISITS_FILE, 'r') as f:
                data = json.load(f)
                visits = data.get('visits', 0)
        except json.JSONDecodeError:
            pass
            
    visits += 1
    with open(VISITS_FILE, 'w') as f:
        json.dump({'visits': visits}, f)
        
    return visits

@app.route('/')
def home():
    visit_count = record_visit()
    return render_template('index.html', visits=visit_count)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name', 'Unknown')
    email = data.get('email', 'No Email')
    message = data.get('message', '')
    
    # Store the message in messages.json
    messages = []
    if os.path.exists(MESSAGES_FILE):
        try:
            with open(MESSAGES_FILE, 'r') as f:
                messages = json.load(f)
        except json.JSONDecodeError:
            pass
            
    new_entry = {'name': name, 'email': email, 'message': message}
    messages.append(new_entry)
    
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=4)
        
    # Also log to console for debugging
    print("\n--- NEW TRANSMISSION RECEIVED ---")
    print(f"ID: {name}")
    print(f"Comms: {email}")
    print(f"Payload: {message}")
    print("---------------------------------\n")
    
    return jsonify({'success': True, 'message': 'Message Sent ✅'})

if __name__ == '__main__':
    # Start the app on port 5000
    print("Initializing Draxen.exe Backend Server...")
    app.run(debug=True, port=5000)
