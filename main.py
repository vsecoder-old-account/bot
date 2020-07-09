from models.start import bot
from models.users import lalala
#обработка

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('assets/hi.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    lalala1(message)


@bot.message_handler(content_types=['text'])
def lalala1(message):
    lalala(message)


bot.polling(none_stop=True)