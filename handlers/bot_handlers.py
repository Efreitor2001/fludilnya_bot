from aiogram import types, Dispatcher
from create_bot import bot


def bad_words(message):
    check = False
    # bw = ['блядь', 'бляха-муха', 'бля', 'бля буду', 'блядство', 'блядун', 'бляди', 'блядское', 'блядская', 'блядские',
    #       'блядский', 'блядища', 'блядовать', 'выблядок', 'ебёныть', 'ёбнулся', 'ёб', 'ебать', 'ебанутый',
    #       'ебать-копать', 'ебать', 'ебаться', 'ёбырь', 'ебальник', 'ебало', 'ебло', 'ёбнуть', 'ебануть', 'ёбнутый',
    #       'выебнулся', 'наебнуться', 'выебнуться', 'долбоёб', 'заеблись', 'заебатый', 'настоебенить', 'настоебать',
    #       'ебаквакнуться', 'наебать', 'ебысь', 'еблысь', 'наёбка', 'подъебать', 'подъёб', 'подъёбка',
    #       'поебать', 'поебень', 'поеботина', 'коноебля', 'коноёбиться', 'ебля', 'уёбище', 'бомбоуёбище', 'уёбывать',
    #       'съёбывать', 'изъебнуться', 'изъёб', 'невъебенно', 'заебатый', 'заебательский', 'разъебай', 'разъёба',
    #       'поёбка', 'еблан', 'ебанат', 'туебень', 'ёбово', 'еботятина', 'ебливый', 'ебучий', 'злоебучий', 'косоёбиться',
    #       'шароёбиться', 'пиздец', 'пизда', 'спизжены', 'пизды', 'пизд', 'опиздол', 'пиздо', 'хуёвый', 'хуёво', 'хуета',
    #       'нехуй', 'хуйня', 'хуетень', 'хуёвина', 'хуётина', 'хули', 'хуячить', 'хуярить', 'хуярыжить', 'охуенный',
    #       'охуительный', 'охуевательный', 'охуенный', 'охуеть', 'ни хуя', 'нихуя', 'не хуя', 'нехуя', 'по хую', 'похую',
    #       'по хуй', 'похуй', 'хуяк', 'похуист', 'похуизм', 'на хуй', 'нахуй', 'хуила', 'хуебяка', 'хуйнуть', 'семихуй',
    #       'полухуй', 'хуемполбия', 'хуесос', 'хуй', 'уебывай', 'уёбывай', 'еб', 'еби', 'еба', 'ебу', 'заебу', 'ебстись',
    #       'заебало', 'заебала', 'заебали', 'заебать', 'трахать', 'дрочить', 'дрочила', 'задроченный', 'придрочиться',
    #       'подрочить', 'пидор', 'пидар', 'педик', 'педрила', 'педрильо', 'пидарас', 'пидораз', 'пидорас', 'пидарасить',
    #       'пидормот', 'пидорюга', 'пидорище', 'ебись', 'хуева', 'хуево', 'блядина', 'блять', 'охуенно', 'охуенный',
    #       'охуенная', 'охуенные', 'охуено', 'охуеная', 'охуеный', 'охуеные', 'пиздато', 'пиздатый', 'пиздатая',
    #       'пиздатые', 'хуеплет', 'хуев', 'хуево', 'заебал', 'пиздо', 'ахуенно']
    bw = '6ля, 6лядь, 6лять, b3ъeб, cock, cunt, e6aль, ebal, eblan, eбaл, eбaть, eбyч, eбать, eбёт, eблантий, fuck,' \
         ' fucker, fucking, xyёв, xyй, xyя, xуе,xуй, xую, zaeb, zaebal, zaebali, zaebat, архипиздрит, ахуел, ахуеть,' \
         ' бздение, бздеть, бздех, бздецы, бздит, бздицы, бздло, бзднуть, бздун, бздунья, бздюха, бздюшка, бздюшко,' \
         ' бля, блябу, блябуду, бляд, бляди, блядина, блядище, блядки, блядовать, блядство, блядун, блядуны,' \
         ' блядунья, блядь, блядюга, блять, вафел, вафлёр, взъебка, взьебка, взьебывать, въеб, въебался, въебенн,' \
         ' въебусь, въебывать, выблядок, выблядыш, выеб, выебать, выебен, выебнулся, выебон, выебываться, выпердеть,' \
         ' высраться, выссаться, вьебен, гавно, гавнюк, гавнючка, гамно, гандон, гнид, гнида, гниды, говенка, ' \
         'говенный, говешка, говназия, говнецо, говнище, говно, говноед, говнолинк, говночист, говнюк, говнюха, ' \
         'говнядина, говняк, говняный, говнять, гондон, доебываться, долбоеб, долбоёб, долбоящер, дрисня, дрист, ' \
         'дристануть, дристать, дристун, дристуха, дрочелло, дрочена, дрочила, дрочилка, дрочистый, дрочить, ' \
         'дрочка, дрочун, е6ал, е6ут, еб твою мать, ёб твою мать, ёбaн, ебaть, ебyч, ебал, ебало, ебальник,' \
         ' ебан, ебанамать, ебанат, ебаная, ёбаная, ебанический, ебанный, ебанныйврот, ебаное, ебануть,' \
         ' ебануться, ёбаную, ебаный, ебанько, ебарь, ебат, ёбат, ебатория, ебать, ебать-копать, ебаться,' \
         ' ебашить, ебёна, ебет, ебёт, ебец, ебик, ебин, ебись, ебическая, ебки, ебла, еблан, ебливый, еблище,' \
         ' ебло, еблыст, ебля, ёбн, ебнуть, ебнуться, ебня, ебош, ебаш, ебская, ебский, ебтвоюмать, ебун, ебут,' \
         ' ебуч, ебуче, ебучее, ебучий, ебучим, ебущ, ебырь, елда, елдак, елдачить, жопа, жопу, заговнять,' \
         ' задрачивать, задристать, задрота, зае6, заё6, заеб, заёб, заеба, заебал, заебанец, заебастая, заебастый,' \
         ' заебать, заебаться, заебашить, заебистое, заёбистое, заебистые, заёбистые, заебистый, заёбистый, ' \
         'заебись, заебошить, заебываться, залуп, залупа, залупаться, залупить, залупиться, замудохаться,' \
         ' запиздячить, засерать, засерун, засеря, засирать, засрун, захуячить, заябестая, злоеб, злоебучая, ' \
         'злоебучее, злоебучий, ибанамат, ибонех, изговнять, изговняться, изъебнуться, ипать, ипаться, ипаццо,' \
         ' Какдвапальцаобоссать, конча, курва, курвятник, лох, лошарa, лошара, лошары, лошок, лярва, малафья,' \
         ' манда, мандавошек, мандавошка, мандавошки, мандей, мандень, мандеть, мандища, мандой, манду, мандюк, ' \
         'минет, минетчик, минетчица, млять, мокрощелка, мокрощёлка, мразь, мудak, мудaк, мудаг, мудак, муде, ' \
         'мудель, мудеть, муди, мудил, мудила, мудистый, мудня, мудоеб, мудозвон, мудоклюй, на хер, на хуй,' \
         ' набздел, набздеть, наговнять, надристать, надрочить, наебать, наебет, наебнуть, наебнуться, наебывать,' \
         ' напиздел, напиздели, напиздело, напиздили, насрать, настопиздить, нахер, нахрен, нахуй, нахуйник, ' \
         'не ебет, не ебёт, невротебучий, невъебенно, нехира, нехрен, Нехуй, нехуйственно, ниибацо, ниипацца, ' \
         'ниипаццо, ниипет, никуя, нихера, нихуя, обдристаться, обосранец, обосрать, обосцать, обосцаться, обсирать,' \
         ' объебос, обьебать обьебос, однохуйственно, опездал, опизде, опизденивающе, остоебенить, остопиздеть, ' \
         'отмудохать, отпиздить, отпиздячить, отпороть, отъебись, охуевательский, охуевать, охуевающий, охуел, ' \
         'охуенно, охуеньчик, охуеть, охуительно, охуительный, охуяньчик, охуячивать, охуячить, очкун, падла, ' \
         'падонки, падонок, паскуда, педерас, педик, педрик, педрила, педрилло, педрило, педрилы, пездень, пездит, ' \
         'пездишь, пездо, пездят, пердануть, пердеж, пердение, пердеть, пердильник, перднуть, пёрднуть, пердун, ' \
         'пердунец, пердунина, пердунья, пердуха, пердь, переёбок, пернуть, пёрнуть, пи3д, пи3де, пи3ду, пиzдец,' \
         ' пидар, пидарaс, пидарас, пидарасы, пидары, пидор, пидорасы, пидорка, пидорок, пидоры, пидрас, пизда, ' \
         'пиздануть, пиздануться, пиздарваньчик, пиздато, пиздатое, пиздатый, пизденка, пизденыш, пиздёныш,' \
         ' пиздеть, пиздец, пиздит, пиздить, пиздиться, пиздишь, пиздища, пиздище, пиздобол, пиздоболы, ' \
         'пиздобратия, пиздоватая, пиздоватый, пиздолиз, пиздонутые, пиздорванец, пиздорванка, пиздострадатель,' \
         ' пизду, пиздуй, пиздун, пиздунья, пизды, пиздюга, пиздюк, пиздюлина, пиздюля, пиздят, пиздячить, ' \
         'писбшки, писька, писькострадатель, писюн, писюшка, по хуй, по хую, подговнять, подонки, подонок,' \
         ' подъебнуть, подъебнуться, поебать, поебень, поёбываает, поскуда, посрать, потаскуха, потаскушка,' \
         ' похер, похерил, похерила, похерили, похеру, похрен, похрену, похуй, похуист, похуистка, похую,' \
         ' придурок, приебаться, припиздень, припизднутый, припиздюлина, пробзделся, проблядь, проеб, проебанка,' \
         ' проебать, промандеть, промудеть, пропизделся, пропиздеть, пропиздячить, раздолбай, разхуячить, разъеб,' \
         ' разъеба, разъебай, разъебать, распиздай, распиздеться, распиздяй, распиздяйство, распроеть, сволота, ' \
         'сволочь, сговнять, секель, серун, серька, сестроеб, сикель, сила, сирать, сирывать, соси, спиздел, ' \
         'спиздеть, спиздил, спиздила, спиздили, спиздит, спиздить, срака, сраку, сраный, сранье, срать, срун, ' \
         'ссака, ссышь, стерва, страхопиздище, сука, суки, суходрочка, сучара, сучий, сучка, сучко, сучонок, ' \
         'сучье, сцание, сцать, сцука, сцуки, сцуконах, сцуль, сцыха, сцышь, съебаться, сыкун, трахае6, трахаеб, ' \
         'трахаёб, трахатель, ублюдок, уебать, уёбища, уебище, уёбище, уебищное, уёбищное, уебк, уебки, уёбки, ' \
         'уебок, уёбок, урюк, усраться, ушлепок, х_у_я_р_а, хyё, хyй, хyйня, хамло, хер, херня, херовато, херовина, ' \
         'херовый, хитровыебанный, хитрожопый, хуeм, хуе, хуё, хуевато, хуёвенький, хуевина, хуево, хуевый, хуёвый, ' \
         'хуек, хуёк, хуел, хуем, хуенч, хуеныш, хуенький, хуеплет, хуеплёт, хуепромышленник, хуерик, хуерыло, ' \
         'хуесос, хуесоска, хуета, хуетень, хуею, хуи, хуй, хуйком, хуйло, хуйня, хуйрик, хуище, хуля, хую, хуюл, ' \
         'хуя, хуяк, хуякать, хуякнуть, хуяра, хуясе, хуячить, целка, чмо, чмошник, чмырь, шалава, шалавой, ' \
         'шараёбиться, шлюха, шлюхой, шлюшка, ябывает, еб'.replace(' ', '').split(',')
    for i in bw:
        if i in message.text.lower().replace('ё', 'е').replace('a', 'а').replace('y', 'у').replace('e', 'е') \
                .replace('x', 'х').replace('c', 'с').replace('p', 'р').replace('k', 'к').replace('b', 'б')\
                .replace('z', 'з'):
            check = True
            return check

    return check


