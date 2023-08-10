import asyncio
from collections import deque

from . import dragoiq, edit_or_reply

plugin_category = "fun"


@dragoiq.ar_cmd(
    pattern="افكر$",
    command=("افكر", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}افكر",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "افكر")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@dragoiq.ar_cmd(
    pattern="متت$",
    command=("متت", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}متت",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "متت")
    deq = deque(list("😹🤣😂😹🤣😂"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@dragoiq.ar_cmd(
    pattern="ضايج$",
    command=("ضايج", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}ضايج",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "ضايج")
    deq = deque(list("😕😞🙁☹️😕😞🙁"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@dragoiq.ar_cmd(
    pattern="ساعه$",
    command=("ساعه", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}ساعه",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "ساعه")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@dragoiq.ar_cmd(
    pattern="مح$",
    command=("مح", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}مح",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "مح")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@dragoiq.ar_cmd(
    pattern="قلب$",
    command=("قلب", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}قلب",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "قلب")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@dragoiq.ar_cmd(
    pattern="جيم$",
    command=("جيم", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}جيم",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "جيم")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@dragoiq.ar_cmd(
    pattern="الارض$",
    command=("الارض", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}الارض",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "الارض")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@dragoiq.ar_cmd(
    pattern="قمر$",
    command=("قمر", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}قمر",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@dragoiq.ar_cmd(
    pattern="اقمار$",
    command=("اقمار", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}اقمار",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "اقمار")
    animation_interval = 0.2
    animation_ttl = range(101)
    await event.edit("اقمار..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@dragoiq.ar_cmd(
    pattern="قمور$",
    command=("قمور", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}قمور",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "قمور")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])
@dragoiq.ar_cmd(
    pattern="موجوع$",
    command=("موجوع", plugin_category),
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("موجوع كلبي والتعب بيه")
        await asyncio.sleep(0.4)
        await event.edit(" من اباوع على روحي ينكسر كلبي عليه")
        await asyncio.sleep(0.6)
        await event.edit("موجوع كلبي والتعب بيه")
        await asyncio.sleep(0.4)
        await event.edit("من اباوع على روحي ينكسر كلبي عليه")
        await asyncio.sleep(0.4)
        await event.edit("تعبان وجهي وعيوني قهرتني")
        await asyncio.sleep(0.6)
        await event.edit("دنيا شلت حال حالي وبحياتي كرهتني")
        await asyncio.sleep(0.4)
        await event.edit("كرهت الحب, , ماريده دمرني")
        await asyncio.sleep(0.6)
        await event.edit("طيب اني وادري طيبي, , لهالحال وصلني")
        await asyncio.sleep(0.4)
        await event.edit(" موجوع كلبي, , والتعب بيه")
        await asyncio.sleep(0.6)
        await event.edit("من اباوع على روحي, , ينكسر كلبي عليه")
        await asyncio.sleep(0.4)
        await event.edit("كل يوم صدمه اقوى من اللي قبلها")
        await asyncio.sleep(0.6)
        await event.edit("اني واصل بالشدايد شده محد واصل الها")
        await asyncio.sleep(0.4)
