from loader import dp
from aiogram import types

from aiogram.dispatcher.filters import Command

@dp.message_handler(commands='a')
async def answer(message: types.Message, command: Command.CommandObj):
    if message.chat.id != -884694436: return

    await dp.bot.send_message(command.args.split()[0], text=' '.join(command.args.split()[1:]))
    return