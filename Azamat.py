import telebot

bot = telebot.TeleBot('1891179593:AAEbSzhgSbDZKYhtecatsWRpVgqQKmtd3iA')

#по команде meet нам возвращается ссылка
@bot.message_handler(commands=['meet'])
def open_website(message):
    bot.send_message(message.chat.id, "ГО! ГО! ГО!: <a href='https://meet.google.com/bxq-nsek-ept'>Митинг</a>", parse_mode='html')


#по команде start бот здоровается и выводит его имя и фамилию
@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакое направление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

bot.polling(none_stop=True)