# @dp.message_handler(content_types=['new_chat_members'])
async def del_new(message):
    await bot.delete_message(message.chat.id, message.message_id)


# @dp.message_handler(content_types=['any'])
async def delete_messages(message: types.Message):
    if bad_words(message) is True:
        await message.reply(f'<b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>, '
                            f'у нас не матерятся!</b>', parse_mode='html')
        await message.delete()
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEFjwABYvjHWC8yVvt-gQcTL8wytAVmRnMAAjosAAL8eDlLFcEUfmcSuwkpBA')
    check = 0
    is_admin = await bot.get_chat_administrators(message.chat.id)
    wl = ['https://t.me/c/', 'github.com']
    for i in range(len(is_admin)):
        if int(message.from_user.id) == int(is_admin[i]['user']['id']):
            check = 0
    if message.content_type == 'photo' or message.content_type == 'video' or message.content_type == 'document' or \
            message.content_type == 'audio' or message.content_type == 'album':
        for i in wl:
            if i in message.caption:
                check = 1
    else:
        for i in wl:
            if i in message.text:
                check = 1
    if check == 0:
        count = 0
        if message.content_type == 'photo' or message.content_type == 'video' or message.content_type == 'document' or \
                message.content_type == 'audio' or message.content_type == 'album':
            for caption_entity in message.caption_entities:
                if caption_entity.type in ["url", "text_link", "hlink"] and count == 0:
                    for i in range(len(is_admin)):
                        if not is_admin[i]['user']['is_bot'] and int(
                                is_admin[i]['user']['id']) != 1387606641:
                            try:
                                await bot.send_message(is_admin[i]['user']['id'],
                                                       f'<b>Сообщение: </b>{message.caption}\n\n'
                                                       f'<b>Отправитель: </b><a href="tg://user?id='
                                                       f'{message.from_user.id}">'
                                                       f'{message.from_user.full_name}</a>'
                                                       f'\n\n<b>Ссылка на сообщение: </b>{message.url}',
                                                       parse_mode="html")
                                count += 1
                            except:
                                i += 1
        else:
            for entity in message.entities:
                if entity.type in ["url", "text_link", "hlink"] and count == 0:
                    for i in range(len(is_admin)):
                        if not is_admin[i]['user']['is_bot'] and int(is_admin[i]['user']['id']) != 1387606641:
                            try:
                                await bot.send_message(is_admin[i]['user']['id'],
                                                       f'<b>Сообщение: </b>{message.text}\n\n'
                                                       f'<b>Отправитель: </b><a href="tg://user?id='
                                                       f'{message.from_user.id}">'
                                                       f'{message.from_user.full_name}</a>'
                                                       f'\n\n<b>Ссылка на сообщение: </b>{message.url}',
                                                       parse_mode="html")
                                count += 1
                            except:
                                i += 1
    ck1 = 0
    ck2 = 0
    check1 = ['gitignore', 'git ignore', 'гитигнор', 'гит игнор']
    check2 = ['пришлите', 'скиньте', 'дайте', 'скинь']
    s = message.text.lower()
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
