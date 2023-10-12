from telethon import events
import random, re
from ..Config import Config

from drago.utils import admin_cmd

import asyncio
from drago import dragoiq
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"

@dragoiq.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
 f"**[ᯏماެتـࢪكس اެݪعـࢪبيᯏ](t.me/MaTriXThon)\n✦┅━╍━╍╍━━╍━━╍━┅✦\n.م1  ◂ اެۅٛاެمࢪ اެݪاެدمن\n.م2  ◂ اެۅٛاެمࢪ اެݪمجمۅٛعة\n.م3  ◂ اެۅٛاެمࢪ اެݪتࢪحيب ۅٛاެݪࢪدۅٛد\n.م4  ◂ حماެية خاެص ۅٛاެݪتݪكࢪاެف\n.م5  ◂ اެۅٛاެمࢪ اެݪمنشن ۅٛاެݪاެنتحاެݪ\n.م6  ◂ اެۅٛاެمࢪ اެݪتࢪجمة\n.م7  ◂ اެۅٛاެمࢪ اެݪمنع ۅٛ اެݪقفݪ\n.م8  ◂ اެۅٛاެمࢪ اެݪتنظيف ۅٛاެݪتكࢪاެࢪ\n.م9  ◂ اެۅٛاެمࢪ اެݪتخصيص ۅٛاެݪفاެࢪاެت\n.م10 ◂ اެۅٛاެمࢪ اެݪۅٛقتي ۅٛ اެݪتشغيݪ\n.م11 ◂ اެۅٛاެمࢪ اެݪكشف ۅٛ اެݪࢪۅٛاެبط\n.م12 ◂ اެۅٛاެمࢪ اެݪمساެعدة ۅٛاެݪإذاެعة \n.م13 ◂ اެۅٛاެمࢪ اެݪاެࢪساެݪ ۅٛاެݪاެذكاެࢪ\n.م14 ◂ اެۅٛاެمࢪ اެݪمـݪصقاެت ۅٛكۅٛكݪ\n.م15 ◂ اެۅٛاެمࢪ اެݪتسݪية ۅٛاެݪميمࢪ࣪ ۅٛاެݪتحشيش \n.م16 ◂ اެۅٛاެمࢪ اެݪصيغ ۅٛاެݪجهاެت\n.م17 ◂ اެۅٛاެمࢪ اެݪتمبݪࢪ ۅٛاެݪࢪ࣪غࢪفة ۅٛاެݪمتحࢪكة\n.م18 ◂ اެۅٛاެمࢪ اެݪحساެب ۅٛاެݪتࢪفيه\n.م19 ◂ اެۅٛاެمࢪ بصماެت اެݪميمࢪ࣪\n.م20 ◂ اެۅٛاެمࢪ اެݪذكاެء اެݪاެصطناެعي\n.م21 ◂ اެۅٛاެمࢪ اެݪتجميع\n.م22 ◂ اެۅٛاެمࢪ اެݪخطۅٛط\n.م23 ◂ اެۅٛاެمࢪ اެݪتحميݪ\n.م24 ◂ اެۅٛاެمࢪ اެݪهمسة اެݪسࢪية\n.م25 ◂ اެۅٛاެمࢪ اެݪباެيۅٛ ۅٛاެݪاެقتباެس\n.م26 ◂ اެۅٛاެمࢪ اެݪاެكس اެۅٛ\n✦┅━╍━╍╍━━╍━━╍━┅✦**"
)

@dragoiq.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**قاެئمة اެۅٛاެمࢪ اެݪاެدمن ݪسۅٛࢪس ماެتࢪكس :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ اެختࢪ اެحدى هذه اެݪقۅٛاެئم\n\n- ( `.اوامر الحظر )\n- ( .اوامر الكتم )\n- ( .اوامر التثبيت )\n- ( .اوامر الاشراف )\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon**"
)
		
@dragoiq.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**قاެئمة اެۅٛاެمࢪ اެݪمجـمۅٛعه ݪسۅٛࢪس ماެتࢪكس :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ اެختࢪ اެحدى هذه اެݪقۅٛاެئم\n\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon**"
)

@dragoiq.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  "**قأئمة أۅٛأمࢪ أݪـتࢪحيبٰ ۅٛأݪـࢪدۅٛد :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon**"
)

@dragoiq.ar_cmd(  
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة أۅٛأمࢪ حـمأية أݪخأص ۅٛأݪتݪڪࢪأف :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة أۅٛأمࢪ أݪـمڼشڼ ۅٛأݪأڼتحأݪ :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة أۅٛأمࢪ أݪتࢪجمه :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر الترجمة` ) \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة أۅٛأمࢪ أݪقفݪ ۅٛأݪمڼع :\n✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( .أۅٛأمࢪ أݪقفݪ )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة أۅٛأمࢪ أݪتڪࢪأࢪ ۅٛأݪتڼظيف :\n✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( .اوامر التكرار )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة أݪتخصيص ۅٛأݪفأࢪأت :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( .أۅٛأمࢪ أݪتخصيص )\n ݪتغيࢪ أݪصۅٛࢪ ۅٛأݪڪݪأيش ڪݪ مڼ أݪحمأية ۅٛأݪفحص ۅٛأݪبٰڼڪ\n- ( `.اوامر الفارات` )\n - ݪتغيࢪ أݪأسم ۅٛࢪ࣪خࢪفة أݪۅٛقت ۅٛأݪصۅٛࢪة أݪۅٛقتية ۅٛأݪمڼطقة أݪࢪ࣪مڼية ۅٛࢪمࢪ࣪ أݪأسم ۅٛأݪبٰأيۅٛ أݪۅٛقتي ۅٛغيࢪهأ\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة أۅٛأمࢪ أݪۅٛقتي ۅٛأݪتشغيݪ :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( `.اوامر الاسم` )\n- ( .اوامر البايو )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon"
) 

