#ذمة بركبتك ليوم قيامة اذا اخذت اكواد لنفسك تصير اذا تريد تصير مطور اكتب بنفسك مو تخمط 👍
from telethon import events
from drago import dragoiq
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete
from telethon import functions
from telethon.errors.rpcerrorlist import MessageIdInvalidError
@dragoiq.on(admin_cmd(pattern="(خط الغامق|خط غامق)"))
async def btext(event):
    isbold = gvarstatus("bold")
    if not isbold:
        addgvar ("bold", "on")
        await edit_delete(event, "**᥀︙تم تفعيل خط الغامق بنجاح**")
        return

    if isbold:
        delgvar("bold")
        await edit_delete(event, "**᥀︙تم اطفاء خط الغامق بنجاح**")
        return

@dragoiq.on(admin_cmd(pattern="(خط رمز|خط الرمز)"))
async def btext(event):
    isramz = gvarstatus("ramz")
    if not isramz:
        addgvar ("ramz", "on")
        await edit_delete(event, "**᥀︙تم تفعيل خط الرمز بنجاح**")
        return

    if isramz:
        delgvar("ramz")
        await edit_delete(event, "**᥀︙تم اطفاء خط الرمز بنجاح**")
        return

@dragoiq.on(admin_cmd(pattern="(خط التشويش| خط تشويش)"))
async def btext(event):
    isramz = gvarstatus("matrxhide")
    if not isramz:
        addgvar ("matrxhide", "on")
        await edit_delete(event, "**᥀︙تم تفعيل خط التشويش بنجاح**")
        return

    if isramz:
        delgvar("ramz")
        await edit_delete(event, "**᥀︙تم اطفاء خط التشويش بنجاح**")
        

@dragoiq.on(events.NewMessage(outgoing=True))
async def reda(event):
    isbold = gvarstatus("bold")
    if isbold:
        try:
            await event.edit(f"**{event.message.message}**")
        except MessageIdInvalidError:
            pass
    isramz = gvarstatus("ramz")
    if isramz:
        try:
            await event.edit(f"`{event.message.message}`")
        except MessageIdInvalidError:
            pass
    matrixuserbot = gvarstatus("matrxhide")
    if matrixuserbot:
        try:
            await event.edit(f"||{event.message.message}||")
        except MessageIdInvalidError:
            pass
