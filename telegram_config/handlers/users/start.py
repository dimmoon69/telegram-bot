import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from telegram_config.filters import IsPrivate

from telegram_config.loader import dp


@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d", re.UNICODE)), IsPrivate())
async def bot_start_deeplink(message: types.Message):
    deep_link_aegs = message.get_args()
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке.\n'
                         f'В вашей команде есть диплинк\n'
                         f'Вы передали аргумент {deep_link_aegs}.\n')


@dp.message_handler(CommandStart(deep_link=None), IsPrivate())
async def bot_start(message: types.Message):
    bot_user = await dp.bot.get_me()
    deep_link = f'http://t.me/{bot_user.username}?start=123'
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке.\n'
                         f'В вашей команде нет диплинка\n'
                         f'Ваша диплинк ссылка - {deep_link}')
