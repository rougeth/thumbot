import telebot
from thumbot import Thumbot


TOKEN = 'YOUR BOT TOKEN'


bot = telebot.TeleBot(TOKEN)
thumbot = Thumbot()


@bot.message_handler()
def handle_all_messages(message):
    thumbot.check(message)

    message = bot.send_message(message.from_user.id, 'Awesome message...',
                               reply_markup=thumbot.keyboard())


bot.polling()
