import sys
from drago.core.logger import logging
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from ..Config import Config
from .client import DragoClient

LOGS = logging.getLogger("drago")

__version__ = "2.10.6"

loop = None

if Config.STRING_SESSION:
session = StringSession(str(Config.STRING_SESSION))
    
    session = "drago"

try:
    dragoiq = DragoClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(
        f"STRING_SESSION CODE WRONG MAKE A NEW SESSION - {e}\n كود سيشن تيليثـون غير صالح .. قم باستخـراج كود جديد ؟!"
    )
    sys.exit()

    dragoiq.tgbot = tgbot = DragoClient(
        session="Sessionszbot",
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=Config.TG_BOT_TOKEN)
