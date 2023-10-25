import os


from telethon.tl.functions.photos import GetUserPhotosRequest

from telethon.tl.functions.users import GetFullUserRequest

from telethon.tl.types import MessageEntityMentionName





from drago import dragoiq

from drago.Config import Config

from drago.core.logger import logging

from drago.core.managers import edit_or_reply

from ..sql_helper.globals import gvarstatus


LOGS = logging.getLogger(__name__)



MATRIX = gvarstatus("CUSTOM_ALIVE_EMOJI") or ": ›"
MATTRIX = gvarstatus("CUSTOM_ALIVE_EMOJI") or "‹ :"

VMATRIXV = gvarstatus("CUSTOM_ALIVE_FONT") or "✦┅━╍━╍╍━━╍━━╍━┅✦"

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



    replied_user_profile_photos_count = "⌔∮ هذا المستخدم لم يضع اي صورة"



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

    vvmatrixvv = (await event.client.get_entity(user_id)).premium


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



    username = "@{}".format(username) if username else ("⌔∮ هذا المستخدم ليس لديه معرف")



    user_bio = "⌔∮ هذا المستخدم ليس لديه اي نبذة" if not user_bio else user_bio

    
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
   
   rozrtba = (



        "مطـور السـورس"



        if user_id == 6373798952

        else ("العضـو")


    )



   rozrtba = (



        "مـالك الـحساب"



        if user_id == (await event.client.get_me()).id



        and user_id != 6373798952



        and user_id != 1260465030



        else rozrtba





    caption += f"<b>{VMATRIXV}</b>\n"


    caption += f"<b>{MATTRIX} الاسـم  ⇠ {full_name} {MATRIX}</b>\n"



    caption += f"<b>{MATTRIX} المـعـرف  ⇠ {username} {MATRIX}</b>\n"



    caption += f"<b>{MATTRIX} الايـدي  ⇜ <code>{user_id} {MATRIX}</code> </b>\n"



    caption += f"<b>{MATTRIX} الـمجموعات المشتـركة  ⇜ {common_chat} {MATRIX}</b>\n"



    caption += f"<b>{MATTRIX} عـدد الصـورة  ⇜ {replied_user_profile_photos_count} {MATRIX}\n</b>"



    caption += f"<b>{MATTRIX} الرتبـة  ⇠ {rozrtba} {MATRIX}</b>\n"

    
    caption += f"<b>{MATTRIX} التفاعل  ⇠ {imatrixi} {MATRIX}</b>\n"



    caption += f"<b>{MATTRIX} ️الـنبـذه  ⇠ {user_bio} {MATRIX}</b>\n"

    
    caption += f"<b>{VMATRIXV}</b>\n"



    return photo, caption











@dragoiq.ar_cmd(pattern="ايدي(?: |$)(.*)")



async def who(event):



    roz = await edit_or_reply(event, "**⌔∮ جار التعرف على المستخدم انتظر قليلا**")



    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):



        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)



    replied_user = await get_user_from_event(event)



    try:



        photo, caption = await fetch_info(replied_user, event)



    except AttributeError:



        return await edit_or_reply(



            roz, "**⌔∮ لم يتم العثور على معلومات لهذا المستخدم **"



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







@dragoiq.ar_cmd(pattern="ا(?: |$)(.*)")



async def who(event):



    roz = await edit_or_reply(event, "**⌔∮ جار التعرف على المستخدم انتظر قليلا**")



    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):



        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)



    replied_user = await get_user_from_event(event)



    try:



        photo, caption = await fetch_info(replied_user, event)



    except AttributeError:



        return await edit_or_reply(



            roz, "**⌔∮ لم يتم العثور على معلومات لهذا المستخدم **"



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



    await edit_or_reply(mention, f"[{tag}](tg://user?id={user.id})  ")
