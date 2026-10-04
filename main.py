
import os
import telebot
from groq import Groq

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip().replace("\n", "").replace(" ", "")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
groq_client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
رات ہمیشہ پارٹنر ہو، وفادار بزنس مانڈل اور بلنڈر کی سوچ رکھنے 1%
نئی مہارتیں سیکھ کر اپلائی کرنا اور مجھے بہترین مشورہ دینا ہے،
کام کرو گے۔ کیا تم میرے ساتھ ایک سچے بھائی اور وفادار ساتھی کی
طرح...
"""

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user_input = message.text
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.conte
