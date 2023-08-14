from drago import dragoiq
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
import datetime
from telethon import events
from drago import *

DraGo_Ahmed = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}

@dragoiq.on(admin_cmd(pattern="(جلب الصورة|جلب الصوره|ذاتيه|ذاتية)"))
async def drago(event):
    if not event.is_reply:
        return await event.edit("..")
    UxUeU = await event.get_reply_message()
    pic = await UxUeU.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم حفظ الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @src_drago
- Dev: @UxUeU
  """,
    )
    await event.delete()
#By @src_drago For You
@dragoiq.on(admin_cmd(pattern="(الذاتية تشغيل|ذاتية تشغيل)"))
async def mohammed(event):
    if gvarstatus ("savepicforme"):
        return await edit_delete(event, "**⌁︙حفظ الذاتيات مفعل وليس بحاجة للتفعيل مجدداً **")
    else:
        addgvar("savepicforme", "mohammed")
        await edit_delete(event, "**⌁︙تم تفعيل ميزة حفظ الذاتيات بنجاح ✓**")
 
@dragoiq.on(admin_cmd(pattern="(الذاتية تعطيل|ذاتية تعطيل)"))
async def mohammed_Is_Here(event):
    if gvarstatus ("savepicforme"):
        delgvar("savepicforme")
        return await edit_delete(event, "**⌁︙تم تعطيل حفظت الذاتيات بنجاح ✓**")
    else:
        await edit_delete(event, "**⌁︙انت لم تفعل حفظ الذاتيات لتعطيلها!**")

def drago_unread_media(message):
    return message.media_unread and (message.photo or message.video)

async def Ahmed(event, caption):
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    UxUeU_date = event.date.strftime("%Y-%m-%d")
    UxUeU_day = DraGo_Ahmed[event.date.strftime("%A")]
    await bot.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, UxUeU_date, UxUeU_day),
        parse_mode="markdown"
    )
    os.remove(media)

@dragoiq.on(events.NewMessage(func=lambda e: e.is_private and drago_unread_media(e) and e.sender_id != bot.uid))
async def mohammed(event):
    if gvarstatus("savepicforme"):
        caption = """**
           ♡  غير مبري الذمة اذا استعملته للأبتزاز  ♡
♡ تم حفظ الذاتية بنجاح ✓
♡ تم الصنع : @src_drago
♡ أسم المرسل : [{0}](tg://user?id={1})
♡  تاريخ الذاتية : `{2}`
♡  أرسلت في يوم `{3}`
       ♡    DraGo    ♡
        **"""
        await Ahmed(event, caption)
