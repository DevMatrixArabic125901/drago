import sys
import drago
from drago import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import dragoiq
from .utils import (
    add_bot_to_logger_group,
    install_externalrepo,
    ipchange,
    load_plugins,
    setup_bot,
    mybot,
    startupmessage,
    verifyLoggerGroup,
    saves,
)

LOGS = logging.getLogger("drago")

print(drago.__copyright__)
print("Licensed under the terms of the " + drago.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("᭡︙جـار بـدء سـورس ماتـركس︙᭡")
    dragoiq.loop.run_until_complete(setup_bot())
    LOGS.info("᭡︙تم اكتمال تنـصيب بـوتك على سـورس ماتـركس︙᭡")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

try:
    LOGS.info("᭡︙يتم تفعيل وضع الانلاين تلقائياً︙᭡")
    dragoiq.loop.run_until_complete(mybot())
    LOGS.info("᭡︙تم تفعيل وضع الانلاين تلقائياً بنجاح︙᭡")
except Exception as dragoiq:
    LOGS.error(f"- {dragoiq}")
    sys.exit()    

class CatCheck:
    def __init__(self):
        self.sucess = True


Catcheck = CatCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        Catcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("✦┅━╍━╍╍━━╍━━╍╍━━╍╍━━╍╍━━╍━┅✦")
    print("᭡︙تـم تنـصيب سـورس ماتـركس الـعربي بنجـاح︙᭡")
    print(
        f"᭡︙تم تشغيل الانلاين تلقائياً ارسل {cmdhr} الاوامر لـرؤيـة اوامر السورس︙᭡\
        \n᭡︙للمسـاعدة تواصـل  https://t.me/MaTrxSupport︙᭡"
    )
    print("✦┅━╍━╍╍━━╍━━╍╍━━╍╍━━╍╍━━╍━┅✦")
    await verifyLoggerGroup()
    await saves()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return

dragoiq.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    dragoiq.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        dragoiq.run_until_disconnected()
    except ConnectionError:
        pass
