# MATRIX & ZTHON

# Copyright (C) 2022 MATRIX . All Rights Reserved

#

# This file is a part of < https://github.com/qithoniq/matrix/ >

# PLease read the GNU Affero General Public License in

# <https://www.github.com/qithoniq/matrix/blob/main/LICENSE/>.



"""

MATRIX & ZTHON

- كتـابـة الاضـافـات

- تخمـط صيـر مطـور كفــوو واذكــر المصــدر

"""



import contextlib

import html

import os

import base64



from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from telethon.tl.types import MessageEntityMentionName



from requests import get

from telethon.tl.functions.photos import GetUserPhotosRequest

from telethon.tl.functions.users import GetFullUserRequest



from drago import dragoiq

from drago.core.logger import logging



from ..Config import Config

from ..core.managers import edit_or_reply, edit_delete

from ..helpers import reply_id

from ..sql_helper.globals import gvarstatus

from . import spamwatch



plugin_category = "العروض"

LOGS = logging.getLogger(__name__)


MATRIX_TEXT = gvarstatus("CUSTOM_ALIVE_TEXT") or "مـعلومـات حـسابـك مـن سـورس ماتـركس العـربي"

MATRIX = gvarstatus("CUSTOM_ALIVE_EMOJI") or "- "

VMATRIXV = gvarstatus("CUSTOM_ALIVE_FONT") or "✦┅━╍━╍╍━━╍━━╍━┅✦"

mat = (1260465030)

matrix = (6373798952)





async def get_user_from_event(event):

    if event.reply_to_msg_id:

        previous_message = await event.get_reply_message()

        user_object = await event.client.get_entity(previous_message.sender_id)

    else:

        user = event.pattern_match.group(1)

        if user.isnumeric():

            user = int(user)

        if not user:

            self_user = await event.client.get_me()

            user = self_user.id

        if event.message.entities:

            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):

                user_id = probable_user_mention_entity.user_id

                user_obj = await event.client.get_entity(user_id)

                return user_obj

        if isinstance(user, int) or user.startswith("@"):

            user_obj = await event.client.get_entity(user)

            return user_obj

        try:

            user_object = await event.client.get_entity(user)

        except (TypeError, ValueError) as err:

            await event.edit(str(err))

            return None

    return user_object





async def fetch_info(replied_user, event):

    """Get details from the User object."""

    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user

    replied_user_profile_photos = await event.client(

        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)

    )

    replied_user_profile_photos_count = "لا يـوجـد بروفـايـل"

    dc_id = "Can't get dc id"

    with contextlib.suppress(AttributeError):

        replied_user_profile_photos_count = replied_user_profile_photos.count

        dc_id = replied_user.photo.dc_id

    user_id = replied_user.id

    first_name = replied_user.first_name

    full_name = FullUser.private_forward_name

    common_chat = FullUser.common_chats_count

    username = replied_user.username

    user_bio = FullUser.about

    is_bot = replied_user.bot

    restricted = replied_user.restricted

    verified = replied_user.verified

    vvmatrixvv = (await event.client.get_entity(user_id)).premium

    photo = await event.client.download_profile_photo(

        user_id,

        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",

        download_big=True,

    )

    first_name = (

        first_name.replace("\u2060", "")

        if first_name

        else ("هذا المستخدم ليس له اسم أول")

    )

    full_name = full_name or first_name

    username = "@{}".format(username) if username else ("لا يـوجـد")

    user_bio = "لا يـوجـد" if not user_bio else user_bio

    zmsg = await bot.get_messages(event.chat_id, 0, from_user=user_id)
    iimatrixii = zmsg.total
    if iimatrixii < 100:
        imatrixi = "غير متفاعل"
    elif iimatrixii > 200 and iimatrixii < 500:
        imatrixi = "ضعيف"
    elif iimatrixii > 500 and iimatrixii < 700:
        imatrixi = "شد حيلك"
    elif iimatrixii > 700 and iimatrixii < 1000:
        imatrixi = "استمر"
    elif iimatrixii > 1000 and iimatrixii < 2000:
        imatrixi = "ملك التفاعل"
    elif iimatrixii > 2000 and iimatrixii < 3000:
        imatrixi = "امبراطور التفاعل"
    elif iimatrixii > 3000 and iimatrixii < 4000:
        imatrixi = "نار وشرار"
    else:
        imatrixi = "خاتم التفاعل"
