import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])

def send_welcome(message):
    bot.send_message(message.chat.id, "Ciao, mi chiamo MonuVeronaBot! Ti aiuterò nella ricerca dei monumenti più interessanti dell\'ovest veronese! Scegli il comune tra l\'elenco: ")

    
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Bussolengo", callback_data = "1"),
               InlineKeyboardButton("Lazise", callback_data = "2"))
    
    return markup


@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == "1":
        bot.send_message(call.message.chat.id, "Ciacia")
    elif call.data == "2":
        bot.answer_callback_query(call.id, "Oneone")
        
    
bot.polling()