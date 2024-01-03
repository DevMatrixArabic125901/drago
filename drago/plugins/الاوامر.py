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
f"**– – – – – – – – – – – – – – – –\n↯︙⦗ م1. ⦘ ↫ اوامر الادمن\n↯︙⦗ 2م. ⦘ ↫ اوامر القروب\n↯︙⦗ .م3 ⦘ ↫ اوامر الترحيب والردود \n↯︙⦗ .م4 ⦘ ↫ اوامر الخاص وتليكراف\n↯︙⦗ .م5 ⦘ ↫ اوامر المنشن والانتحال\n↯︙⦗ .م6 ⦘ ↫ اوامر الترجمة\n↯︙⦗ .م7 ⦘ ↫ اوامر المنع والقفل\n↯︙⦗ .م8 ⦘ ↫ اوامر التنظيف والتكرار\n↯︙⦗ .م9 ⦘  ↫ اوامر التخصيص والفارات\n↯︙⦗ .م10 ⦘ ↫ اوامر الوقتي والتشغيل\n↯︙⦗ .م11 ⦘ ↫ اوامر الكشف والروابط\n↯︙⦗ .م12 ⦘ ↫ اوامر المساعدة والاذاعة \n↯︙⦗ .م13 ⦘ ↫ اوامر الارسال والاذكار\n↯︙⦗ .م14 ⦘ ↫ اوامر الملصقات والكوكل\n↯︙⦗ .م15 ⦘ ↫ اوامر التسلية والميمز والتحشيش \n↯︙⦗ .م16 ⦘ ↫ اوامر الصيغ والجهات\n↯︙⦗ .م17 ⦘ ↫ اوامر التمبلر\n↯︙⦗ .م18 ⦘ ↫ اوامر الحساب والترفيه\n↯︙⦗ .م19 ⦘ ↫ اوامر بصمات\n↯︙⦗ .م20 ⦘ ↫ اوامر الذكاء الاصطناعي\n↯︙⦗ .م21 ⦘ ↫ اوامر تجميع السورس\n↯︙⦗ .م22 ⦘ ↫ اوامر خطوط السورس\n↯︙⦗ .م23 ⦘ ↫ اوامر تحميل من جميع المواقع\n↯︙⦗ .م24 ⦘ ↫ اوامر الهمسة السرية\n↯︙⦗ .م25 ⦘ ↫ اوامر البايو والاقتباس\n\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘\n↯︙جميع الاوامر بدايتها ↫ ⦗ . ⦘**"
	)
@dragoiq.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**قائمة اوامر الادمن لسورس ماتركس :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد القوائم\n\n- ( .اوامر الحظر )\n- ( .اوامر الكتم )\n- ( .اوامر التثبيت )\n- ( .اوامر الاشراف )\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘**"
)
		
@dragoiq.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"**قائمة اوامر المجموعه لسورس ماتركس :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد القوائم\n\n- ( .اوامر المحذوفين )\n- ( .اوامر الكروب )\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘**"
)

@dragoiq.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  "**قائمة اوامر الردود والترحيب لسورس ماتركس :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .اوامر الترحيب )\n- ( .اوامر الردود )\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘**"
)

@dragoiq.ar_cmd(  
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر الحماية والتلكراف لسورس ماتركس :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .اوامر الحماية )\n- ( .اوامر التلكراف ) \n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر المنشن والانتحال لسورس ماتركس :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .اوامر الانتحال )\n- ( .اوامر التقليد )\n- ( .اوامر المنشن ) \n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر الترجمة :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .اوامر النطق )\n- ( .اوامر الترجمة ) \n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر المنع والقفل :\n– – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .أۅٛأمࢪ أݪقفݪ )\n- ( .اوامر الفتح )\n- ( .اوامر المنع ) \n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر التنظيف والتكرار :\n– – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .اوامر التكرار )\n- ( .اوامر السبام )\n- ( .اوامر التنظيف ) \n- ( .اوامر المسح ) \n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قأئمة التخصيص والفارات :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .أۅٛأمࢪ أݪتخصيص )\n ݪتغيࢪ أݪصۅٛࢪ ۅٛأݪڪݪأيش ڪݪ مڼ أݪحمأية ۅٛأݪفحص ۅٛأݪبٰڼڪ\n- ( .اوامر الفارات )\n - ݪتغيࢪ أݪأسم ۅٛࢪ࣪خࢪفة أݪۅٛقت ۅٛأݪصۅٛࢪة أݪۅٛقتية ۅٛأݪمڼطقة أݪࢪ࣪مڼية ۅٛࢪمࢪ࣪ أݪأسم ۅٛأݪبٰأيۅٛ أݪۅٛقتي ۅٛغيࢪهأ\n– – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر الوقتي والتشغيل :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .اوامر الاسم )\n- ( .اوامر البايو )\n- ( .اوامر التشغيل ) \n- ( .اوامر الاطفاء ) \n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
) 

