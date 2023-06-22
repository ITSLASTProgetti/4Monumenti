from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='')
dp = Dispatcher(bot)
button1 = InlineKeyboardButton(text = 'Bussolengo', callback_data = '1')
button2 = InlineKeyboardButton (text = 'Castelnuovo', callback_data = '2')
button3 = InlineKeyboardButton(text = 'Lazise', callback_data = '3')
button4 = InlineKeyboardButton (text = 'Mozzecane', callback_data = '4')
button5 = InlineKeyboardButton(text = 'Pastrengo', callback_data = '5')
button6 = InlineKeyboardButton (text = 'Pescantina', callback_data = '6')
button7 = InlineKeyboardButton(text = 'Sommacampagna', callback_data = '7')
button8 = InlineKeyboardButton (text = 'Sona', callback_data = '8')
button9 = InlineKeyboardButton(text = 'Valeggio', callback_data = '9')
button10 = InlineKeyboardButton (text = 'Vigasio', callback_data = '10')
button11 = InlineKeyboardButton (text = 'Villafranca', callback_data = '11')

keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)

@dp.message_handler(commands=['start', 'help'])
async def welcome (message: types.Message):
    await message.reply("Ciao, mi chiamo MonuVeronaBot! Ti aiuterò nella ricerca dei monumenti più interessanti dell\'ovest veronese! Scegli il comune tra l\'elenco: ")
    
@dp.callback_query_handler (text = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
async def random_value(call: types. CallbackQuery):
    if call.data == '1':
        await call.message.answer("Ciao bello")
    if call.data == '2':
        await call.message.answer ()
    if call.data == '3':
        await call.message.answer()
    if call.data == '4':
        await call.message.answer ()    
        
        await call.answer()
        
executor.start_polling (dp)