from loader import dp
from aiogram import types
from keyboards.default import channelMarkup
from data.texts import *

@dp.callback_query_handler()
async def information(callback_query: types.CallbackQuery):
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, \
        text=TEXT_ru if callback_query.data == 'ru' else TEXT_kz, reply_markup=channelMarkup)