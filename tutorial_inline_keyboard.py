from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='6255269129:AAFmX03HehvmbA2DzJ6u9DD2mLrVWB2XJ6Q')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="Bussolengo")
button2 = InlineKeyboardButton(text="Castelnuovo")
button3 = InlineKeyboardButton(text="Lazise")
button4 = InlineKeyboardButton(text="Mozzecane")
button5 = InlineKeyboardButton(text="Pastrengo")
button6 = InlineKeyboardButton(text="Pescantina")
button7 = InlineKeyboardButton(text="Sommacampagna")
button8 = InlineKeyboardButton(text="Sona")
button9 = InlineKeyboardButton(text="Valeggio")
button10 = InlineKeyboardButton(text="Vigasio")
button11= InlineKeyboardButton(text="Villafranca")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("👋 Hello!", "💋 Youtube")


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Ciao, mi chiamo MonuVeronaBot! Ti aiuterò nella ricerca dei monumenti più interessanti dell\'ovest veronese! Scegli il comune tra l\'elenco: ", reply_markup=keyboard1)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '👋 Hello!':
        await message.reply("Hi! How are you?")
    elif message.text == '💋 Youtube':
        await message.reply("https://youtube.com/gunthersuper")
    else:
        await message.reply(f"Your message is: {message.text}")


executor.start_polling(dp)