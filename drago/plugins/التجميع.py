import asyncio
import time
from drago import dragoiq
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.events import NewMessage
import requests
from telethon.tl.functions.users import GetFullUserRequest
from ..Config import Config
import re
from telethon import events
c = requests.session()
bot_username = '@EEObot'
bot_username2 = '@MARKTEBOT'
bot_username3 = '@qweqwe1919bot'
bot_username4 = '@xnsex21bot'
bot_username5 = '@DamKombot'
drago = ['yes']
Consoledragon = Config.T7KM
its_Reham = False
its_ahmed = False
its_mohammed = False
its_dragon = False
@dragoiq.on(events.NewMessage(incoming=True))
async def ahmed(event):
    if event.message.message.startswith("تجميع المليار") and str(event.sender_id) in Consoledragon:
        await event.reply("**⌁︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await dragoiq.get_entity(bot_username)
        await dragoiq.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await dragoiq.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await dragoiq.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await dragoiq(GetHistoryRequest(peer=channel_entity, limit=1,
                                                offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await dragoiq.send_message(event.chat_id, f"تم الانتهاء من التجميع")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await dragoiq(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await dragoiq(ImportChatInviteRequest(bott))
                msg2 = await dragoiq.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await dragoiq.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await dragoiq.send_message(event.chat_id, "تم الانتهاء من التجميع")
@dragoiq.on(events.NewMessage(incoming=True))
async def ahmed(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in Consoledragon:
        await dragoiq.send_message(bot_username, "/start")
        await event.reply("** ⌁︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")
        
@dragoiq.on(events.NewMessage(incoming=True))
async def ahmed(event):
    if event.message.message.startswith("تجميع العقاب") and str(event.sender_id) in Consoledragon:
        await event.reply("**⌁︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await dragoiq.get_entity(bot_username2)
        await dragoiq.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(3)
        msg0 = await dragoiq.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await dragoiq.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(3)
            list = await dragoiq(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await dragoiq.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await dragoiq(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await dragoiq(ImportChatInviteRequest(bott))
                msg2 = await dragoiq.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await dragoiq.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await dragoiq.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await dragoiq.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@dragoiq.on(events.NewMessage(incoming=True))
async def ahmed(event):
    if event.message.message.startswith("تجميع المليون") and str(event.sender_id) in Consoledragon:
        await event.reply("**⌁︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await dragoiq.get_entity(bot_username3)
        await dragoiq.send_message('@qweqwe1919bot', '/start')
        await asyncio.sleep(2)
        msg0 = await dragoiq.get_messages('@qweqwe1919bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await dragoiq.get_messages('@qweqwe1919bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(2)

            list = await dragoiq(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await dragoiq.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await dragoiq(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await dragoiq(ImportChatInviteRequest(bott))
                msg2 = await dragoiq.get_messages('@qweqwe1919bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await dragoiq.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await dragoiq.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await dragoiq.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

@dragoiq.on(admin_cmd(pattern="(تجميع المليار|تجميع مليار)"))
async def _(event):
    await event.edit("**⌁︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await dragoiq.get_entity(bot_username)
    await dragoiq.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await dragoiq.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await dragoiq.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await dragoiq(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await dragoiq.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await dragoiq(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await dragoiq(ImportChatInviteRequest(bott))
            msg2 = await dragoiq.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await dragoiq.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await dragoiq.send_message(event.chat_id, "تم الانتهاء من التجميع")
        
@dragoiq.on(admin_cmd(pattern="(ايقاف التجميع|ايقاف تجميع)"))
async def cancel_collection(event):
    await dragoiq.send_message('@EEObot', '/start')
    await event.edit("** ⌁︙ تم الغاء التجميع من بوت المليار **")

@dragoiq.on(admin_cmd(pattern="(تجميع العقاب|تجميع عقاب)"))
async def _(event):
    if drago[0] == "yes":
        await event.edit("**⌁︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await dragoiq.get_entity(bot_username2)
        await dragoiq.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(3)
        msg0 = await dragoiq.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await dragoiq.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if drago[0] == 'no':
                break
            await asyncio.sleep(3)

            list = await dragoiq(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await dragoiq.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await dragoiq(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await dragoiq(ImportChatInviteRequest(bott))
                msg2 = await dragoiq.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await dragoiq.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await dragoiq.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await dragoiq.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@dragoiq.on(admin_cmd(pattern="(تجميع المليون|تجميع مليون)"))
async def _(event):
    if drago[0] == "yes":
        await event.edit("**⌁︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await dragoiq.get_entity(bot_username3)
        await dragoiq.send_message('@qweqwe1919bot', '/start')
        await asyncio.sleep(2)
        msg0 = await dragoiq.get_messages('@qweqwe1919bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await dragoiq.get_messages('@qweqwe1919bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if drago[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await dragoiq(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await dragoiq.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await dragoiq(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await dragoiq(ImportChatInviteRequest(bott))
                msg2 = await dragoiq.get_messages('@qweqwe1919bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await dragoiq.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await dragoiq.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await dragoiq.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@dragoiq.on(admin_cmd(pattern="(تجميع العرب|تجميع عرب)"))
async def _(event):
    await event.edit("**⌁︙سيتم تجميع النقاط من بوت العرب , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await dragoiq.get_entity(bot_username4)
    await dragoiq.send_message(bot_username4, '/start')
    await asyncio.sleep(4)
    msg0 = await dragoiq.get_messages(bot_username4, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await dragoiq.get_messages(bot_username4, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await dragoiq(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await dragoiq.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await dragoiq(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await dragoiq(ImportChatInviteRequest(bott))
            msg2 = await dragoiq.get_messages(bot_username4, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await dragoiq.get_messages(bot_username4, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await dragoiq.send_message(event.chat_id, "تم الانتهاء من التجميع")
@dragoiq.on(admin_cmd(pattern="تجميع دعمكم"))
async def _(event):
    await event.edit("**⌁︙سيتم تجميع النقاط من بوت دعمكم , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await dragoiq.get_entity(bot_username5)
    await dragoiq.send_message('@DamKombot', '/start')
    await asyncio.sleep(4)
    msg0 = await dragoiq.get_messages(bot_username5, limit=1)
    await msg0[0].click(1)
    await asyncio.sleep(4)
    msg1 = await dragoiq.get_messages(bot_username5, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await dragoiq(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
            await dragoiq.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        msg_text = msgs.message  # الكود تمت كتابتهُ من قبل سورس دراكو 
        if "اشترك فالقناة @" in msg_text:
            drago_channel = msg_text.split('@')[1].split()[0]
            try:
                entity = await dragoiq.get_entity(drago_channel)
                if entity:
                    await dragoiq(JoinChannelRequest(entity.id))
                    await asyncio.sleep(4)
                    msg2 = await dragoiq.get_messages(bot_username5, limit=1)
                    await msg2[0].click(text='اشتركت ✅')
                    chs += 1
                    await event.edit(f"تم الانظمام الى القناة رقم {chs}")
            except:
                await dragoiq.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break

    await dragoiq.send_message(event.chat_id, "تم الانتهاء من التجميع")

@dragoiq.ar_cmd(pattern="راتب وعد(?:\s|$)([\s\S]*)")
async def ahmed(event):
    global its_ahmed
    await event.delete()
    if not its_ahmed:
        its_ahmed = True
        if event.is_group:
            await send_reham(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

async def send_reham(event):
    await event.respond('راتب')
    await asyncio.sleep(660)
    global its_ahmed
    if its_ahmed:
        await send_reham(event)  
@dragoiq.ar_cmd(pattern="ايقاف راتب وعد(?:\s|$)([\s\S]*)")
async def ahmed(event):
    global its_ahmed
    its_ahmed = False
    await event.edit("**تم تعطيل راتب وعد بنجاح ✅**")
@dragoiq.ar_cmd(pattern="بخشيش وعد(?:\s|$)([\s\S]*)")
async def ahmed(event):
    global its_dragon
    await event.delete()
    if not its_dragon:
        its_dragon = True
        if event.is_group:
            await send_drago(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
async def send_drago(event):
    await event.respond('بخشيش')
    await asyncio.sleep(660)
    global its_dragon
    if its_dragon:
        await send_drago(event)  
@dragoiq.ar_cmd(pattern="ايقاف بخشيش وعد(?:\s|$)([\s\S]*)")
async def ahmed(event):
    global its_dragon
    its_dragon = False
    await event.edit("**⌁︙ تم تعطيل بخشيش وعد بنجاح ✓ **")
@dragoiq.ar_cmd(pattern="سرقة وعد(?:\s|$)([\s\S]*)")
async def ahmed(event):
    global its_mohammed
    await event.delete()
    if not its_mohammed:
        its_mohammed = True
        if event.is_group:
            message = event.pattern_match.group(1).strip()
            if message:
                await send_message(event, message)
            else:
                await event.edit("**يرجى كتابة ايدي الشخص مع الامر!**")

async def send_message(event, message):
    await event.respond(f"زرف {message}")
    await asyncio.sleep(660)
    global its_mohammed
    if its_mohammed:
        await send_message(event, message)

@dragoiq.ar_cmd(pattern="ايقاف سرقة وعد(?:\s|$)([\s\S]*)")
async def Mohammed(event):
    global its_mohammed
    its_mohammed = False
    await event.edit("** ⌁︙ تم ايقاف السرقة بنجاح ✓ **")
client = dragoiq

@dragoiq.ar_cmd(pattern="استثمار وعد")
async def w3d_dragon(event):
    await event.delete()
    global its_Reham
    its_Reham = True
    while its_Reham:
        if event.is_group:
            await event.client.send_message(event.chat_id, "فلوسي")
            await asyncio.sleep(3)
            drago = await event.client.get_messages(event.chat_id, limit=1)
            drago = drago[0].message
            drago = ("".join(drago.split(maxsplit=2)[2:])).split(" ", 2)
            dragoiq = drago[0]
            if dragoiq.isdigit() and int(dragoiq) > 500000000:
                await event.client.send_message(event.chat_id,f"استثمار {dragoiq}")
                await asyncio.sleep(5)
                dragon = await event.client.get_messages(event.chat_id, limit=1)
                await dragon[0].click(text="اي ✅")
            else:
                await event.client.send_message(event.chat_id, f"استثمار {dragoiq}")
            await asyncio.sleep(1210)
        
        else:
            await event.edit("** ⌁︙ امر الاستثمار يمكنك استعماله في المجموعات فقط 🖤**")
@dragoiq.ar_cmd(pattern="ايقاف استثمار وعد")
async def disable_w3d(event):
    global its_Reham
    its_Reham = False
    await event.edit("**تم تعطيل عملية الاستثمار وعد.**")
