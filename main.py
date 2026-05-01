from app import app, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

if __name__ == '__main__':
    print("Initializing Draxen.exe Backend Server...")
    print(f"Telegram Integration: {'🟢 ACTIVE' if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID else '🔴 INACTIVE (Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env)'}")
    app.run(debug=True, port=5000)
