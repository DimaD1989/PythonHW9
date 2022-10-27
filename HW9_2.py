import telebot

bot = telebot.Telebot ('5503832266:AAHVuUlj6vOR8YbrgEsCrLoceCMeg9BJ2KE')

value = ' '
old_value = ' '

keyboard = telebot.types.InlineKeybeardMarkup()
keyboard.row(telebot.types.InlineKeybeardButton(' ', callback='no'),
            telebot.types.InlineKeybeardButton('C', callback='C'),
            telebot.types.InlineKeybeardButton('<=', callback='<='),
            telebot.types.InlineKeybeardButton('/', callback='/'))

keyboard.row(telebot.types.InlineKeybeardButton('7', callback='7'),
            telebot.types.InlineKeybeardButton('8', callback='8'),
            telebot.types.InlineKeybeardButton('9', callback='9'),
             telebot.types.InlineKeybeardButton('*', callback='*'))

keyboard.row(telebot.types.InlineKeybeardButton('4', callback='4'),
            telebot.types.InlineKeybeardButton('5', callback='5'),
            telebot.types.InlineKeybeardButton('6', callback='6'),
             telebot.types.InlineKeybeardButton('-', callback='-'))

keyboard.row(telebot.types.InlineKeybeardButton('1', callback='1'),
            telebot.types.InlineKeybeardButton('2', callback='2'),
            telebot.types.InlineKeybeardButton('3', callback='3'),
            telebot.types.InlineKeybeardButton('+', callback='+'))

keyboard.row(telebot.types.InlineKeybeardButton(' ', callback='no'),
            telebot.types.InlineKeybeardButton('0', callback='0'),
            telebot.types.InlineKeybeardButton(',', callback=','),
            telebot.types.InlineKeybeardButton('=', callback='='))


@bot.massage_handler(commmands=['stars'], ['calculater'])
def getMessage(message):
    global value
    if value == ' ':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: true)
def callback_func(query)
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        value = ' '
    elif data == '<=':
        if value != ' ':
            value = value [:len(value)-1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка!'
    else += data

    if ( value != old_value and value != ' ') or ('0' != old_value and value == ' ') :
        if value == ' ':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyborad)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value,
                                  reply_markup=keyborad)
            old_value = value

    if value == 'Ошибка!': value = ' '


bot.polling(none_stop=False, interval=0)
