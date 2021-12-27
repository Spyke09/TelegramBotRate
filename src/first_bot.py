from telegram.ext import Updater
import site_parsing
import logging
from telegram.ext import CommandHandler
from time import sleep


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Начало работы")



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '1797743243:AAH8TG5ZApBA1eLmP3qsPYNVltU3jzw4OKg'
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
site_parsing.create_json()
while 1:
    sleep(5)
    a = site_parsing.check()
    if a:
        for i in a:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Начало работы")

