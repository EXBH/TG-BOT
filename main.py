import telebot
import random

API_TOKEN = "7203577790:AAEo9jnbpDBMQ2aWBtUCXoo_5yRt6gODOXw"

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands=["start"])
def send_welcome(mеssage):
    bot.reply_to(mеssage,"добро пожаловать!")

@bot.message_handler(commands=["info"])
def info(mеssage):
    bot.reply_to(mеssage, "здравствуйте это я ваш любимый криптоинвестер и сегодня я снёс бедный детдом и построил на его месте своё 13 джакузи ")


@bot.message_handler(commands=['rad'])
def send_help(massege):
    try:
        random_imdex = random.randint(0,9)
        image_path = f"./img/image{random_imdex}.jpg"
        with open(image_path,'rb') as image_file:
            bot.send_photo(massege.chat.id,image_file)
    except Exception as e:
        bot.reply_to(massege, f"Произошла ошибка {e}")

@bot.message_handler()
def popa(mеssage):
    response ="<b>Простите я не знаю такой команды</b>."
    bot.reply_to(mеssage, response)

# запуск бота
bot.polling(none_stop=True)