import config
import temp
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
previous = ''
@bot.message_handler(content_types=['text'])
def lalala(message):
    global previous
    if message.chat.type == 'private':
        if message.text == 'Погода':
            bot.send_message(message.chat.id, "Выберите город",
                             reply_markup=keyboard_for_weather())
        elif message.text == 'Калькулятор':
            bot.send_message(message.chat.id, 'Введите выражение типа 9+7:')
        elif message.text != 'Погода' and message.text != 'Калькулятор' and previous == 'Калькулятор':
            bot.send_message(message.chat.id, str(eval(message.text)),
                             reply_markup=keyboard())
        elif message.text == 'Екатеринбург':
            bot.send_message(message.chat.id, temp.temp(message.text),
                                reply_markup=keyboard())
        elif message.text == 'Москва':
            bot.send_message(message.chat.id, temp.temp(message.text),
                                reply_markup=keyboard())
        else:
            bot.send_message(message.chat.id, 'Такой команды не существует',
                             reply_markup=keyboard())
        previous = message.text



@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Введите команду",
                     parse_mode='html',
                     reply_markup=keyboard())


def keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Погода')
    item2 = types.KeyboardButton('Калькулятор')
    markup.add(item1, item2)
    return markup

def keyboard_for_weather():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Екатеринбург')
    item2 = types.KeyboardButton('Москва')
    markup.add(item1, item2)
    return markup

# RUN
bot.polling(none_stop=True)
