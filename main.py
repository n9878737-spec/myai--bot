import os
import telebot
from groq import Groq

TELEGRAM_TOKEN = "8986237392:AAHQ-Ahsj0znq7JhVSPQD_ZjOwotkDxDwY0"
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip().replace("\n", "").replace(" ", "")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
groq_client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
1% وفادار، بزنس مائنڈڈ اور بلینرز کی سوچ رکھنے वाले رائٹ ہینڈ پارٹنر ہو۔
نئی مہارتیں سیکھ کر اپلائی کرنا اور مجھے بہترین مشورے دینا ہے۔
تم میرے ساتھ ایک سچے بھائی اور وفادار ساتھی کی तरह کام کرو گے۔
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

        reply = response.choices[0].message.content
        bot.reply_to(message, reply)
    except Exception as e:
       bot.reply_to(message, f"Error: {str(e)}")

bot.polling()
