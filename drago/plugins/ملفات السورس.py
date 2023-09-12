from drago import dragoiq
import pkg_resources
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from ..Config import Config
import json
import requests
import os

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
    await _zedutils.runcmd(cmd)
    OUTPUT = f"**اعـادة تهيئــة البـوت:**\n\n**تـم حذف جميـع المجـلدات والملفـات بنجـاح ✓**"
    event = await edit_or_reply(event, OUTPUT)
