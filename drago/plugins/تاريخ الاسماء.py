import asyncio


from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock


from . import dragoiq


from ..core.managers import edit_delete, edit_or_reply
from ..helpers import get_user_from_event, sanga_seperator
from ..helpers.utils import _format


plugin_category = "العروض"




@dragoiq.ar_cmd(
    pattern="كشف(المعرف)?(?:\s|$)([\s\S]*)",
    command=("الاسماء", plugin_category),
    info={
        "header": "To get name history of the user.",
        "flags": {
            "u": "That is sgu to get username history.",
        },
        "usage": [
            "{tr}كشف <username/userid/reply>",
            "{tr}كشف المعرف <username/userid/reply>",
        ],
        "examples": "{tr}sg @missrose_bot",
    },
)

async def _(event):  # sourcery no-metrics
    "To get name/username history."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "**- بالـرد ع الشخص او باضافة معـرف/ايـدي الشخـص للامـر**",
        )
    user, rank = await get_user_from_event(event, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMata_beta_bot"
    catevent = await edit_or_reply(event, "**جار الكشف**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await dragoiq(unblock("SangMata_beta_bot"))
            await conv.send_message(f"{uid}")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(catevent, "**- الامـر في وضع الصيانه حاليـاً ...**")
    if "No data available" in responses:
        await edit_delete(catevent, "**المستخدم ليس لديه أي سجل اسمـاء بعـد ...**")
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    sandy = None
    check = usernames if cmd == " المعرف" else names
    for i in check:
        if sandy:
            await event.reply(i, parse_mode=_format.parse_pre)

        else:
            sandy = True
            await catevent.edit(i, parse_mode=_format.parse_pre)





@dragoiq.ar_cmd(
    pattern="الاسماء(المعرف)?(?:\s|$)([\s\S]*)",
    command=("الاسماء", plugin_category),
    info={
        "header": "To get name history of the user.",
        "flags": {
            "u": "That is sgu to get username history.",
        },
        "usage": [
            "{tr}كشف <username/userid/reply>",
            "{tr}كشف المعرف <username/userid/reply>",
        ],
        "examples": "{tr}sg @missrose_bot",
    },
)
async def _(event):  # sourcery no-metrics
    "To get name/username history."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "**- بالـرد ع الشخص او باضافة معـرف/ايـدي الشخـص للامـر**",
        )
    user, rank = await get_user_from_event(event, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMata_beta_bot"
    catevent = await edit_or_reply(event, "**جار الكشف**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await dragoiq(unblock("SangMata_beta_bot"))
            await conv.send_message(f"{uid}")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(catevent, "**- الامـر في وضع الصيانه حاليـاً ...**")
    if "No data available" in responses:
        await edit_delete(catevent, "**المستخدم ليس لديه أي سجل اسمـاء بعـد ...**")
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    sandy = None
    check = usernames if cmd == " المعرف" else names
    for i in check:
        if sandy:
            await event.reply(i, parse_mode=_format.parse_pre)

        else:
            sandy = True
            await catevent.edit(i, parse_mode=_format.parse_pre)
