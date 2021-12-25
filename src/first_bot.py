from telegram.ext import Updater
import site_parsing
import logging
from telegram.ext import CommandHandler



def start(update, context):
    # `bot.send_message` это метод Telegram API
    # `update.effective_chat.id` - определяем `id` чата,
    # откуда прилетело сообщение
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '1797743243:AAH8TG5ZApBA1eLmP3qsPYNVltU3jzw4OKg'
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