@dragoiq.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر الكشف والروابط:\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .اوامر الكشف )\n- ( .اوامر الروابط ) \n\n – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  "قائمة اوامر المساعدة  :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد هذه القوائم\n\n- ( .اوامر الوقت والتاريخ )\n- (.اوامر الكورونا )\n- ( .اوامر الصلاة ) \n- ( .اوامر المساعدة )\n- ( .اوامر الاذاعه )\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
  )
	 
@dragoiq.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر الملصقات والكوكل :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد القوائم\n\n- ( .اوامر الملصقات )\n- ( .اوامر الكوكل )\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر التسلية والتحشيش :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد القوائم\n\n- ( .اوامر التسلية )\n- ( .اوامر التحشيش )\n- ( .اوامر الميمز )\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  " قائمة اوامر تحويل الصيغ والجهات :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد القوائم\n\n- ( .اوامر التحويل )\n- ( .اوامر الجهات ) \n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
  "قائمة اوامر الحساب والترفيه :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد القوائم\n\n- ( .اوامر الترفيه )\n- ( .اوامر الحساب ) \n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م19$",
    command=("م19", plugin_category),
)
async def _(event):
 if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
  await event.edit(
   " قائمة اوامر بصمات الميمز :\n – – – – – – – – – – – – – – – –\n ↯︙ اختر احد القوائم\n\n- ( .بصمات ميمز )\n- ( .بصمات ميمز2 )\n- ( .بصمات ميمز3 )\n- ( .بصمات ميمز4 )\n- ( .بصمات ميمز5 )\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح عـن اެۅٛاެمـࢪ الذكاء الاصطناعي \n– – – – – – – – – – – – – – – –\n ↯︙ اختر احد الاوامر \n\n- ( .الذكاء تفعيل  )\n  ↯︙ݪيتم تشغيݪ الذكاء الاصطناعي عݪى اެݪاެشخاެص يجب كتاެبة\n- ( .الذكاء تعطيل )\n↯︙ݪيتم تعطيݪ الذكاء الاصطناعي عݪى اެݪاެشخاެص يجب كتاެبة\n\n- ( .ذكاء + اެݪسؤاެݪ ) \n ↯︙اެمࢪ الذكاء الاصطناعي يجب كتاެبة\n\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
) 

@dragoiq.ar_cmd(
    pattern="م21$",
    command=("م21", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قائمة اوامر التجميع\n– – – – – – – – – – – – – – – –\n↯︙ اختر احد الاوامر\n\n- ( .تجميع المليار )\n- ( .تجميع العقاب )\n- ( .تجميع العرب )\n- ( .تجميع المليون )\n- ( .تجميع دعمكم )\n\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م22$",
    command=("م22", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "↯︙قائمة الخطوط تفعيل ~ تعطيل نفس الامر \n– – – – – – – – – – – – – – – –\n↯︙ اختر احد الاوامر\n\n- ( .خط الغامق )\n- ( .خط الرمز )\n-( .خط المائل )\n-( .خط القوس )\n\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م23$",
    command=("م23", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قائمة اوامر التحميل من جميع المواقع\n– – – – – – – – – – – – – – – –\n↯︙ اختر احد الاوامر\n\n- ( .فيس )\n- ( .انستا )\n- ( .تيك )\n- ( .لايكي )\n- ( .بنترست )\n- ( .سناب )\n- ( .ساوند )\n\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م24$",
    command=("م24", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "↯︙شرح كيـفية كتابة همسة السرية**\n↯︙اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n↯︙مثال  :   .همسة ماتركس العربي @X_EXTRA\n\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
)

@dragoiq.ar_cmd(
    pattern="م25$",
    command=("م25", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قائمة اوامر البايو والاقتباس\n– – – – – – – – – – – – – – – –\n↯︙ اختر احد الاوامر\n\n- ( .البايو )\n- ( .اوامر اقتباس )\n\n– – – – – – – – – – – – – – – –\n↯︙قناة السورس ↫ ⦗ @MaTrixThoN ⦘"
	)
