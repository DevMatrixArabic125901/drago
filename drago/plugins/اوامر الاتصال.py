from drago.core.logger import logging
from telethon import TelegramClient, client, events

from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

import os
try:
    import pytgcalls
except ModuleNotFoundError:
    os.system("pip3 install pytgcalls")
    import pytgcalls

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped, AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo
from drago import dragoiq

from ..Config import Config
from telethon.sessions import StringSession

import asyncio
LOGS = logging.getLogger(__name__)

new_dragoiq = TelegramClient(StringSession(Config.STRING_SESSION), Config.APP_ID, Config.API_HASH)

async def PyStart():
    global dragoiq_py
    try:
        await new_dragoiq.start()
        dragoiq_py = PyTgCalls(new_dragoiq)
        await dragoiq_py.start()
    except Exception as error:
        print (error)

async def JoinThenStreamVideo(chat_id, StreamFile):
    global dragoiq_py
    await PyStart()
    await dragoiq_py.join_group_call(
        int(chat_id),
        AudioVideoPiped(
            StreamFile,
            HighQualityAudio(),
            HighQualityVideo(),
        ),
        stream_type=StreamType().local_stream,
    )
    await idle()
    
async def JoinThenStreamAudio(chat_id, StreamFile):
    global dragoiq_py
    await PyStart()
    await dragoiq_py.join_group_call(
        int(chat_id),
        AudioPiped(
            StreamFile,
            HighQualityAudio(),
        ),
        stream_type=StreamType().local_stream,
    )
    await idle()
    
async def LeaveStream(chat_id):
    global dragoiq_py
    await dragoiq_py.leave_group_call(
        chat_id,
    )


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]
        
# DOWNLOAD THEN STREAM AUDIO
@dragoiq.on(events.NewMessage(outgoing=True, pattern=r'.شغل صوت'))
async def AudioFileToVoiceChat(event):
    if event.reply_to != None:
        try:
            from telethon.tl.functions.channels import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(channel=event.chat_id, id=[event.reply_to.reply_to_msg_id]))
        except:
            from telethon.tl.functions.messages import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(id=[event.reply_to.reply_to_msg_id]))
            
        try:
            if message_media.messages[0].media != None and str(message_media.messages[0].media.document.mime_type).startswith('audio'):
                edit = await event.edit('**`جاري تشغيل المقطع الصوتي ...`**')
                filename = await event.client.download_media(message_media.messages[0], 'audio')
                
                edit = await event.edit("**` تم تشغيل بنجاح`**")
                try:
                    stream = await JoinThenStreamAudio(f'{event.chat_id}', filename)
                    edit = await event.edit('**⌁ ⦙ تم بنجاح**')
                except Exception as error:
                    print (error)
                    edit = await event.edit('**⌁ ⦙ البث جاريي, اذا لم يبدأ اوقف البث و حاول مرة اخرى**')
            else:
                edit = await event.edit('**⌁ ⦙ يجب الرد على صوتية**')
                
        except Exception as error:
            edit = await event.edit('**⌁ ⦙ يجب الرد على صوتية**')
    else:
        edit = await event.edit('**⌁ ⦙ يجب الرد على صوتية**')
    

# DOWNLOAD THEN STREAM VIDEO
@dragoiq.on(events.NewMessage(outgoing=True, pattern=r'.شغل فيديو'))
async def VideoFileToVoiceChat(event):
    if event.reply_to != None:
        try:
            from telethon.tl.functions.channels import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(channel=event.chat_id, id=[event.reply_to.reply_to_msg_id]))
        except:
            from telethon.tl.functions.messages import GetMessagesRequest
            message_media = await event.client(GetMessagesRequest(id=[event.reply_to.reply_to_msg_id]))
            
        try:
            if message_media.messages[0].media != None and str(message_media.messages[0].media.document.mime_type).startswith('video'):
                edit = await event.edit('**`جاري تشغيل المقطع الفيديو ...`**')
                filename = await event.client.download_media(message_media.messages[0], 'video')
                
                edit = await event.edit("**`تم تشغيل بنجاح`**")
                try:
                    stream = await JoinThenStreamVideo(f'{event.chat_id}', filename)
                    edit = await event.edit('**⌁ ⦙ تم .. بنجـاح**')
                except Exception as error:
                    print (error)
                    edit = await event.edit('**⌁ ⦙ البث جاري, اذا لم يبدأ اوقف البث و حاول مرة اخرى**')
            else:
                edit = await event.edit('**⌁ ⦙ يجب الرد على الفيديو**')
                
        except Exception as error:
            edit = await event.edit('**⌁ ⦙ يجب الرد على الفيديو**')
    else:
        edit = await event.edit('**⌁ ⦙ يجب الرد على الفيديو**')