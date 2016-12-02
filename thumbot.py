import telebot

from keyboard import Keyboard


TOKEN = ''

bot = telebot.TeleBot(TOKEN)


@bot.message_handler()
def handle_all_messages(message):
    keyboard = Keyboard()
    message = bot.send_message(message.from_user.id, 'Promoção imperdível...',
                               reply_markup=keyboard.generate())


bot.polling()
