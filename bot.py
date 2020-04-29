import random
import telebot

from telebot import types

bot = telebot.TeleBot('1017480910:AAGfTZPrKwZXpw4fPPuAqmUXPEWJG6nZ5pE')
name = ''
sec_number = 0
count = 7

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "What is your name?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Write /start')

def get_name(message):
    global name
    name = message.text

    keyboard = types.InlineKeyboardMarkup() 
    key_1 = types.InlineKeyboardButton(text='1 - 100', callback_data='100')
    keyboard.add(key_1)  
    key_2 = types.InlineKeyboardButton(text='1 - 1000', callback_data='1000')
    keyboard.add(key_2)
    key_3 = types.InlineKeyboardButton(text='1 - 1000000', callback_data='1000000')
    keyboard.add(key_3)
    question = 'Choose your rank: ' 
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

def get_answer(message):
    global count
    try:
        Message = int(message.text)
        if Message == sec_number:
            bot.send_message(message.from_user.id, 'Yees, ' + name + ', you got it!!! ')
            bot.send_sticker(message.chat.id, 'CAADAgADTwsAAkKvaQABE3jwX_D6RZYWBA')
        elif Message > sec_number:
            count -= 1
            if count > 0:
                bot.send_message(message.from_user.id, 'Less :)' + '\nLeft ' + str(count) + ' tries :( \nInput your choosen number: ')
                bot.register_next_step_handler(message, get_answer)
            else:
                bot.send_message(message.from_user.id, 'Game over, ' + name + ". You're LOOSER")
                bot.send_sticker(message.chat.id, 'CAADAgADSAsAAkKvaQAB5dPHe9mTOQIWBA')
        else:
            count -= 1
            if count > 0:
                bot.send_message(message.from_user.id, 'More :)' + '\nLeft ' + str(count) + ' tries :( \nInput your choosen number: ')
                bot.register_next_step_handler(message, get_answer)
            else:
                bot.send_message(message.from_user.id, 'Game over, ' + name + ". You're LOOSER")
                bot.send_sticker(message.chat.id, 'CAADAgADSAsAAkKvaQAB5dPHe9mTOQIWBA')
    except Exception:
        bot.send_message(message.from_user.id, 'My dear, write numbers, please')
        bot.send_message(message.from_user.id, 'Input your choosen number: ')
        bot.register_next_step_handler(message, get_answer)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global sec_number
    if call.data == "100":
        max_number = 100
        sec_number = random.randint(1, max_number)
        bot.send_message(call.message.chat.id,'Input your choosen number, max 7 tries: ')
        bot.register_next_step_handler(call.message, get_answer)
    elif call.data == "1000":
        max_number = 1000
        sec_number = random.randint(1, max_number)
        bot.send_message(call.message.chat.id,'Input your choosen number, max 7 tries: ')
        bot.register_next_step_handler(call.message, get_answer)
    elif call.data == "1000000":
        max_number = 1000000
        sec_number = random.randint(1, max_number)
        bot.send_message(call.message.chat.id,'Input your choosen number, max 7 tries ')
        bot.register_next_step_handler(call.message, get_answer)

bot.polling(none_stop=True, interval=0)