import datetime
from datetime import *
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import asyncio

bot = Bot('5490678266:AAGHhzuse7TRRojzitQir_qZVp-t3u4VWok')
dp = Dispatcher(bot)


@dp.message_handler(commands=['бан', 'ban'], commands_prefix='!')
async def ban(message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    try:
        muteint = int(message.text.split()[1])
        mutetype = message.text.split()[2]
        comment = " ".join(message.text.split()[3:])
    except IndexError:
        await message.reply('Не хватает аргументов!\nПример:\n`!бан 1 ч причина`')
        return
    msg = await bot.send_poll(chat_id=message.chat.id,
                              question=f"Забанить {message.reply_to_message.from_user.first_name}?",
                              options=["Да", "Нет"])
    await asyncio.sleep(5)
    poll = await bot.stop_poll(chat_id=message.chat.id, message_id=msg.message_id)
    if int(poll['options'][0]["voter_count"]) > int(poll['options'][1]["voter_count"]) and \
            int(poll['options'][0]["voter_count"]) > 5:
        if mutetype == "ч" or mutetype == "часов" or mutetype == "час":
            dt = datetime.now() + timedelta(hours=muteint)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                           types.ChatPermissions(False), until_date=timestamp)
            await message.reply(
                f'| <b>Решение было принято:</b> {name1}\n| <b>Жертва:</b> <a href="tg://user?id='
                f'{message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n'
                f'| <b>Срок наказания:</b> {muteint} {mutetype} ⏰\n| <b>Причина:</b> {comment}',
                parse_mode='html')
        elif mutetype == "м" or mutetype == "минут" or mutetype == "минуты":
            dt = datetime.now() + timedelta(minutes=muteint)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                           types.ChatPermissions(False), until_date=timestamp)
            await message.reply(
                f'| <b>Решение было принято:</b> {name1}\n| <b>Жертва:</b> <a href="tg://user?id='
                f'{message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>'
                f'\n| <b>Срок наказания:</b> {muteint} {mutetype} ⏰\n| <b>Причина:</b> {comment}',
                parse_mode='html')
        elif mutetype == "д" or mutetype == "дней" or mutetype == "день":
            dt = datetime.now() + timedelta(days=muteint)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                           types.ChatPermissions(False), until_date=timestamp)
            await message.reply(
                f'| <b>Решение было принято:</b> {name1}\n| <b>Жертва:</b> <a href="tg://user?id='
                f'{message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n'
                f'⏰| <b>Срок наказания:</b> {muteint} {mutetype}\n| <b>Причина:</b> {comment}',
                parse_mode='html')
    else:
        await bot.send_message(message.chat.id, f'<a href="tg://user?id='
                                                f'{message.reply_to_message.from_user.id}">'
                                                f'{message.reply_to_message.from_user.first_name}</a>, '
                                                f'<b>живи... Пока что...</b>', parse_mode='html')


@dp.message_handler(commands=['разбан', 'unban'], commands_prefix='!', is_chat_admin=True)
async def unban(message: types.Message):
    await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await bot.send_message(message.chat.id, 'Done')


@dp.message_handler(content_types=['new_chat_members'])
async def del_new(message):
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=['any'])
async def delete_messages(message: types.Message):
    check = 0
    is_admin = await bot.get_chat_administrators(message.chat.id)
    wl = ['https://t.me/c/', 'github.com']
    for i in range(len(is_admin)):
        if int(message.from_user.id) == int(is_admin[i]['user']['id']):
            check = 1
    if message.content_type == 'photo' or message.content_type == 'video' or message.content_type == 'document':
        for i in wl:
            if i in message.caption:
                check = 1
    else:
        for i in wl:
            if i in message.text:
                check = 1
    if check == 0:
        if message.content_type == 'photo' or message.content_type == 'video' or message.content_type == 'document':
            for caption_entity in message.caption_entities:
                if caption_entity.type in ["url", "text_link", "hlink"]:
                    await message.delete()
        else:
            for entity in message.entities:
                if entity.type in ["url", "text_link", "hlink"]:
                    await message.delete()


print('run')
executor.start_polling(dp)
