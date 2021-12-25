import telegram
import site_parsing

TOKEN = '1797743243:AAH8TG5ZApBA1eLmP3qsPYNVltU3jzw4OKg'
bot = telegram.Bot(token=TOKEN)

for k, t in enumerate(times):
    if t.split()[0] == yesterday_str:  # если новость за вчера, то постим
        # Непосредственно здесь идет отправка. Инициализируем бота с помощью токена
        bot = telegram.Bot(token='123456789:AABBCCDDefgh_mnaviwuue_DP865Y')
        chat_id = '@here_some_channel_to_post'
        # тест новости
        chat_text = 'Новая новость на <a href="http://здесь-урл-сайта.ru">сайте</a>:\n <b>{}</b>'.format(h2s[k])
        # отправка поста в канал. Маленькая тонкость - используется HTML разметка
        bot.send_message(chat_id=chat_id, text=chat_text, parse_mode=telegram.ParseMode.HTML)