################# Dev #################
    if user_id in matrix: 
        rotbat = "مطـور السـورس" 

    elif user_id in mat:

        rotbat = "مطـور السورس²" 

    elif user_id == (await event.client.get_me()).id and user_id not in matr_dev:

        rotbat = "مـالك الحساب " 

    else:

        rotbat = "العضـو"

################# Dev #################
    caption = f"<b> {MATRIX_TEXT} </b>\n"

    caption += f"ٴ<b>{VMATRIXV}</b>\n"

    caption += f"<b>{MATRIX}الاسـم    ⇠ </b> "

    caption += f'<a href="tg://user?id={user_id}">{full_name}</a>'

    caption += f"\n<b>{MATRIX}المعـرف  ⇠  {username}</b>"

    caption += f"\n<b>{MATRIX}الايـدي   ⇠ </b> <code>{user_id}</code>\n"

    caption += f"<b>{MATRIX}الرتبـــه   ⇠ {rotbat} </b>\n"

    if vvmatrixvv == True or user_id in matrix: 
        caption += f"<b>{MATRIX}الحسـاب ⇠  بـريميـوم</b>\n"

    caption += f"<b>{MATRIX}الرسائل   ⇠</b>  {iimatrixii} \n"
    caption += f"<b>{MATRIX}الصـور    ⇠ </b> {replied_user_profile_photos_count}\n"

    if user_id != (await event.client.get_me()).id: 
        caption += f"<b>{MATRIX}الـمجموعات المشتـركة ⇠ </b> {common_chat} \n"

    caption += f"<b>{MATRIX}البايـو     ⇠  {user_bio}</b> \n"

    caption += f"ٴ<b>{VMATRIXV}</b>"

    return photo, caption

# Copyright (C) 2021 matr-Thon . All Rights Reserved





@dragoiq.ar_cmd(

    pattern="ايدي(?: |$)(.*)",

    command=("ايدي", plugin_category),

    info={

        "header": "لـ عـرض معلومـات الشخـص",

        "الاستـخـدام": " {tr}ايدي بالـرد او {tr}ايدي + معـرف/ايـدي الشخص",

    },

)

async def who(event):

    "Gets info of an user"

    matr = await edit_or_reply(event, "⇆")

    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):

        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)

    replied_user = await get_user_from_event(event)

    try:

        photo, caption = await fetch_info(replied_user, event)

    except (AttributeError, TypeError):

        return await edit_or_reply(matr, "**- لـم استطـع العثــور ع الشخــص ؟!**")

    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:

        message_id_to_reply = None

    try:

        await event.client.send_file(

            event.chat_id,

            photo,

            caption=caption,

            link_preview=False,

            force_document=False,

            reply_to=message_id_to_reply,

            parse_mode="html",

        )

        if not photo.startswith("http"):

            os.remove(photo)

        await matr.delete()

    except TypeError:

        await matr.edit(caption, parse_mode="html")





@dragoiq.ar_cmd(

    pattern="ا(?: |$)(.*)",

    command=("ا", plugin_category),

    info={

        "header": "امـر مختصـر لـ عـرض معلومـات الشخـص",

        "الاستـخـدام": " {tr}ا بالـرد او {tr}ا + معـرف/ايـدي الشخص",

    },

)

