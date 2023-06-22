from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="")
dp = Dispatcher(bot)
button1 = KeyboardButton('Bussolengo')
button2 = KeyboardButton('Castelnuovo')
button3 = KeyboardButton('Lazise')
button4 = KeyboardButton('Mozzecane')
button5 = KeyboardButton('Patrengo')
button6 = KeyboardButton('Pescantina')
button7 = KeyboardButton('Sommacampagna')
button8 = KeyboardButton('Sona')
button9 = KeyboardButton('Valeggio')
button10 = KeyboardButton('Vigasio')
button11 = KeyboardButton('Villafranca')

keyboard1 = ReplyKeyboardMarkup (resize_keyboard=True, one_time_keyboard=True).add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)

@dp.message_handler()
async def welcome (message: types.Message):
    await message.answer("Ciao, mi chiamo MonuVeronaBot! Ti aiuterò nella ricerca dei monumenti più interessanti dell\'ovest veronese! Scegli il comune tra l\'elenco: ", reply_markup=keyboard1)
    
executor.start_polling(dp)