from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.utils.exceptions import Throttled
from datetime import datetime, timedelta


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.GROUP))
@dp.message_handler(content_types=['any'])
async def any(message: types.Message):
    try:
        await dp.throttle('start', rate=2)
    except Throttled:
        print('antispam')
        await dp.bot.restrict_chat_member(message.chat.id, message.from_user.id, {"can_send_messages": False,
            "can_send_media_messages": False, "can_send_polls": False,
            "can_send_other_messages": False, "can_add_web_page_previews": False,
            "can_change_info": False, "can_invite_users": False, "can_pin_messages": False,
            "can_manage_topics": False}, (datetime.now() + timedelta(minutes=30)))
    else:
        pass