async def who(event):

    "Gets info of an user"

    matr = await edit_or_reply(event, "⇆")

    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):

        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)

    replied_user = await get_user_from_event(event)

    try:

        photo, caption = await fetch_info(replied_user, event)

    except (AttributeError, TypeError):

        return await edit_or_reply(matr, "**- لـم استطـع العثــور ع الشخــص ؟!**")

    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:

        message_id_to_reply = None

    try:

        await event.client.send_file(

            event.chat_id,

            photo,

            caption=caption,

            link_preview=False,

            force_document=False,

            reply_to=message_id_to_reply,

            parse_mode="html",

        )

        if not photo.startswith("http"):

            os.remove(photo)

        await matr.delete()

    except TypeError:

        await matr.edit(caption, parse_mode="html")





@dragoiq.ar_cmd(

    pattern="صورته(?:\s|$)([\s\S]*)",

    command=("صورته", plugin_category),

    info={

        "header": "لـ جـلب بـروفـايـلات الشخـص",

        "الاستـخـدام": [

            "{tr}صورته + عدد",

            "{tr}صورته الكل",

            "{tr}صورته",

        ],

    },

)

async def potocmd(event):

    "To get user or group profile pic"

    uid = "".join(event.raw_text.split(maxsplit=1)[1:])

    user = await event.get_reply_message()

    chat = event.input_chat

    if user and user.sender:

        photos = await event.client.get_profile_photos(user.sender)

        u = True

    else:

        photos = await event.client.get_profile_photos(chat)

        u = False

    if uid.strip() == "":

        uid = 1

        if int(uid) > (len(photos)):

            return await edit_delete(

                event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **"

            )

        send_photos = await event.client.download_media(photos[uid - 1])

        await event.client.send_file(event.chat_id, send_photos)

    elif uid.strip() == "الكل":

        if len(photos) > 0:

            await event.client.send_file(event.chat_id, photos)

        else:

            try:

                if u:

                    photo = await event.client.download_profile_photo(user.sender)

                else:

                    photo = await event.client.download_profile_photo(event.input_chat)

                await event.client.send_file(event.chat_id, photo)

            except Exception:

                return await edit_delete(event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **")

    else:

        try:

            uid = int(uid)

            if uid <= 0:

                await edit_or_reply(

                    event, "**- رقـم خـاطـئ . . .**"

                )

                return

        except BaseException:

            await edit_or_reply(event, "**- رقـم خـاطـئ . . .**")

            return

        if int(uid) > (len(photos)):

            return await edit_delete(

                event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **"

            )



        send_photos = await event.client.download_media(photos[uid - 1])

        await event.client.send_file(event.chat_id, send_photos)

    await event.delete()
@dragoiq.ar_cmd(
    pattern="(الايدي|id)(?:\s|$)([\s\S]*)",
    command=("الايدي", plugin_category),
    info={
        "header": "To get id of the group or user.",
        "description": "if given input then shows id of that given chat/channel/user else if you reply to user then shows id of the replied user \
    along with current chat id and if not replied to user or given input then just show id of the chat where you used the command",
        "usage": "{tr}id <reply/username>",
    },
)
async def _(event):
    "To get id of the group or user."
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{str(e)}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"᥀︙ايدي المستخدم : `{input_str}` هو `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"᥀︙ايدي الدردشة/القناة `{p.title}` هو `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "᥀︙يـجب كـتابة مـعرف الشـخص او الـرد عـليه")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"᥀︙ايدي الدردشه: `{str(event.chat_id)}` \n⌁︙ ايدي المستخدم: `{str(r_msg.sender_id)}` \n⌁︙ ايدي الميديا: `{bot_api_file_id}`",
            )
        else:
            await edit_or_reply(
                event,
               f"᥀︙ايدي الدردشه : `{str(event.chat_id)}` \n⌁︙ ايدي المستخدم: `{str(r_msg.sender_id)}` ",
            )
    else:
        await edit_or_reply(event, f"᥀︙الـدردشـة الـحالية : `{str(event.chat_id)}`")
