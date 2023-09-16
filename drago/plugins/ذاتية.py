from drago import dragoiq
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from telethon import events
from drago import *

drago_Asbo3 = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}

@dragoiq.on(admin_cmd(pattern="(جلب الصورة|جلب الصوره|ذاتيه|ذاتية)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    drago = await event.get_reply_message()
    pic = await drago.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم حفظ الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
  """,
    )
    await event.delete()
@dragoiq.on(admin_cmd(pattern="(الذاتية تشغيل|ذاتية تشغيل)"))
async def ahmed(event):
    if gvarstatus ("savepicforme"):
        return await edit_delete(event, "** ᥀︙حفظ الذاتيات مفعل وليس بحاجة للتفعيل مجدداً **")
    else:
        addgvar("savepicforme", "ahmed")
        await edit_delete(event, "** ᥀︙تم تفعيل ميزة حفظ الذاتيات بنجاح ✓**")
 
@dragoiq.on(admin_cmd(pattern="(الذاتية تعطيل|ذاتية تعطيل)"))
async def mat_Is_Here(event):
    if gvarstatus ("savepicforme"):
        delgvar("savepicforme")
        return await edit_delete(event, "**᥀︙تم تعطيل حفظت الذاتيات بنجاح ✓**")
    else:
        await edit_delete(event, "**᥀︙انت لم تفعل حفظ الذاتيات لتعطيلها!**")

def matrix_unread_media(message):
    return message.media_unread and (message.photo or message.video)

async def Ahmed(event, caption):
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    drago_date = event.date.strftime("%Y-%m-%d")
    drago_day = drago_Asbo3[event.date.strftime("%A")]
    await bot.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, drago_date, drago_day),
        parse_mode="markdown"
    )
    os.remove(media)

@dragoiq.on(events.NewMessage(func=lambda e: e.is_private and matrix_unread_media(e) and e.sender_id != bot.uid))
async def Ahmed(event):
    if gvarstatus("savepicforme"):
        caption = """**
           ♡  غير مبري الذمة اذا استعملته للأبتزاز  ♡
♡ تم حفظ الذاتية بنجاح ✓
♡ أسم المرسل : [{0}](tg://user?id={1})
♡  تاريخ الذاتية : `{2}`
♡  أرسلت في يوم `{3}`
       ♡    MaTriX    ♡
        **"""
        await Ahmed(event, caption)
