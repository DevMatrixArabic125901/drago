from telethon import events
import random, re
from drago.utils import admin_cmd
import asyncio 

@borg.on(
    admin_cmd(pattern="همسة ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    dragoiqb = event.pattern_match.group(1)
    rrrd7 = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    dra = await bot.inline_query(rrrd7, dragoiqb) 
    await dra[0].click(event.chat_id)
    await event.delete()
    
@borg.on(admin_cmd("م27"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("الامر  • `.همسة`\n᥀︙الاستخدام  • لكتابة همسه سرية لشخص في المجموعه \n\n᥀︙الامر • `.الهمسة`\n᥀︙استخدامه • لعرض كيفية كتابة همسة سرية\n\n᥀︙الامر • `.اكس او `\n ᥀︙استخدامه • ففط ارسل الامر لبدء لعبة اكس او\n\n⌁︙ ماتـركس الـعربي  - @MaTriXThon")
         
@borg.on(admin_cmd("الهمسة"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**᥀︙شـرح كيـفية كـتابة همـسة سـرية**\n᥀︙اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n⌁︙ مـثال  :   `.همسة ههلا @X_EXTRA`")
        
@borg.on(
    admin_cmd(
       pattern="اكس او$"
    )
)
async def gamez(event):
    if event.fwd_from:
        return
    matrixusername = "@xoBot"
    uunzz = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    dra = await bot.inline_query(matrixusername, uunzz)
    await dra[0].click(event.chat_id)
    await event.delete()
