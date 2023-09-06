import random
import re
import base64
import time
import asyncio
import os
from datetime import datetime
from platform import python_version

from telethon import version
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

#كتـابة وتعـديل:  @src_dra
#ذمة بركبتك ليوم قيامة اذا اخذت امر واحد من ملف الفحص
#ربي لايعطيك العافية والصحة اذا خمطت امر او ملف الفحص
#كس اخته الي ياخذ امر او ملف الفحص
#حسبية الله ونعمل الوكيل الي ياخذ امر او ملف الفحص

file_path = "installation_date.txt"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as file:
        installation_time = file.read().strip()
else:
    installation_time = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "w") as file:
        file.write(installation_time)

@dragoiq.ar_cmd(pattern="فحص(?:\s|$)([\s\S]*)")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "** ⌁︙ يتـم التـأكـد انتـظر قليلا رجاءا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "-‎"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**父[ 𝖣𝗋𝖺𝖦𝗈 𝗂𝗌 𝖶𝗈𝗋𝖪𝗂𝗇𝖦 ](t.me/src_dra)父**"
    DRAGO_IMG = gvarstatus("ALIVE_PIC") or Config.A_PIC
    dragoiq_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = dragoiq_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        matrixver=DRAGOVERSION,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        dragotime=installation_time,
    )
    if DRAGO_IMG:
        drago = [x for x in DRAGO_IMG.split()]
        PIC = random.choice(drago)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


temp = """{ALIVE_TEXT}
⊱━━━━━⊰✾⊱━━━━━⊰
**- سورس ماتركس يعمل بنجاح .**
**{EMOJI} قاعدة البيانات :** `{dbhealth}`
**{EMOJI} نسخــﮫ التيليثون ↬** `{telever}`
**{EMOJI} نسخــﮫ ماتركـس ↬** `{matrixver}`
**{EMOJI} اصدار البايثون ↬** `{pyver}`
**{EMOJI} مدﮪ التشغيل ↬** `{uptime}`
**{EMOJI} المالك ↬** {mention}
⊱━━━━━⊰✾⊱━━━━━⊰"""
