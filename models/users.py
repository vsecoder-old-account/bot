import telebot
import random
from models.start import bot
from telebot import types
#сообщения

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '/start':
            sti = open('assets/hi.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Обо мне")
            item2 = types.KeyboardButton("Каналы")
            item3 = types.KeyboardButton("Купить сайт")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id,
                             "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы рассказать о своём создателе — <i>Всеволоде html</i>.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
        elif message.text == 'Каналы':
            bot.send_message(message.chat.id, "Мой канал на Дзен: https://zen.yandex.ru/id/5e7c78ee99d560276a9df6e4\nМой телеграм канал: https://t.me/vsevolodhtmlru\nМои боты: @htmlbankBot @testingZenBot")
        elif message.text == 'Купить сайт':
            bot.send_message(message.chat.id, "Напишите какой вам нужен сайт мне на почту: vsevolodhtml@yandex.ru")
        elif message.text == 'Обо мне':
            sti = open('assets/hi1.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id,
                             '<b>Опыт работы - мои проекты:</b>'
                             '\n<a href="https://vsevolodhtml.ru/cmd">Терминал</a>'
                             '\n<a href="https://kreepmeister.github.io">Змейка</a>'
                             '\n<a href="https://zen.yandex.ru/id/5e7c78ee99d560276a9df6e4">Канал на Дзен</a>'
                             '\n<a href="https://2dplatform.github.io/">Платформер</a>'
                             '\n<a href="https://vsevolodhtml.ru">Блог</a>'
                             '\n<a href="https://vsevolodhtml.ru/public/chat">Чат</a>'
                             '\n<a href="https://vsevolodhtml.ru/public/redactor">Редактор html</a>'
                             '\n<b>Образование по книгам: </b>\nJava Script\nJava Script и HTML'
                             '\nСовременный Веб-дизайн\nНовая большая книга CSS\nPHP и MySQL'
                             '\nNode и Express\n<a href=\'https://vsevolodhtml.ru/resume/\'><b>###Больше обо мне тут###</b></a>',
                             parse_mode='html')
        elif message.text == '/help':
            bot.send_message(message.chat.id, "Всё очень просто, есть три команды:\n\"Купить сайт\"\n\"Обо мне\"\n\"Каналы\"")
        elif message.text == '/me':
            #данные пользователя
            name = message.from_user.first_name
            name1 = message.from_user.last_name
            url = message.from_user.username
            iduser = message.from_user.id
            #/данные пользователя
            bot.send_message(message.chat.id, "Имя: " + str(name) + " " + str(name1) + "\nСсылка: @" + str(url) + "\nID: " + str (iduser))
        elif message.text == '/vsevolodtop':
            sti = open('assets/hi2.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, "Спасибо, секретные команды:\nПароль\n/me\n/vsevolodtop\nВ скоре список увеличится!!!")
        elif message.text == 'Пароль':
            chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#VsevlodHtml#'
            number = int(1)
            length = int(8)
            for n in range(number):
                password = ''
                for i in range(length):
                    password += random.choice(chars)
            bot.send_message(message.chat.id, 'Ваш пароль: ' + str(password))
        else:
            msg = message.text
            bot.send_message(message.chat.id, 'Я не знаю что ответить вам на \"' + str(msg) + "\", /start")