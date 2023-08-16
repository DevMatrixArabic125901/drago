import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterPhotos

from drago import dragoiq
from ..helpers.utils import reply_id

# الي يخمط ويكول من كتابتي الا امه انيجه وقد اعذر من انذر
# ذمة بركبتك ليوم قيامة اذا اخذت امر او الملف
@dragoiq.on(admin_cmd(pattern="حالتي ?(.*)"))
async def _(event):
    await event.edit("**- يتم التاكد من حالتك اذا كنت محظور او لا**")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** اولا الغي حظر @SpamBot وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @src_dra")


@dragoiq.on(admin_cmd(pattern="الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("- انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir ( @auddbot ) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@dragoiq.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            dragoiqmail = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({dragoiqmail})"
        )
@dragoiq.on(admin_cmd(outgoing=True, pattern="غنيلي$"))
async def dragovois(vois):
  rl = random.randint(2,2301)
  url = f"https://t.me/AudiosWaTaN/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⌁︙ BY : @src_dra",parse_mode="html")
  await vois.delete()

@dragoiq.on(admin_cmd(outgoing=True, pattern="شعر$"))
async def dragovois(vois):
  rl = random.randint(2,622)
  url = f"https://t.me/L1BBBL/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⌁︙ BY : @src_dra",parse_mode="html")
  await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="راب$"))
async def dragovois(vois):
  rl = random.randint(2,86)
  url = f"https://t.me/RapEthan/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⌁︙ BY : @src_dra",parse_mode="html")
  await vois.delete()
@dragoiq.on(admin_cmd(outgoing=True, pattern="ريمكس$"))
async def dragovois(vois):
  rl = random.randint(2,279)
  url = f"https://t.me/remixsource/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⌁︙ BY : @src_dra",parse_mode="html")
  await vois.delete()
@dragoiq.ar_cmd(pattern="انمي$")
async def Ahmed(event):
 dragoevent = await edit_or_reply(event, "⇆")
    try:
        arph = [
            ahmed
            async for ahmed in event.client.iter_messages(
                "@AnimeWaTaN", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(arph),
            caption=f"⌁︙𝖠𝗇𝗂𝗆𝖾 𝖡𝖸 : @src_dra",
            buttons=[(Button.url("‹: 𝖲𝗈𝗎𝗋𝖼𝖾 𝖣𝗋𝖺𝖦𝗈 :›", "https://t.me/src_dra"),)],
        )
        await dragoevent.delete()
    except Exception:
        await dragoevent.edit("No Found")
