#- ZThon - DraGo - #

import asyncio
import base64
import contextlib


from telethon.errors.rpcerrorlist import ForbiddenError
from telethon.tl import functions, types
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name


from . import dragoiq

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _catutils
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "Services"

UNSPAM = gvarstatus("DRAGO_UNSPAM") or "ايقاف البلاغ"




async def spam_abuseinform_drago(event, sandy, inform_drago, sleeptimem, sleeptimet, DelaySpam=False):
    # sourcery no-metrics
    counter = int(inform_drago[0])
    if len(inform_drago) == 2:
        spam_message = str(inform_drago[1])
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message('@AbuseNotifications', spam_message) 
            await asyncio.sleep(4)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message('@AbuseNotifications', spam_message) 
            await asyncio.sleep(4)
    else:
        return
    if DelaySpam is not True: 
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**- البلاغات**\n"
            + f"**-   تم تنفيذ تكرار البلاغات \n- لـ الدعم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عدد البلاغات :** {counter} **مرات**\n**- وقت التكرار :** {sleeptimet} **ثانيـه**\n"
            + f"**- كليشـة البلاغات :**\n `{spam_message}`",
        )
            await event.client.send_message(event.chat_id, f"**- بلاغات_ الداخلية 🚸\n-  تم تنفيذ تكرار بلاغات بنجاح\n- لـ الدعم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عدد البلاغات :** {counter} **مرات\n- كليشـة البلاغات :**\n `{spam_message}`")



    elif BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
                "**- البلاغات**\n"
            + f"**-   تم تنفيذ تكرار البلاغات \n- لـ الدعم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عدد البلاغات :** {counter} **مرات**\n**- وقت التكرار :** {sleeptimet} **ثانيـه**\n"
            + f"**- كليشـة البلاغات :**\n `{spam_message}`",
        )
        await event.client.send_message(event.chat_id, f"**- بلاغات_ الداخلية 🚸\n-  تم تنفيذ تكرار بلاغات بنجاح\n- لـ الدعم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عدد البلاغات :** {counter} **مرات\n- كليشـة البلاغات :**\n `{spam_message}`")





@dragoiq.ar_cmd(pattern="بلاغ ([\s\S]*)")
async def spammer(event):
    sandy = await event.get_reply_message()
    inform_drago = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    try:
        counter = int(inform_drago[0])
    except Exception:
        return await edit_delete(
            event, "**- ارسـل الامـر بالشكـل التالي**\n\n`.بلاغ` **+ عدد التكرار + الرسالة او بالـرد ع رسالة**\n**- مثـال : .بلاغ 12 بالـرد ع كليشـة البـلاغ**"
        )
    if counter > 50:
        sleeptimet = 4
        sleeptimem = 1
    else:
        sleeptimet = 4
        sleeptimem = 0.3
    await edit_delete(event, f"**⌁︙جـارِ الابـلاغ الداخلـي . . . ⚠️ \n⌁︙لـ الدعم @AbuseNotifications\n⌁︙عـدد البلاغـات ** {inform_drago}", 5)
    addgvar("spamwork", True)
    await spam_abuseinform_drago(event, sandy, inform_drago, sleeptimem, sleeptimet)






@dragoiq.ar_cmd(pattern=f"{UNSPAM} ?(.*)",)
async def spammer(event):
    if gvarstatus("spamwork") is not None and gvarstatus("spamwork") == "true":
        delgvar("spamwork")
        return await edit_delete(event, "**- تم ايقـاف البلاغـات .. بنجـاح ✅**")
    return await edit_delete(event, "**- لايوجـد هنـاك بلاغـات لـ إيقافهـا ؟!**")





