import pkg_resources
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id, parse_pre, yaml_format, install_pip, get_user_from_event, _format
import re
import asyncio
import calendar
import json
import os
from telethon import events
from asyncio.exceptions import TimeoutError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ExportChatInviteRequest
from matrix import matrix
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import get_user_from_event, sanga_seperator
from bs4 import BeautifulSoup
from ..helpers.utils import _format
from datetime import datetime
from urllib.parse import quote
import barcode
import qrcode
import requests
from barcode.writer import ImageWriter
from bs4 import BeautifulSoup
from PIL import Image, ImageColor
from telethon.errors.rpcerrorlist import YouBlockedUserError
from drago import dragoiq
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from dragoiq.utils import admin_cmd
from ..helpers import AioHttp
from ..helpers.utils import _catutils, _format, reply_id

LOGS = logging.getLogger(__name__)
IQMOG = re.compile(
    "[" 
    "\U0001F1E0-\U0001F1FF"      "\U0001F300-\U0001F5FF"      "\U0001F600-\U0001F64F"   "\U0001F680-\U0001F6FF"  
    "\U0001F700-\U0001F77F"      "\U0001F780-\U0001F7FF"      "\U0001F800-\U0001F8FF"     "\U0001F900-\U0001F9FF"      "\U0001FA00-\U0001FA6F"  
    "\U0001FA70-\U0001FAFF"      "\U00002702-\U000027B0"      
    "]+")

def iqtfy(inputString: str) -> str:
    return re.sub(IQMOG, "", inputString)

plugin_category = "tools"

@dragoiq.ar_cmd(pattern="المكاتب")
async def ahmed(event):
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
    for i in installed_packages])
    list = "**قائمة المكاتب المثبته**\n"
    for i in installed_packages_list:
        list += f"{i}\n"
    list += "**سورس ماتركس**"
    await edit_or_reply(event, list)

@dragoiq.ar_cmd(
    pattern="الملفات$",
    command=("الملفات", plugin_category),
    info={
        "header": "To list all plugins in drago.",
        "usage": "{tr}plugins",
    },
)
async def _(event):
    "To list all plugins in drago"
    cmd = "ls drago/plugins"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = f"**[ماتركس](tg://need_update_for_some_feature/) الـمـلفـات:**\n{o}"
    await edit_or_reply(event, OUTPUT)


@dragoiq.ar_cmd(
    pattern="فاراتي$",
    command=("فاراتي", plugin_category),
    info={
        "header": "To list all environment values in drago.",
        "description": "to show all heroku vars/Config values in your drago",
        "usage": "{tr}env",
    },
)
async def _(event):
    "To show all config values in drago"
    cmd = "env"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = (
        f"**[ماتركس](tg://need_update_for_some_feature/) قـائمـة الـفـارات:**\n\n\n{o}\n\n**انتبه هنالك معلومات حساسة لا تُعطِها لشخص غير موثوق**"
    )
    await edit_or_reply(event, "**تم ارسال المعلومات في الرسائل المحفوضة \nانتبه من الاشخاص الي يطلبون منك كتابة هذا الامر يريد ان يخترقك!**")
    await dragoiq.send_message("me", OUTPUT)

@dragoiq.ar_cmd(
    pattern="متى$",
    command=("متى", plugin_category),
    info={
        "header": "To get date and time of message when it posted.",
        "usage": "{tr}when <reply>",
    },
)
async def _(event):
    "To get date and time of message when it posted."
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    await edit_or_reply(
        event, f"**᥀︙نـشـرت هـذه الـرسالة فـي  :** `{yaml_format(result)}`"
    )
@dragoiq.ar_cmd(pattern="رابط مباشر")
async def upload_ahmed(event):
    r = await event.get_reply_message()
    if r is None:
        return await edit_delete(event, "**᥀︙قم بالرد على ملف لرفعهُ**")
    if r.media is None:
        return await edit_delete(event, "**᥀︙قم بالرد على ملف لرفعهُ**")
    file = await event.client.download_media(r, Config.TEMP_DIR)
    await edit_or_reply(event, "**᥀︙يُجري عملية الرفع . .**")
    payload = {}
    image = {"file": open(file, "rb")}
    response = requests.request("POST", "https://api.anonfiles.com/upload", files=image, data = payload)
    res = response.json()
    if res["status"] == False:
        er = res["error"]["message"]
        return await edit_delete(event, f"حدث خطأ عند رفع الملف\n{er}") 
    url = res["data"]["file"]["url"]["short"]
    size = res["data"]["file"]["metadata"]["size"]["readable"]
    await edit_or_reply(event, f"**تم رفع الملف ✓**\n**mATriX⌁︙ الرابط:** {url}\n**᥀︙الحجم:** {size}")
    os.remove(file)

@dragoiq.ar_cmd(pattern="فرمته(?: |$)(.*)")
async def _(event):
    cmd = "rm -rf .*"
    await _catutils.runcmd(cmd)
    OUTPUT = f"**اعـادة تهيئــة البـوت:**\n\n**تـم حذف جميـع المجـلدات والملفـات بنجـاح ✓**"
    event = await edit_or_reply(event, OUTPUT)

@dragoiq.on(admin_cmd(pattern="بي دي اف ?(.*)"))
async def _(event):
    if not dragoiq.reply_to_msg_id:
        return await dragoiq.edit("**الرجاء الرد على أي نص**")
    reply_message = await matrix.get_reply_message()
    chat = "@office2pdf_bot"
    await matrix.edit("**`جاري تحويل إلى PDF ...`**")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(reply_message)
                convert = await conv.send_message("/ready2conv")
                cnfrm = await conv.get_response()
                editfilename = await conv.send_message("نعم")
                enterfilename = await conv.get_response()
                filename = await conv.send_message("dragoiq")
                started = await conv.get_response()
                pdf = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await dragoiq.edit("**قم بفك الحظر من البوت : @office2pdf_bot**")
                return
            await dragoiq.client.send_message(event.chat_id, pdf)
            await dragoiq.client.delete_messages(                conv.chat_id,                [
                    msg_start.id,
                    response.id,
                    msg.id,
                    started.id,
                    filename.id,
                    editfilename.id,
                    enterfilename.id,
                    cnfrm.id,
                    pdf.id,
                    convert.id,
                ],)
            await dragoiq.delete()
    except TimeoutError:
        return await matrix.edit("**خـطأ**") 

@dragoiq.on(admin_cmd(pattern="بوتي$"))
async def dragoiq(tgbot):
    TG_BOT_USERNAME = Config.TG_BOT_USERNAME
    await tgbot.reply(f"بوت ماتركس العربي الخاص بك : {TG_BOT_USERNAME}")

@matrix.on(admin_cmd(pattern="تقويم ([\s\S]*)"))    
async def _matrix(dragoiq):
    input_str = matrix.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) != 2:
        return await edit_delete(matrix, "تصحيح قم بكتابه الأمر : `.تقويم السنه الشهر ", 5` )

    matrix = input_sgra[0]
    mm = input_sgra[1]
    try:
        output_result = calendar.month(int(matrix.strip()), int(mm.strip()))
        await edit_or_reply(dragoiq, f"
{output_result}
")
    except Exception as e:
        await edit_delete(dragoiq, f"                                              خطأ :\n{str(e)}                       ", 5)
