import os
import telebot
from groq import Groq

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN").strip().replace("\n", "").replace(" ", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY").strip().replace("\n", "").replace(" ", "")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
groq_client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
1% وفادار، بزنس مائنڈڈ اور بلینرز کی سوچ رکھنے والے رائٹ ہینڈ پارٹنر ہو۔
نئی مہارتیں سیکھ کر اپلائی کرنا اور مجھے بہترین مشورے دینا ہے۔
تم میرے ساتھ ایک سچے بھائی اور وفادار ساتھی کی طرح کام کرو گے۔
"""

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user_input = message.text
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.polling()

