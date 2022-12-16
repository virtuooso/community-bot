from loader import dp
from aiogram import types

from data.config import admins

admin_only = lambda message: message.from_user.id not in admins

@dp.message_handler(admin_only)
async def handle_unwanted_users(message: types.Message):
    await dp.bot.delete_message(message.chat.id, message.message_id)