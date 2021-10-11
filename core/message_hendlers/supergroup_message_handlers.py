from core import bot, telebot, OUR_GROUP


@bot.message_handler(content_types=['text'], chat_types=['supergroup'])
def handler_text(message):
    try:
        print(message)
        bot.send_message(message.json['reply_to_message']['forward_from']['id'], message.text)
    except KeyError:
        bot.send_message(OUR_GROUP, 'Зачинений аккаунт або самореплай')


@bot.message_handler(content_types=['document'], chat_types=['supergroup'])
def handler_text(message):
    try:
        print(message)
        bot.copy_message(message.json['reply_to_message']['forward_from']['id'], OUR_GROUP, message.id)
    except KeyError:
        bot.send_message(OUR_GROUP, 'Зачинений аккаунт або самореплай')
