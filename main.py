import telebot
from telebot import types
import random
from api_keys import telegram_bot_key  # your own token


keys = Keys()
bot = telebot.TeleBot(telegram_bot_key)


@bot.message_handler(commands=["start"])
def start(message):
    text = 'Это тестовый бот Степанова Дениса.' \
           'С чего хотели бы начать?' \
           'Все команды можно узнать если написать /help в чат'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["help"])
def help_command(message):
    with open('commands.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        bot.send_message(message.chat.id, text)


def open_keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    greeting = types.KeyboardButton('hello')
    get_id = types.KeyboardButton('id')
    get_photo = types.KeyboardButton('photo')
    get_sticker = types.KeyboardButton('sticker')
    get_music = types.KeyboardButton('music')
    get_github = types.KeyboardButton('github')

    markup.add(greeting, get_id, get_photo, get_sticker, get_music, get_github)
    sticker_id = ['CAACAgIAAxkBAAEIUaNkHv4wNBR0egm--BGulAPu_qzCDgACHA4AAjGLiUvymLr-EpI_yC8E',
                  'CAACAgIAAxkBAAEIUaVkHv6Hxlej3mMWMJxVrDi-UDw68QACkQ0AAiypkUsY0bKk3fH5Qy8E',
                  'CAACAgIAAxkBAAEIUapkHv6MGAvgLXTMxpRH0-msnzKXzwACsA4AAjm7kEu4R3lPf_scHC8E',
                  'CAACAgIAAxkBAAEIUa5kHv6x5H6zyPTFUsCN98CE1x30vQACEA8AArANkUulanYn3R4Nai8E']
    sid = random.randint(0, len(sticker_id) - 1)
    bot.send_sticker(message.chat.id, sticker_id[sid], reply_markup=markup)


@bot.message_handler(commands=['menu'])
def buttons(message):
    open_keyboard(message)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    if message.text == "menu":
        open_keyboard(message)

    elif message.text == "hello":
        text = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
        a = types.KeyboardButton('menu')
        markup.add(a)
        bot.send_message(message.chat.id, text, reply_markup=markup)

    elif message.text == "id":
        text = f'Твой ID: {message.from_user.id}'
        a = types.KeyboardButton('menu')
        markup.add(a)
        bot.send_message(message.chat.id, text, reply_markup=markup)

    elif message.text == "photo":
        photo = open("static/img/picture.jpeg", "rb")
        a = types.KeyboardButton('menu')
        markup.add(a)
        bot.send_photo(message.chat.id, photo, reply_markup=markup)

    elif message.text == "sticker":
        sticker_id = 'CAACAgIAAxkBAAEIUbBkHv8TxamBq_InCGx_RQ9qjtSF-AACfREAAqU0yEtUPRwUwa1a1S8E'
        a = types.KeyboardButton('menu')
        markup.add(a)
        bot.send_sticker(message.chat.id, sticker_id, reply_markup=markup)

    elif message.text == "music":
        with open('static/audio/music.mp3', 'rb') as audio:
            a = types.KeyboardButton('menu')
            markup.add(a)
            bot.send_audio(message.chat.id, audio, reply_markup=markup)
    elif message.text == "github":
        link = 'https://github.com/mor1nch'
        a = types.KeyboardButton('menu')
        markup.add(a)
        bot.send_message(message.chat.id, link, reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'ладно')


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Великолепное фото! Расскажите подробнее.')


bot.polling(none_stop=True)
