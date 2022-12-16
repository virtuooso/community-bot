from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import Throttled

from loader import dp

@dp.message_handler(commands='fb')
async def feedback(message: types.Message, command: Command.CommandObj):
    try:
        await dp.throttle('fb', rate=30)
    except Throttled:
        await message.reply('Подождите 30 секунд. Нельзя часто использовать эту команду.')
    else:
        if command.args == None:
            await message.answer('Пожалуйста, не оставляйте пустым вопрос!')
            return
        await message.reply('Ваше обращение успешно доставлено администраторам!')

        user = '\\@' + (message.from_user.username).replace('_', '\\_')
        await dp.bot.send_message(-884694436, text=f'''{command.args}
Id:```{message.chat.id}```Nickname: {user}''', parse_mode="MarkdownV2")

