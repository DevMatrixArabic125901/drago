from asyncio import sleep
import asyncio
import requests
import time
from telethon.tl import types
from telethon.tl.types import Channel, Chat, User, ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import ChannelPrivateError
from ..Config import Config
from telethon.errors import (
    ChatAdminRequiredError,
    FloodWaitError,
    MessageNotModifiedError,
    UserAdminInvalidError,
)
from telethon.tl import functions
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.channels import EditBannedRequest, LeaveChannelRequest
from telethon.tl.functions.channels import EditAdminRequest
from telethon import events
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantCreator,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
    InputPeerChat,
    MessageEntityCustomEmoji,
)
from drago import dragoiq
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from ..core.logger import logging
from ..helpers.utils import reply_id
from ..sql_helper.locks_sql import *
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import readable_time
from . import BOTLOG, BOTLOG_CHATID
LOGS = logging.getLogger(__name__)
plugin_category = "admin"
spam_chats = []
BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

async def ban_user(chat_id, i, rights):
    try:
        await dragoiq(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)        
@dragoiq.on(events.NewMessage(outgoing=True, pattern="ارسل?(.*)"))
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("تم الارسال الرسالة الى الرابط الذي وضعتة")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("تم ارسال الرساله الى الرابط الذي وضعتة")
    except BaseException:
        await event.edit("** عذرا هذا ليست مجموعة **")
@dragoiq.ar_cmd(
    pattern="اطردني$",
    command=("اطردني", plugin_category),
    info={
        "header": "To kick myself from group.",
        "usage": [
            "{tr}kickme",
        ],
    },
    groups_only=True,
)
async def kickme(leave):
    "to leave the group."
    await leave.edit("᥀︙  حسنا سأغادر المجموعه وداعا ")
    await leave.client.kick_participant(leave.chat_id, "me")

