import random
import re
import time
from platform import python_version

from telethon import version, Button
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from drago import StartTime, dragoiq, DRAGOVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"

@dragoiq.ar_cmd(
    pattern="المطور$",
    command=("المطور", plugin_category),
    info={
        "header": "لأظهار مطورين السورس",
        "usage": [
            "{tr}المطور",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    CAT_IMG = "https://telegra.ph/file/1dc317fe998717901fc02.mp4"
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        matrix_caption = f"مطور ماتـركس العربي\n"
        matrix_caption += f"━━━━━━━━━━━━━\n"
        matrix_caption += f"- المـطور  : @X_EXTRA\n"    
        matrix_caption += f"━━━━━━━━━━━━━\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=matrix_caption, reply_to=reply_to_id
        )

@dragoiq.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)

MATRIXDEV = [6373798952]

@dragoiq.on(events.NewMessage(incoming=True))
async def Ahmed(event):
    if event.reply_to and event.sender_id in MATRIXDEV:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == dragoiq.uid:
           if event.message.message == "حظر من السورس":
               await event.reply("**حاضر مطوري ، لقد تم حظره من استخدام السورس**")
               addgvar("blockedfrom", "yes")
           elif event.message.message == "الغاء الحظر من السورس":
               await event.reply("**حاضر مطوري ، لقد الغيت الحظر**")
               delgvar("blockedfrom")
