from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from ..core.logger import logging

LOGS = logging.getLogger(__name__)


# Admin checker by uniborg
async def is_admin(dragoiq, chat_id, userid):
    if not str(chat_id).startswith("-100"):
        return False
    try:
        dra_go = await dragoiq.get_permissions(chat_id, userid)
        chat_participant = dra_go.participant
        if isinstance(
            chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
        ):
            return True
    except Exception as e:
        LOGS.info(str(e))
        return False
    else:
        return False
