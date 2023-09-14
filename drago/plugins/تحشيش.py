import html
import os
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from drago import dragoiq
from Dragoiq.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"



@dragoiq.on(admin_cmd(pattern="رفع جلب(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**᥀︙ لكك هذا المطور أحمد ︙᥀**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ المستخدم** [{drago}](tg://user?id={user.id}) \n**᥀︙  تـم رفعـه جلب 🐶 بواسطة :** {my_mention}**")

@dragoiq.on(admin_cmd(pattern="رفع تاج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"᥀︙ المستخدم [{drago}](tg://user?id={user.id}) \n**᥀︙  تـم رفعـه تاج بواسطة :** {my_mention} 👑🔥")

@dragoiq.on(admin_cmd(pattern="رفع قرد(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**᥀︙ لكك هذا المطور أحمد ︙᥀**")
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"᥀︙ المستخدم [{drago}](tg://user?id={user.id}) \n**᥀︙  تـم رفعـه قرد 🙊🙈 :** {my_mention}")

@dragoiq.on(admin_cmd(pattern="رفع بكلبي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ المستخدم** [{drago}](tg://user?id={user.id}) \n**᥀︙  تـم رفعـه بكلـبك 🤍 بواسطة :** {my_mention}**")
    
    

@dragoiq.on(admin_cmd(pattern="رفع مطي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**᥀︙ لكك هذا المطور أحمد ︙᥀**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ المستخدم** [{drago}](tg://user?id={user.id}) \n**᥀︙  تـم رفعـه مطي 🐴 بواسطة :** {my_mention} \n**᥀︙  تعال حبي استلم  انه **")

@dragoiq.on(admin_cmd(pattern="رفع زوجي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**᥀︙ لكك هذا المطور أحمد ︙᥀**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ المستخدم** [{drago}](tg://user?id={user.id}) \n**᥀︙  تـم رفعـه زوجك بواسطة :** {my_mention}**")
    
@dragoiq.ar_cmd(
    pattern="رزله(?:\s|$)([\s\S]*)",
    command=("رزله", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**᥀︙ لكك هذا المطور أحمد ︙᥀**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"᥀︙ ولك [{tag}](tg://user?id={user.id}) \n᥀︙ ما رزل زبايل 👍")

@dragoiq.on(admin_cmd(pattern="رفع حاته(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ المستخدم** [{drago}](tg://user?id={user.id}) \n**᥀︙ تـم رفعـها حاته الكروب بواسطة :** {my_mention}**")

@dragoiq.on(admin_cmd(pattern="رفع هايشة(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ المستخدم** [{drago}](tg://user?id={user.id}) \n**᥀︙  تـم رفعـه المتهم هايشة 🐄 بواسطة :** {my_mention} \n**᥀︙  ها يلهايشة خوش بيك حليب تعال احلبك 😂**")

@dragoiq.on(admin_cmd(pattern="رفع صاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ المستخدم** [{drago}](tg://user?id={user.id}) \n**᥀︙  تـم رفعـه صاك بواسطة :** {my_mention}**")


@dragoiq.on(admin_cmd(pattern="رفع زبال(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ المستخدم** [{drago}](tg://user?id={user.id}) \n**᥀︙  تـم رفعـه زبال الكروب 🧹 بواسطة :** {my_mention} \n**᥀︙  تعال يلزبال اكنس الكروب لا أهينك 🗑😹**")

@dragoiq.on(admin_cmd(pattern="رفع مميز(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ الحلو** 「[{drago}](tg://user?id={user.id})」 \n**᥀︙  تـم رفعه مميز بواسطة :** {my_mention}")

@dragoiq.on(admin_cmd(pattern="رفع ادمن(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ الحلو** 「[{drago}](tg://user?id={user.id})」 \n**᥀︙  تـم رفعه ادمن بواسطة :** {my_mention}")

@dragoiq.on(admin_cmd(pattern="رفع منشئ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ الحلو** 「[{drago}](tg://user?id={user.id})」 \n**᥀︙  تـم رفعه منشئ بواسطة :** {my_mention}")

@dragoiq.on(admin_cmd(pattern="رفع مالك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    drago = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙ الحلو** 「[{drago}](tg://user?id={user.id})」 \n**᥀︙  تـم رفعه مالك الكروب بواسطة :** {my_mention}")

@dragoiq.on(admin_cmd(pattern="رفع وصخ(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    drago = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"** ᥀︙  المستخدم => • ** [{drago}](tg://user?id={user.id}) \n ☑️ **᥀︙ تم رفعه وصخ الكروب 🤢 بواسطه  :**{my_mention} .\n**᥀︙  لك دكوم يلوصخ اسبح مو ريحتك كتلتنا 🤮 ** ")

@dragoiq.on(admin_cmd(pattern="زواج(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    drago = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"᥀︙ ** لقد تم زواجك/ج من : **[{drago}](tg://user?id={user.id}) 💍\n**᥀︙ الف الف مبروك الان يمكنك اخذ راحتكم ** ")

@dragoiq.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    drago = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᥀︙  انتِ طالق طالق طالق 🙎🏻‍♂️ من  :**{my_mention} .\n**᥀︙  لقد تم طلاقها بلثلاث وفسخ زواجكما الان الكل حر طليق ** ")

MATRIXDEV = [6373798952]
@dragoiq.on(events.NewMessage(incoming=True))
async def Ahmed(event):
    if event.reply_to and event.sender_id in MATRIXDEV:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == dragoiq.uid:
           if event.message.message == "/matrix":
               await event.reply("**᥀︙اهـلاً بـك مـطوري فـي سـورس ماتـركس الـعربي︙᥀**")
           elif event.message.message == "منصب؟":
               await event.reply("**᥀︙نعم مطوري︙᥀**")
           elif event.message.message == "/mat":
               await event.reply("**᥀︙اهـلاً بـك مـطوري فـي سـورس ماتـركس الـعربي︙᥀**")
