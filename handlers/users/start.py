from aiogram import types
from loader import dp
from keyboards.default import langsMarkup

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Выберите язык для бота', reply_markup=langsMarkup, parse_mode="MarkdownV2")