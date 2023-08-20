import asyncio
import logging

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import User
from drago import dragoiq
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

from ..vc_drago.stream_helper import Stream
from ..vc_drago.tg_downloader import tg_dl
from ..vc_drago.vcp_helper import dravc

plugin_category = "calls"

logging.getLogger("pytgcalls").setLevel(logging.ERROR)

OWNER_ID = dragoiq.uid

vc_session = Config.VC_SESSION

if vc_session:
    vc_client = TelegramClient(
        StringSession(vc_session), Config.APP_ID, Config.API_HASH
    )
else:
    vc_client = dragoiq

vc_client.__class__.__module__ = "telethon.client.telegramclient"
vc_player = dravc(vc_client)

asyncio.create_task(vc_player.start())


@vc_player.app.on_stream_end()
async def handler(_, update):
    await vc_player.handle_next(update)


ALLOWED_USERS = set()


@dragoiq.ar_cmd(
    pattern="انضمام ?(\S+)? ?(?:-as)? ?(\S+)?",
    command=("انضمام", plugin_category),
    info={
        "header": "To join a Voice Chat.",
        "description": "To join or create and join a Voice Chat",
        "note": "You can use -as flag to join anonymously",
        "flags": {
            "-as": "To join as another chat.",
        },
        "usage": [
            "{tr}joinvc",
            "{tr}joinvc (chat_id)",
            "{tr}joinvc -as (peer_id)",
            "{tr}joinvc (chat_id) -as (peer_id)",
        ],
        "examples": [
            "{tr}joinvc",
            "{tr}joinvc -1005895485",
            "{tr}joinvc -as -1005895485",
            "{tr}joinvc -1005895485 -as -1005895485",
        ],
    },
)
async def joinVoicechat(event):
    "To join a Voice Chat."
    chat = event.pattern_match.group(1)
    joinas = event.pattern_match.group(2)

    await edit_or_reply(event, "**جار الانضمام للمكالمة الصوتية**")

    if chat and chat != "-as":
        if chat.strip("-").isnumeric():
            chat = int(chat)
    else:
        chat = event.chat_id

    if vc_player.app.active_calls:
        return await edit_delete(
            event, f"لقد انضممت بالفعل الى {vc_player.CHAT_NAME}"
        )

    try:
        vc_chat = await dragoiq.get_entity(chat)
    except Exception as e:
        return await edit_delete(event, f'ERROR : \n{e or "UNKNOWN CHAT"}')

    if isinstance(vc_chat, User):
        return await edit_delete(
            event, "لايمكنك استعمال اوامر الميوزك على الخاص فقط في المجموعات !"
        )

    if joinas and not vc_chat.username:
        await edit_or_reply(
            event, "**انت وين لكيت هل كلاوات حبيبي مو كتلك ميصير بلاتصال الخاص**"
        )
        joinas = False

    out = await vc_player.join_vc(vc_chat, joinas)
    await edit_delete(event, out)


@dragoiq.ar_cmd(
    pattern="غادر",
    command=("غادر", plugin_category),
    info={
        "header": "To leave a Voice Chat.",
        "description": "To leave a Voice Chat",
        "usage": [
            "{tr}leavevc",
        ],
        "examples": [
            "{tr}leavevc",
        ],
    },
)
async def leaveVoicechat(event):
    "To leave a Voice Chat."
    if vc_player.CHAT_ID:
        await edit_or_reply(event, "** تدلل غادرت من الاتصال **")
        chat_name = vc_player.CHAT_NAME
        await vc_player.leave_vc()
        await edit_delete(event, f"تمت المغادرة من {chat_name}")
    else:
        await edit_delete(event, "** انا لست منضم الى الاتصال عزيزي**")


@dragoiq.ar_cmd(
    pattern="قائمة_التشغيل",
    command=("قائمة_التشغيل", plugin_category),
    info={
        "header": "To Get all playlist.",
        "description": "To Get all playlist for Voice Chat.",
        "usage": [
            "{tr}playlist",
        ],
        "examples": [
            "{tr}playlist",
        ],
    },
)
async def get_playlist(event):
    "To Get all playlist for Voice Chat."
    await edit_or_reply(event, "**جارِ جلب قائمة التشغيل ......**")
    playl = vc_player.PLAYLIST
    if not playl:
        await edit_delete(event, "Playlist empty", time=10)
    else:
        dra = ""
        for num, item in enumerate(playl, 1):
            if item["stream"] == Stream.audio:
                dra += f"{num}. 🔉  `{item['title']}`\n"
            else:
                dra += f"{num}. 📺  `{item['title']}`\n"
        await edit_delete(event, f"**قائمة التشغيل:**\n\n{dra}\n**دراكو يتمنى لكم وقتاً ممتعاً**")


@dragoiq.ar_cmd(
    pattern="تشغيل ?(-f)? ?([\S ]*)?",
    command=("تشغيل", plugin_category),
    info={
        "header": "To Play a media as audio on VC.",
        "description": "To play a audio stream on VC.",
        "flags": {
            "-f": "Force play the Audio",
        },
        "usage": [
            "{tr}play (reply to message)",
            "{tr}play (yt link)",
            "{tr}play -f (yt link)",
        ],
        "examples": [
            "{tr}play",
            "{tr}play https://www.youtube.com/watch?v=c05GBLT_Ds0",
            "{tr}play -f https://www.youtube.com/watch?v=c05GBLT_Ds0",
        ],
    },
)
async def play_audio(event):
    "To Play a media as audio on VC."
    flag = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    if input_str == "" and event.reply_to_msg_id:
        input_str = await tg_dl(event)
    if not input_str:
        return await edit_delete(
            event, "**قم بالرد على ملف صوتي او رابط يوتيوب**", time=20
        )
    if not vc_player.CHAT_ID:
        return await edit_or_reply(event, "**`قم بلانضمام للمكالمة اولاً بأستخدام أمر `انضمام")
    if not input_str:
        return await edit_or_reply(event, "No Input to play in vc")
    await edit_or_reply(event, "**يتم الان تشغيل الاغنية في الاتصال**")
    if flag:
        resp = await vc_player.play_song(input_str, Stream.audio, force=True)
    else:
        resp = await vc_player.play_song(input_str, Stream.audio, force=False)
    if resp:
        await edit_delete(event, resp, time=30)


