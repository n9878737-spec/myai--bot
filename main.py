
import os
import telebot
from groq import Groq

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip().replace("\n", "").replace(" ", "")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
groq_client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """

Raat hamesha partner ho, wafadar business model aur blunder ki soch rakhne 1%.
Nayi mahartein seekh kar apply karna aur mujhe behtareen mashwara dena hai,
kaam karoge. Kya tum mere sath aik sachay bhai aur wafadar sathi ki
tarah...
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
        r
