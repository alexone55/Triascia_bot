from core import bot, telebot, OUR_GROUP


@bot.callback_query_handler(func=lambda call: call.data == 'consultation')
def options_consult_query(call):
    bot.send_message(call.message.chat.id, f'Нижче ти можеш написати свое питання\n'
                                           f'Тобі обов\'язково буде надана відповідь')

    @bot.message_handler(content_types=['text'], chat_types=['private'])
    def handler_text(message):
        bot.forward_message(OUR_GROUP, message.chat.id, message.id)


@bot.callback_query_handler(func=lambda call: call.data == 'write')
def options_write_query(call):
    bot.send_message(call.message.chat.id, 'Відправляй ТЗ згідно зразку из правил')

    @bot.message_handler(content_types=['document'], chat_types=['private'])
    def handler_document(message):
        bot.forward_message(OUR_GROUP, message.chat.id, message.id)


@bot.callback_query_handler(func=lambda call: call.data == 'something_else')
def options_else_query(call):
    print("and its to")
