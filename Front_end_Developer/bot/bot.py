import telebot
from decouple import config

BOT_TOKEN = config("BOT_TOKEN")


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def welcome(massage):
    bot.send_message(massage.chat.id, "welcome")


@bot.message_handler(commands=["w", "w"])
def welcome(massage):
    bot.send_message(massage.chat.id, "ok")


bot.polling()
