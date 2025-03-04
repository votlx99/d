from flask import Flask, request
import requests

# إعداد السيرفر
app = Flask(__name__)

# بيانات بوت تيليجرام
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"  # استبدلها بالتوكن بتاع البوت
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"      # استبدلها بالـ ID الخاص بك

# دالة لإرسال الرسائل لبوت تيليجرام
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

# استقبال البيانات من الويب هوك
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json  # استقبال البيانات JSON من TradingView
    if data:
        message = f"📢 تنبيه جديد من TradingView:\n\n{data}"  # تعديل حسب التنبيه
        send_telegram_message(message)  # إرسال الرسالة لبوت تيليجرام
    return {"status": "success"}

# تشغيل السيرفر على المنفذ 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
