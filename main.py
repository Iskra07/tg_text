import telebot

TOKEN = '5956193209:AAH55_tv76AItp2r5tqpdDipuGNdRSxhiRc'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def greetings(message):
    reply = 'Hello i am data collection bot'
    bot.reply_to(message, reply)


is_taking_name = False
is_taking_surname = False
@bot.message_handler(content_types=['text'])
def message_handler(message):
    chat_id = message.chat.id
    global is_taking_name
    global is_taking_surname


    if is_taking_surname == True:
        surname = message.text
        print(surname)
        is_taking_surname = False

    if is_taking_name:
        user_name = message.text
        print(user_name)
        is_taking_name = False
        is_taking_surname = True
        bot.send_message(chat_id,'Input your surname: ')


    if message.text == 'save name':
        is_taking_name = True
        bot.send_message(chat_id, 'Input your name: ')




bot.infinity_polling()