@dragoiq.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة أۅٛأمࢪ أݪڪـشف ۅٛ أݪࢪۅٛأبٰط :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( .اوامر الكشف )\n- ( .اوامر الروابط ) \n\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة أۅٛأمࢪ أݪمسأعدة  :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ أختࢪ أحدىٰ هذه أݪقۅٛأئم\n\n- ( .اوامر الوقت والتاريخ )\n- (`.اوامر الكورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر المساعدة` )\n- ( `.اوامر الاذاعه` ) \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙مأتࢪڪـس أݪعـࢪبٰي : @MaTriXThon"ات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قاެئمة اެۅٛاެمࢪ اެݪمݪصقاެت ۅٛكۅٛكݪ :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ اެختࢪ اެحدى هذه اެݪقۅٛاެئم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر الكوكل` )\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قاެئمة اެۅٛاެمࢪ اެݪتسݪية ۅٛاެݪتحشيش :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ اެختࢪ اެحدى هذه اެݪقۅٛاެئم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قاެئمة اެۅٛاެمࢪ تحۅٛيݪ اެݪصيغ ۅٛ اެݪجهاެت :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ اެختࢪ اެحدى هذه اެݪقۅٛاެئم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)

 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قاެئمة اެۅٛاެمࢪ اެݪحساެب ۅٛ اެݪتࢪفيه :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ اެختࢪ اެحدى هذه اެݪقۅٛاެئم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م19$",
    command=("م19", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
   " قاެئمة اެۅٛاެمࢪ بصماެت اެݪميمࢪ࣪ :\n ✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ اެختࢪ اެحدى هذه اެݪقۅٛاެئم\n\n- ( `.بصمات ميمز` )\n- ( `.بصمات ميمز2` )\n- ( `.بصمات ميمز3` )\n- ( `.بصمات ميمز4` )\n- ( `.بصمات ميمز5` )\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـࢪح عـن اެۅٛاެمـࢪ اެݪذكاެء اެݪاެصطناެعي \n✦┅━╍━╍╍━━╍━━╍━┅✦\n ᭡︙ اެختࢪ اެحدى هذه اެݪاެۅٛاެمࢪ \n\n- ( `.الذكاء تفعيل`  )\n  ᭡︙ݪيتم تشغيݪ اެݪذكاެء اެݪاެصطناެعي عݪى اެݪاެشخاެص يجب كتاެبة\n- ( `.الذكاء تعطيل` )\n᭡︙ݪيتم تعطيݪ اެݪذكاެء اެݪاެصطناެعي عݪى اެݪاެشخاެص يجب كتاެبة\n\n- ( .ذكاء + اެݪسؤاެݪ ) \n ᭡︙اެمࢪ اެݪذكاެء اެݪاެصطناެعي يجب كتاެبة\n\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
) 

@dragoiq.ar_cmd(
    pattern="م21$",
    command=("م21", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قاެئمة اެۅٛاެمࢪ اެݪتجميع\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ اެختࢪ اެحدى هذه اެݪاެۅٛاެمࢪ\n\n- ( `.تجميع المليار` )\n- ( `.تجميع العقاب` )\n- ( `.تجميع العرب` )\n- ( `.تجميع المليون` )\n- ( `.تجميع دعمكم` )\n\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م22$",
    command=("م22", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "᭡︙قاެئمة اެݪخطۅٛط تفعيݪ/ۅٛاެݪتعطيݪ نفس اެݪاެمࢪ \n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ اެختࢪ اެحدى هذه اެݪاެۅٛاެمࢪ\n\n- ( `.خط الغامق` )\n- ( `.خط الرمز` )\n-( `.خط المائل` )\n-( `.خط القوس` )\n\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م23$",
    command=("م23", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قاެئمة اެۅٛاެمࢪ اެݪتحميݪ\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ اެختࢪ اެحدى هذه اެݪاެۅٛاެمࢪ\n\n- ( `.فيس` )\n- ( `.انستا` )\n- ( `.تيك` )\n- ( `.لايكي` )\n- ( `.بنترست` )\n- ( `.سناب` )\n- ( `.ساوند` )\n\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م24$",
    command=("م24", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "᭡︙شـࢪح كيـفية كـتاެبة همـسة سـࢪية**\n᭡︙اެۅٛݪاެ اެكتب اެݪاެمࢪ  .همسة  بعدهاެ اެݪࢪساެݪة بعدهاެ اެكتب معࢪف اެݪشخص\n᭡︙مـثاެݪ  :   `.همسة `ماެتࢪكس اެݪعࢪبي @X_EXTRA\n\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م25$",
    command=("م25", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قاެئمة اެۅٛاެمࢪ اެݪبـاެيۅٛ ۅٛ اެݪاެقـتباެس\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ اެختࢪ اެحدى هذه اެݪاެۅٛاެمࢪ\n\n- ( `.البايو` )\n- ( `.اوامر اقتباس` )\n\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
)

@dragoiq.ar_cmd(
    pattern="م26$",
    command=("م26", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قاެئمة اެۅٛاެمࢪ اެكس اެۅٛ\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ اެختࢪ اެحدى هذه اެݪاެۅٛاެمࢪ\n\n- ( `.اكس او` )\n\n✦┅━╍━╍╍━━╍━━╍━┅✦\n᭡︙ماެتࢪكـس اެݪعـࢪبي : @MaTriXThon"
	)
