from datetime import datetime

from drago import dragoiq
from ..core.managers import edit_delete, edit_or_reply


@dragoiq.ar_cmd(pattern="حساب العمر(?:\s|$)([\s\S]*)")
async def _(event):
    dragoyar = event.text[12:]
    if not dragoyar:
       return await edit_or_reply(event, "**⌁︙حساب العمر + السنة**")
    YearNow = datetime.now().year
    MyAge = YearNow - yar
    await edit_or_reply(e, "**⌁︙عمرك :**  {}".format(MyAge))
