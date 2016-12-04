import telebot
from thumbot import Thumbot


TOKEN = 'YOUR BOT TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler()
def handle_all_messages(message):
    message = bot.send_message(message.chat.id, 'Awesome message...',
                               reply_markup=Thumbot.empty_keyboard())


@bot.callback_query_handler(lambda q: q.data == 'thumb_up')
def thumb_up(callback):
    thumbot = Thumbot(callback.message)
    if thumbot.up(callback.from_user.id):
        bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=thumbot.keyboard())


@bot.callback_query_handler(lambda q: q.data == 'thumb_down')
def thumb_down(callback):
    thumbot = Thumbot(callback.message)
    if thumbot.down(callback.from_user.id):
        bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            reply_markup=thumbot.keyboard())


if __name__ == '__main__':
    bot.polling()
