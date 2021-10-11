from core import bot, telebot


REFUSE_TEXT = f'На жаль, ми не можемо надати вам допомоги, сподіваємося на ваше розуміння'


@bot.callback_query_handler(func=lambda call: call.data == 'False')
def options_false_query(call):
    bot.send_message(call.message.chat.id, REFUSE_TEXT)


@bot.callback_query_handler(func=lambda call: call.data == 'True')
def options_true_query(call):
    img = open('./resources/pics/price.png', 'rb')
    buttons = telebot.types.InlineKeyboardMarkup(row_width=3)
    btn_1 = telebot.types.InlineKeyboardButton('Консультація', callback_data='consultation')
    btn_2 = telebot.types.InlineKeyboardButton('Написання роботи', callback_data='write')
    btn_3 = telebot.types.InlineKeyboardButton('Інше', callback_data='something_else')
    buttons.row(btn_1, btn_2, btn_3)
    bot.send_photo(call.message.chat.id, img, reply_markup=buttons)
    img.close()
