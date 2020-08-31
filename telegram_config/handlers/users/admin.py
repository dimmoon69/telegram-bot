from aiogram import types
from telegram_config.filters import IsPrivate
from telegram_config.loader import dp

from telegram_config.data.config import admins


@dp.message_handler(IsPrivate(), text='secret', user_id=admins)
async def admin_chat_secret(message: types.Message):
    await message.answer('Это секретное сообщение, вызванное одним из администраторов'
                         'в личной переписке')