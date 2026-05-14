import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 Orion Flow AI online com sucesso!")

print("BOT ONLINE...")
bot.infinity_polling()
