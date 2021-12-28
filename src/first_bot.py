import telebot
import site_parsing
from time import sleep

TOKEN = '1797743243:AAH8TG5ZApBA1eLmP3qsPYNVltU3jzw4OKg'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Bot started")
    while 1:
        for i in site_parsing.check_and_update():
            bot.send_message(chat_id, i)
        sleep(5)


bot.polling(none_stop=True, interval=2)
