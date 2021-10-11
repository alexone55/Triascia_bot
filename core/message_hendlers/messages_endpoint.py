from core import bot, telebot, RULE_TEXT, GUARANTEE_TEXT


@bot.message_handler(commands=['rules'], chat_types='private')
def option_rules_handler(message):
    print(message)
    chat_id = message.chat.id
    bot.send_message(chat_id, RULE_TEXT, parse_mode='Markdown')


@bot.message_handler(commands=['guarantees'], chat_types='private')
def option_guarantees_handler(message):
    chat_id = message.chat.id

    buttons = telebot.types.InlineKeyboardMarkup(row_width=2)
    btn_1 = telebot.types.InlineKeyboardButton('Так', callback_data='True')
    btn_2 = telebot.types.InlineKeyboardButton('Ні', callback_data='False')
    buttons.row(btn_1, btn_2)
    bot.send_message(chat_id, GUARANTEE_TEXT, parse_mode='Markdown', reply_markup=buttons)