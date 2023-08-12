import os

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from drago import dragoiq
from drago.Config import Config
from drago.core.logger import logging
from drago.core.managers import edit_or_reply

LOGS = logging.getLogger(__name__)


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
    replied_user_profile_photos_count = "هذا المستخدم لم يضع اي صورة"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
        replied_user.photo.dc_id
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    replied_user.bot
    replied_user.restricted
    replied_user.verified
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس لديه اسم اول")
    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("هذا المستخدم ليس لديه معرف")
    user_bio = "هذا المستخدم ليس لديه اي نبذة" if not user_bio else user_bio
    rotbat = (
     "مطـور السورس"
        if user_id == 6528225068 or user_id == 1260465030
        else ("عضو")
    )
    rotbat = (
        "مـالك الحساب"
        if user_id == (await event.client.get_me()).id
        and user_id != 6528225068
        and user_id != 1260465030
        else rotbat
    )
    caption = " \n"
    caption += f"╎<b>الاسـم ⇜ </b> {full_name}\n"
    caption += f"╎<b>المـعـرف ⇜ </b> {username}\n"
    caption += f"╎<b> الايـدي  ⇜</b> <code>{user_id}</code>\n"
    caption += f"╎<b>الـمجموعات المشتـركة ⇜</b> {common_chat}\n"
    caption += f"╎<b>الصـور ⇜</b> {replied_user_profile_photos_count}\n"
    caption += f"╎<b>الرتبـه ⇜</b>{rotbat}\n"
    caption += f"╎<b>رابط حسـابه ⇜</b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>\n'
    caption += f"╎<b>البايـو ⇜</b> \n<code>{user_bio}</code>\n\n"
    caption = " \n"
    return photo, caption


@dragoiq.ar_cmd(pattern="ايدي(?: |$)(.*)")
async def who(event):
    roz = await edit_or_reply(event, "**⇆**")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(
            roz, "**لم يتم العثور على معلومات لهذا المستخدم **"
        )
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
        await roz.delete()
    except TypeError:
        await roz.edit(caption, parse_mode="html")


@dragoiq.ar_cmd(pattern="رابط الحساب(?:\s|$)([\s\S]*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"⪼  [{tag}](tg://user?id={user.id})  𓆰. ")
@dragoiq.ar_cmd(
    pattern="(الايدي|id)(?:\s|$)([\s\S]*)",
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
                    event, f"⌁︙ ايدي المستخدم : `{input_str}` هو `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"⌁︙ ايدي الدردشة/القناة `{p.title}` هو `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "⌁︙ يـجب كـتابة مـعرف الشـخص او الـرد عـليه")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"⌁︙ ايدي الدردشه: `{str(event.chat_id)}` \n⌁︙ ايدي المستخدم: `{str(r_msg.sender_id)}` \n⌁︙ ايدي الميديا: `{bot_api_file_id}`",
            )
        else:
            await edit_or_reply(
                event,
               f"⌁︙ ايدي الدردشه : `{str(event.chat_id)}` \n⌁︙ ايدي المستخدم: `{str(r_msg.sender_id)}` ",
            )
    else:
        await edit_or_reply(event, f"⌁︙ الـدردشـة الـحالية : `{str(event.chat_id)}`")
        