@dragoiq.ar_cmd(
    pattern="ايقاف_مؤقت",
    command=("ايقاف_مؤقت", plugin_category),
    info={
        "header": "To Pause a stream on Voice Chat.",
        "description": "To Pause a stream on Voice Chat",
        "usage": [
            "{tr}pause",
        ],
        "examples": [
            "{tr}pause",
        ],
    },
)
async def pause_stream(event):
    "To Pause a stream on Voice Chat."
    await edit_or_reply(event, "**تم ايقاف الموسيقى مؤقتاً**")
    res = await vc_player.pause()
    await edit_delete(event, res, time=30)


@dragoiq.ar_cmd(
    pattern="استمرار",
    command=("استمرار", plugin_category),
    info={
        "header": "To Resume a stream on Voice Chat.",
        "description": "To Resume a stream on Voice Chat",
        "usage": [
            "{tr}resume",
        ],
        "examples": [
            "{tr}resume",
        ],
    },
)
async def resume_stream(event):
    "To Resume a stream on Voice Chat."
    await edit_or_reply(event, "**تم استمرار الاغنيه استمتع**")
    res = await vc_player.resume()
    await edit_delete(event, res, time=30)


@dragoiq.ar_cmd(
    pattern="تخطي",
    command=("تخطي", plugin_category),
    info={
        "header": "To Skip currently playing stream on Voice Chat.",
        "description": "To Skip currently playing stream on Voice Chat.",
        "usage": [
            "{tr}skip",
        ],
        "examples": [
            "{tr}skip",
        ],
    },
)
async def skip_stream(event):
    "To Skip currently playing stream on Voice Chat."
    await edit_or_reply(event, "**تم تخطي الاغنية تشغيل الاغنيه التالية**")
    res = await vc_player.skip()
    await edit_delete(event, res, time=30)


"""
@dragoiq.ar_cmd(
    pattern="a(?:llow)?vc ?([\d ]*)?",
    command=("allowvc", plugin_category),
    info={
        "header": "To allow a user to control VC.",
        "الوصـف": "To allow a user to controll VC.",
        "الاستخـدام": [
            "{tr}allowvc",
            "{tr}allowvc (user id)",
        ],
    },
)
async def allowvc(event):
    "To allow a user to controll VC."
    user_id = event.pattern_match.group(1)
    if user_id:
        user_id = user_id.split(" ")
    if not user_id and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        user_id = [reply.from_id]
    if not user_id:
        return await edit_delete(event, "Whom should i Add")
    ALLOWED_USERS.update(user_id)
    return await edit_delete(event, "Added User to Allowed List")


@dragoiq.ar_cmd(
    pattern="d(?:isallow)?vc ?([\d ]*)?",
    command=("disallowvc", plugin_category),
    info={
        "header": "To disallowvc a user to control VC.",
        "الوصـف": "To disallowvc a user to controll VC.",
        "الاستخـدام": [
            "{tr}disallowvc",
            "{tr}disallowvc (user id)",
        ],
    },
)
async def disallowvc(event):
    "To allow a user to controll VC."
    user_id = event.pattern_match.group(1)
    if user_id:
        user_id = user_id.split(" ")
    if not user_id and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        user_id = [reply.from_id]
    if not user_id:
        return await edit_delete(event, "Whom should i remove")
    ALLOWED_USERS.difference_update(user_id)
    return await edit_delete(event, "Removed User to Allowed List")


@dragoiq.on(
    events.NewMessage(outgoing=True, pattern=f"{tr}(speak|sp)(h|j)?(?:\s|$)([\s\S]*)")
)  #only for dragoiq client
async def speak(event):
    "Speak in vc"
    r = event.pattern_match.group(2)
    input_str = event.pattern_match.group(3)
    re = await event.get_reply_message()
    if ";" in input_str:
        lan, text = input_str.split(";")
    else:
        if input_str:
            text = input_str
        elif re and re.text and not input_str:
            text = re.message
        else:
            return await event.delete()
        if r == "h":
            lan = "hi"
        elif r == "j":
            lan = "ja"
        else:
            lan = "en"
    text = deEmojify(text.strip())
    lan = lan.strip()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    file = "./temp/" + "voice.ogg"
    try:
        tts = gTTS(text, lang=lan)
        tts.save(file)
        cmd = [
            "ffmpeg",
            "-i",
            file,
            "-map",
            "0:a",
            "-codec:a",
            "libopus",
            "-b:a",
            "100k",
            "-vbr",
            "on",
            file + ".opus",
        ]
        try:
            t_response = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await edit_or_reply(event, str(exc))
        else:
            os.remove(file)
            file = file + ".opus"
        await vc_player.play_song(file, Stream.audio, force=False)
        await event.delete()
        os.remove(file)
    except Exception as e:
         await edit_or_reply(event, f"**Error:**\n`{e}`")
"""