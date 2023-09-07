import html
import os
import random

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from drago import dragoiq

from ..Config import Config
from Dragoiq.razan.resources.strings import *
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch

plugin_category = "utils"


@dragoiq.ar_cmd(
    pattern="نسبة الحب(?:\s|$)([\s\S]*)",
    command=("نسبة الحب", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    matrix = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(mention, f"نـسـبتكم انـت و [{matrix}](tg://user?id={user.id}) هـي {rza}")
    
    
   
@dragoiq.ar_cmd(
    pattern="نسبة الانوثة(?:\s|$)([\s\S]*)",
    command=("نسبة الانوثة", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    matrix = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(mention, f"⌁︙ نسبة الانوثة لـ [{matrix}](tg://user?id={user.id}) هـي {sos}")

@dragoiq.ar_cmd(
    pattern="نسبة الرجولة(?:\s|$)([\s\S]*)",
    command=("نسبة الرجولة", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    matrix = user.first_name.replace("\u2060", "") if user.first_name else user.username
    dra = random.choice(rr7)
    await edit_or_reply(mention, f"⌁︙ نسبة الرجولة لـ [{matrix}](tg://user?id={user.id}) هـي {dra}")

@dragoiq.ar_cmd(
    pattern="نسبة الغباء(?:\s|$)([\s\S]*)",
    command=("نسبة الغباء", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**0% ♥🙂**")
    matrix = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(mention, f"نسبة الغباء لـ [{matrix}](tg://user?id={user.id}) هـي {rzona} 😂💔")

@dragoiq.ar_cmd(
    pattern="نسبة الكذب(?:\s|$)([\s\S]*)",
    command=("نسبة الكذب", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**0% ♥🙂**")
    matrix = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(mention, f"نسبة الكذب لـ [{matrix}](tg://user?id={user.id}) هـي {rzona}")

@dragoiq.ar_cmd(
    pattern="نسبة الذكاء(?:\s|$)([\s\S]*)",
    command=("نسبة الذكاء", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**100% ميحتاج تسوي نسبة الذكاء للمطور معروف**")
    matrix = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(mention, f"نسبة الذكاء لـ [{matrix}](tg://user?id={user.id}) هـي {rzona}🎈🧸")

@dragoiq.ar_cmd(
    pattern="نسبة الخيانه(?:\s|$)([\s\S]*)",
    command=("نسبة الخيانه", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**دي لك أحمد تاج راسك وميخون شخص**")
    matrix = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(mention, f"نسبة الخيانه لـ [{matrix}](tg://user?id={user.id}) هـي {rzona}🎈🧸")

@dragoiq.ar_cmd(
    pattern="نسبة الجمال(?:\s|$)([\s\S]*)",
    command=("نسبة الجمال", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6373798952:
        return await edit_or_reply(mention, f"**أحمد صاك ميحتاج تقييمه**")
    matrix = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(mention, f"نسبة جماله لـ [{matrix}](tg://user?id={user.id}) هـي {rzona}🎈🧸")
