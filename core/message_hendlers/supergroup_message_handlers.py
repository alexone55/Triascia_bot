from core import bot, telebot, OUR_GROUP


@bot.message_handler(content_types=['text'], chat_types=['supergroup'])
def handler_text(message):
    print(message.json['reply_to_message']['forward_from']['id'])
    bot.send_message(message.json['reply_to_message']['forward_from']['id'], message.text)


@bot.message_handler(content_types=['document'], chat_types=['supergroup'])
def handler_text(message):
    print(message)
    bot.copy_message(message.json['reply_to_message']['forward_from']['id'], OUR_GROUP, message.id)
