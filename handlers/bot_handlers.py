from aiogram import types, Dispatcher
from create_bot import bot


# @dp.message_handler(content_types=['new_chat_members'])
async def del_new(message):
    await bot.delete_message(message.chat.id, message.message_id)


# @dp.message_handler(content_types=['any'])
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


async def gitignore(message: types.Message):
    ck1 = 0
    ck2 = 0
    check1 = ['gitignore', 'git ignore', 'гитигнор', 'гит игнор']
    check2 = ['пришлите', 'скиньте', 'дайте', 'скинь']
    s = message.text
    s = s.lower()
    print(s)
    for i in check1:
        if i in s:
            ck1 = 1
    for j in check2:
        if j in s:
            ck2 = 1
    if ck1 == 1 and ck2 == 1:
        await message.reply(f'Лови https://t.me/c/1745662062/9222')


def register_handlers_bot_handlers(dp: Dispatcher):
    dp.register_message_handler(del_new, content_types=['new_chat_members'])
    dp.register_message_handler(delete_messages, content_types=['any'])
    dp.register_message_handler(gitignore, content_types=['text'])