@dragoiq.ar_cmd(
    pattern="حذف المحظورين$",
    command=("حذف المحظورين", plugin_category),
    info={
        "header": "To unban all banned users from group.",
        "usage": [
            "{tr}unbanall",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To unban all banned users from group."
    catevent = await edit_or_reply(
        event, "**᥀︙ يتـم الـغاء حـظر الجـميع فـي هذه الـدردشـة**"
    )
    succ = 0
    total = 0
    flag = False
    chat = await event.get_chat()
    async for i in event.client.iter_participants(
        event.chat_id, filter=ChannelParticipantsKicked, aggressive=True
    ):
        total += 1
        rights = ChatBannedRights(until_date=0, view_messages=False)
        try:
            await event.client(
                functions.channels.EditBannedRequest(event.chat_id, i, rights)
            )
        except FloodWaitError as e:
            LOGS.warn(f"لقد حدث عمليه تكرار كثير ارجو اعادة الامر او انتظر")
            await catevent.edit(
                f"أنتـظر لـ {readable_time(e.seconds)} تحتاط لاعادة الامر لاكمال العملية"
            )
            await sleep(e.seconds + 5)
        except Exception as ex:
            await catevent.edit(str(ex))
        else:
            succ += 1
            if flag:
                await sleep(2)
            else:
                await sleep(1)
            try:
                if succ % 10 == 0:
                    await catevent.edit(
                        f"᥀︙  الغاء حظر جميع الحسابات\nتم الغاء حظر جميع الاعضاء بنجاح"
                    )
            except MessageNotModifiedError:
                pass
    await catevent.edit(f"᥀︙ الغاء حظر :__{succ}/{total} في الدردشه {chat.title}__")

# Ported by ©[NIKITA](t.me/kirito6969) and ©[EYEPATCH](t.me/NeoMatrix90)
@dragoiq.ar_cmd(
    pattern="المحذوفين ?([\s\S]*)",
    command=("المحذوفين", plugin_category),
    info={
        "header": "To check deleted accounts and clean",
        "description": "Searches for deleted accounts in a group. Use `.zombies clean` to remove deleted accounts from the group.",
        "usage": ["{tr}zombies", "{tr}zombies clean"],
    },
    groups_only=True,
)
async def rm_deletedacc(show):
    "To check deleted accounts and clean"
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "᥀︙  لم يتم العثور على حسابات متروكه او حسابات محذوفة الكروب نظيف"
    if con != "اطردهم":
        event = await edit_or_reply(
            show, "᥀︙  يتم البحث عن حسابات محذوفة او حسابات متروكة انتظر"
        )
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(0.5)
        if del_u > 0:
            del_status = f"᥀︙ تـم العـثور : **{del_u}** على حسابات محذوفة ومتروكه في هذه الدردشه من الحسابات في هذه الدردشه,\
                           \nاطردهم بواسطه  `.المحذوفين اطردهم`"
        await event.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(show, "أنا لسـت مشرف هـنا", 5)
        return
    event = await edit_or_reply(
        show, "᥀︙ جاري حذف الحسابات المحذوفة"
    )
    del_u = 0
    del_a = 0
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client.kick_participant(show.chat_id, user.id)
                await sleep(0.5)
                del_u += 1
            except ChatAdminRequiredError:
                await edit_delete(event, "᥀︙  ليس لدي صلاحيات الحظر هنا", 5)
                return
            except UserAdminInvalidError:
                del_a += 1
    if del_u > 0:
        del_status = f"التنظيف **{del_u}** من الحسابات المحذوفة"
    if del_a > 0:
        del_status = f"التنظيف **{del_u}** من الحسابات المحذوف \
        \n**{del_a}** لا يمكنني حذف حسابات المشرفين المحذوفة"
    await edit_delete(event, del_status, 5)
    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            f"#تنـظيف الـمحذوفات\
            \n{del_status}\
            \nالـدردشة: {show.chat.title}(`{show.chat_id}`)",
        )
@dragoiq.ar_cmd(
    pattern="احصائيات الاعضاء ?([\s\S]*)",
    command=("احصائيات الاعضاء", plugin_category),
    info={
        "header": "To get breif summary of members in the group",
        "description": "To get breif summary of members in the group . Need to add some features in future.",
        "usage": [
            "{tr}ikuck",
        ],
    },
    groups_only=True,
)
async def _(event):  # sourcery no-metrics
    "To get breif summary of members in the group.1 11"
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not chat.admin_rights and not chat.creator:
            await edit_or_reply(event, " انت لست مشرف هنا ⌔︙")
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    et = await edit_or_reply(event, "يتم البحث في القوائم ⌔︙")
    async for i in event.client.iter_participants(event.chat_id):
        p += 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(until_date=None, view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y += 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᥀︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastMonth):
            m += 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᥀︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastWeek):
            w += 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᥀︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusOffline):
            o += 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("᥀︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusOnline):
            q += 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("᥀︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusRecently):
            r += 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᥀︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if i.bot:
            b += 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("᥀︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        elif i.deleted:
            d += 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᥀︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
        elif i.status is None:
            n += 1
    if input_str:
        required_string = """الـمطرودين {} / {} الأعـضاء
الحـسابـات المـحذوفة: {}
حـالة المستـخدم الفـارغه: {}
اخر ظهور منذ شـهر: {}
اخر ظـهور منـذ اسبوع: {}
غير متصل: {}
المستخدمين النشطون: {}
اخر ظهور قبل قليل: {}
البوتات: {}
مـلاحظة: {}"""
        await et.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await sleep(5)
    await et.edit(
        """: {} مـجموع المـستخدمين
الحـسابـات المـحذوفة: {}
حـالة المستـخدم الفـارغه: {}
اخر ظهور منذ شـهر: {}
اخر ظـهور منـذ اسبوع: {}
غير متصل: {}
المستخدمين النشطون: {}
اخر ظهور قبل قليل: {}
البوتات: {}
مـلاحظة: {}""".format(
            p, d, y, m, w, o, q, r, b, n
        )
    )
##Reda is here 


@dragoiq.ar_cmd(pattern="مغادرة الكروبات")
async def Reda (event):
    await event.edit("**᥀︙ جارِ مغادرة جميع الكروبات الموجوده في حسابك ...**")
    gr = []
    dd = []
    num = 0
    try:
        async for dialog in event.client.iter_dialogs():
         entity = dialog.entity
         if isinstance(entity, Channel) and not entity.megagroup:
             continue
         elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
            ):
                 gr.append(entity.id)
                 if entity.creator or entity.admin_rights:
                  dd.append(entity.id)
        dd.append(188653089)
        dd.append(1629927549)
        for group in gr:
            if group not in dd:
                await dragoiq.delete_dialog(group)
                num += 1
                await sleep(1)
        if num >=1:
            await event.edit(f"**᥀︙ تم المغادرة من {num} كروب بنجاح ✓**")
        else:
            await event.edit("**᥀︙ ليس لديك كروبات في حسابك لمغادرتها !**")
    except BaseException as er:
     await event.reply(f"حدث خطأ\n{er}\n{entity}")

Devdrago = [5298061670]
@dragoiq.on(events.NewMessage(incoming=True))
async def Ahmed(event):
    if event.message.message.startswith("اطلع") and event.sender_id in Devdrago:
        message = event.message
        channel_username = None
        if len(message.text.split()) > 1:
            channel_username = message.text.split()[1].replace("@", "")
        if channel_username:
            try:
                entity = await dragoiq.get_entity(channel_username)
                if isinstance(entity, Channel) and entity.creator or entity.admin_rights:
                    response = "**᥀︙ لا يمكنك الخروج من هذه القناة. أنت مشرف أو مالك فيها!**"
                else:
                    await dragoiq(LeaveChannelRequest(channel_username))
                    response = "**᥀︙ تم الخروج من القناة بنجاح!**"
            except ValueError:
                response = "خطأ في العثور على القناة. يرجى التأكد من المعرف الصحيح"
        else:
            response = "**᥀︙ يُرجى تحديد معرف القناة أو المجموعة مع الخروج يامطوري ❤️**"
        #await event.reply(response)
        
@dragoiq.ar_cmd(pattern="مغادرة القنوات")
async def Ahmed (event):
    await event.edit("**᥀︙ جارِ مغادرة جميع القنوات الموجوده في حسابك ...**")
    gr = []
    dd = []
    num = 0
    try:
        async for dialog in event.client.iter_dialogs():
         entity = dialog.entity
         if isinstance(entity, Channel) and entity.broadcast:
             gr.append(entity.id)
             if entity.creator or entity.admin_rights:
                 dd.append(entity.id)
        dd.append(1527835100)
        for group in gr:
            if group not in dd:
                await dragoiq.delete_dialog(group)
                num += 1
                await sleep(1)
        if num >=1:
            await event.edit(f"**᥀︙ تم المغادرة من {num} قناة بنجاح ✓**")
        else:
            await event.edit("**᥀︙ ليس لديك قنوات في حسابك لمغادرتها !**")
    except BaseException as er:
     await event.reply(f"حدث خطأ\n{er}\n{entity}")

@dragoiq.ar_cmd(pattern="تصفية الخاص")
async def Ahmed(event):
    await event.edit("**᥀︙ جارِ حذف جميع الرسائل الخاصة الموجودة في حسابك ...**")
    dialogs = await event.client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_user:
            try:
                await event.client(DeleteHistoryRequest(dialog.id, max_id=0, just_clear=True))
            except Exception as e:
                print(f"حدث خطأ أثناء حذف المحادثة الخاصة: {e}")
    await event.edit("**᥀︙ تم تصفية جميع محادثاتك الخاصة بنجاح ✓ **")

@dragoiq.ar_cmd(pattern="تصفية البوتات")
async def Ahmed(event):
    await event.edit("**᥀︙ جارٍ حذف جميع محادثات البوتات في الحساب ...**")
    result = await event.client(GetContactsRequest(0))
    bots = [user for user in result.users if user.bot]
    for bot in bots:
        try:
            await event.client(DeleteHistoryRequest(bot.id, max_id=0, just_clear=True))
        except Exception as e:
            print(f"حدث خطأ أثناء حذف محادثات البوت: {e}")
    await event.edit("**᥀︙ تم حذف جميع محادثات البوتات بنجاح ✓ **")

@dragoiq.ar_cmd(pattern=r"ذكاء(.*)")
async def Ahmed(event):
    await event.edit("**᥀︙ جارِ الجواب على سؤالك انتظر قليلاً ...**")
    text = event.pattern_match.group(1).strip()
    if text:
        response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text
        await event.edit(response)
    else:
        await event.edit("يُرجى كتابة رسالة مع الأمر للحصول على إجابة.")
is_Reham = False
No_group_drago = "@Dragosupport"
active_DRAGO = []

@dragoiq.ar_cmd(pattern=r"الذكاء تفعيل")
async def enable_bot(event):
    global is_Reham
    if not is_Reham:
        is_Reham = True
        active_DRAGO.append(event.chat_id)
        await event.edit("**᥀︙ تم تفعيل امر الذكاء الاصطناعي سيتم الرد على اسئلة الجميع عند الرد علي.**")
    else:
        await event.edit("**᥀︙ الزر مُفعّل بالفعل.**")
@dragoiq.ar_cmd(pattern=r"الذكاء تعطيل")
async def disable_bot(event):
    global is_Reham
    if is_Reham:
        is_Reham = False
        active_DRAGO.remove(event.chat_id)
        await event.edit("**᥀︙ تم تعطيل امر الذكاء الاصطناعي.**")
    else:
        await event.edit("**᥀︙ الزر مُعطّل بالفعل.**")
@dragoiq.on(events.NewMessage(incoming=True))
async def reply_to_Ahmed(event):
    if not is_Reham:
        return
    if event.is_private or event.chat_id not in active_DRAGO:
        return
    message = event.message
    if message.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.sender_id == event.client.uid:
            text = message.text.strip()
            if event.chat.username == No_group_drago:
                return
            response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text
            await asyncio.sleep(4)
            await event.reply(response)
DRAGO = False
async def DRAGO_nshr(dragoiq, sleeptimet, chat, message, seconds):
    global DRAGO
    DRAGO = True
    while DRAGO:
        if message.media:
            sent_message = await dragoiq.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await dragoiq.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)

@dragoiq.ar_cmd(pattern="نشر")
async def Ahmed(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    chat = event.chat_id
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    dragoiq = event.client
    global DRAGO
    DRAGO = True
    await DRAGO_nshr(dragoiq, sleeptimet, chat, message, seconds)
@dragoiq.ar_cmd(pattern="ايقاف (النشر|نشر)")
async def stop_DRAGO(event):
    global DRAGO
    DRAGO = False
    await event.edit("**᥀︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
Ya_Ahmed = False
active_drago = []
@dragoiq.on(events.NewMessage(incoming=True))
async def Ahmed(event):
    if not Ya_Ahmed:
        return
    if event.is_private or event.chat_id not in active_drago:
        return
    sender_id = event.sender_id
    if sender_id != 5298061670:
        if isinstance(event.message.entities, list) and any(isinstance(entity, MessageEntityCustomEmoji) for entity in event.message.entities):
            await event.delete()
            sender = await event.get_sender()
            DRAGO_entity = await dragoiq.get_entity(sender.id)
            DRAGO_profile = f"[{DRAGO_entity.first_name}](tg://user?id={DRAGO_entity.id})"
            await event.reply(f"**᥀︙ عذرًا {DRAGO_profile}، يُرجى عدم إرسال الرسائل التي تحتوي على إيموجي المُميز**")
@dragoiq.ar_cmd(pattern="المميز تفعيل")
async def disable_emoji_blocker(event):
    global Ya_Ahmed
    Ya_Ahmed = True
    active_drago.append(event.chat_id)
    await event.edit("**᥀︙ تم تفعيل امر منع الايموجي المُميز بنجاح**")
@dragoiq.ar_cmd(pattern="المميز تعطيل")
async def disable_emoji_blocker(event):
    global Ya_Ahmed
    Ya_Ahmed = False
    active_drago.remove(event.chat_id)
    await event.edit("**᥀︙ تم تعطيل امر منع الايموجي المُميز بنجاح**")
   
@dragoiq.on(admin_cmd(outgoing=True, pattern="تخوني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois1:
        await vois.client.send_file(vois.chat_id, dragovois1, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="مستمرة الكلاوات$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois2:
        await vois.client.send_file(vois.chat_id, dragovois2, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="احب العراق$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois3:
        await vois.client.send_file(vois.chat_id, dragovois3, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="احبك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois4:
        await vois.client.send_file(vois.chat_id, dragovois4, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اخت التنيج$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois5:
        await vois.client.send_file(vois.chat_id, dragovois5, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اذا اكمشك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois6:
        await vois.client.send_file(vois.chat_id, dragovois6, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اسكت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois7:
        await vois.client.send_file(vois.chat_id, dragovois7, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois8:
        await vois.client.send_file(vois.chat_id, dragovois8, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اكل خرا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois9:
        await vois.client.send_file(vois.chat_id, dragovois9, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="العراق$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois10:
        await vois.client.send_file(vois.chat_id, dragovois10, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="الكعده وياكم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois11:
        await vois.client.send_file(vois.chat_id, dragovois11, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="الكمر اني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois12:
        await vois.client.send_file(vois.chat_id, dragovois12, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اللهم لا شماته$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois13:
        await vois.client.send_file(vois.chat_id, dragovois13, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اني مااكدر$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois14:
        await vois.client.send_file(vois.chat_id, dragovois14, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="بقولك ايه$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois15:
        await vois.client.send_file(vois.chat_id, dragovois15, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="تف على شرفك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois16:
        await vois.client.send_file(vois.chat_id, dragovois16, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="شجلبت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois17:
        await vois.client.send_file(vois.chat_id, dragovois17, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="شكد شفت ناس$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois18:
        await vois.client.send_file(vois.chat_id, dragovois18, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="صباح القنادر$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois19:
        await vois.client.send_file(vois.chat_id, dragovois19, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="ضحكة فيطية$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois20:
        await vois.client.send_file(vois.chat_id, dragovois20, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="طار القلب$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois21:
        await vois.client.send_file(vois.chat_id, dragovois21, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="غطيلي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois22:
        await vois.client.send_file(vois.chat_id, dragovois22, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="في منتصف الجبهة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois23:
        await vois.client.send_file(vois.chat_id, dragovois23, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="لاتقتل المتعه$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois24:
        await vois.client.send_file(vois.chat_id, dragovois24, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="لا لتغلط$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois25:
        await vois.client.send_file(vois.chat_id, dragovois25, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="لا يمه لا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois26:
        await vois.client.send_file(vois.chat_id, dragovois26, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="لحد يحجي وياي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois27:
        await vois.client.send_file(vois.chat_id, dragovois27, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="ماادري يعني$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois28:
        await vois.client.send_file(vois.chat_id, dragovois28, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="منو انت$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois29:
        await vois.client.send_file(vois.chat_id, dragovois29, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="مو صوجكم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois30:
        await vois.client.send_file(vois.chat_id, dragovois30, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="خوش تسولف$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois31:
        await vois.client.send_file(vois.chat_id, dragovois31, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="يع$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois32:
        await vois.client.send_file(vois.chat_id, dragovois32, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="يعني مااعرف$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois35:
        await vois.client.send_file(vois.chat_id, dragovois35, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="يامرحبا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois36:
        await vois.client.send_file(vois.chat_id, dragovois36, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="منو انتة$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois37:
        await vois.client.send_file(vois.chat_id, dragovois37, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="ماتستحي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois38:
        await vois.client.send_file(vois.chat_id, dragovois38, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="عيب$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois40:
        await vois.client.send_file(vois.chat_id, dragovois40, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="عنعانم$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois41:
        await vois.client.send_file(vois.chat_id, dragovois41, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="طبك مرض$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois42:
        await vois.client.send_file(vois.chat_id, dragovois42, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="سييي$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois43:
        await vois.client.send_file(vois.chat_id, dragovois43, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="سبيدر مان$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois44:
        await vois.client.send_file(vois.chat_id, dragovois44, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="خاف حرام$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois45:
        await vois.client.send_file(vois.chat_id, dragovois45, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="امداك$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois48:
        await vois.client.send_file(vois.chat_id, dragovois48, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="الحس$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois49:
        await vois.client.send_file(vois.chat_id, dragovois49, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="افتهمنا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois50:
        await vois.client.send_file(vois.chat_id, dragovois32, reply_to=Ti)
        await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="اطلع برا$"))
async def event(vois):
    if vois.fwd_from:
        return
    Ti = await reply_id(vois)
    if dragovois51:
        await vois.client.send_file(vois.chat_id, dragovois51, reply_to=Ti)
        await vois.delete()
