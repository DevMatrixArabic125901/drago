# WRITE  BY Drago_dr
# PLUGIN FOR Drago_dr 
# @Drago_dr

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

drago = [
    "قال المهدي(عجل الله فرجه):الدّينُ لمحمّد صلى الله عليه وآله وسلم والهدايةُ لعَلِيٍّ أمير المؤمنين ع، لأنها لهُ وفي عَقِبِه باقيةً إلى يومِ القيامة",
    "قال المهدي(عجل الله فرجه):إذا استغفرت الله (عز وجل) فالله يغفر لك",
    "قال المهدي(عجل الله فرجه):لا يحلّ لأحد أن يتصرّف في مال غيره بغير إذنه",
    "قال المهدي(عجل الله فرجه):إن اُستَرشدت أُرشِدتَ، وإن طَلبت وجدت",
    "قَالَ الإمام علي (عليه السلام): يَا ابْنَ آدَمَ إِذَا رَأَيْتَ رَبَّكَ سُبْحَانَهُ يُتَابِعُ عَلَيْكَ نِعَمَهُ وَأَنْتَ تَعْصِيهِ فَاحْذَرْهُ",
    "قَالَ الإمام علي (عليه السلام): الصَّبْرُ صَبْرَانِ صَبْرٌ عَلَى مَا تَكْرَهُ وَصَبْرٌ عَمَّا تُحِبُّ",
    "قَالَ الإمام علي (عليه السلام): لَا يَكُونُ الصَّدِيقُ صَدِيقاً حَتَّى يَحْفَظَ أَخَاهُ فِي ثَلَاثٍ فِي نَكْبَتِهِ وَغَيْبَتِهِ وَوَفَاتِهِ",
    "قال الإمام الصادق(عليه السلام): اكتبوا فإنكم لا تحفظون حتى تكتبو",
    "قال الإمام الصادق(عليه السلام): ركعة يصليها الفقيه أفضل من سبعين ألف ركعة يصليها العابد",
    "قال الإمام الصادق(عليه السلام): طلب العلم فريضة من فرائض الله",
    "عن رسول الله (صلى الله عليه وآله): الْبَخِيلُ‏ حَقّاً مَنْ ذُكِرْتُ عِنْدَهُ فَلَمْ يُصَلِّ عَلَيَّ",
    "عن رسول الله (صلى الله عليه وآله): مَنْ أَتَانِي زَائِراً كُنْتُ شَفِيعَهُ‏ يَوْمَ‏ الْقِيَامَة",
    "عن رسول الله (صلى الله عليه وآله): بُغْضُ‏ عَلِيٍ‏ كُفْرٌ وَ بُغْضُ بَنِي هَاشِمٍ نِفَاقٌ",
    "عن الامام علي (عليه السلام) قال : أعظم الذنوب ما استخف به صاحبه",
    "عن الامام علي (عليه السلام) قال : إذا قويت فاقو على طاعة الله، وإذا ضعفت فاضعف في معصيته",
    "عن الامام علي (عليه السلام) قال : أعداؤك ثلاثة: عدوك، وصديق عدوك، وعدو صديقك",
    "عن الامام علي (عليه السلام) قال : لا غنى كالعقل، ولا فقر كالجهل، ولا ميراث كالأدب",
    "عن الامام علي (عليه السلام) قال : لسانك حصانك، إن صنته صانك",
]
@dragoiq.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        FFlXlX = random.choice(drago)
        await event.edit(
	f"**‹ اوامر سورس دراكو ›**\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n`.م1`  ⦙ **اوامر الادمن**\n`.م2`  ⦙ **اوامر المجموعة**\n`.م3`  ⦙ **اوامر الترحيب والردود**\n`.م4`  ⦙ **حماية خاص والتلكراف**\n`.م5`  ⦙ **اوامر المنشن والانتحال**\n`.م6`  ⦙ **اوامر التحميل والترجمة**\n`.م7`  ⦙ **اوامر المنع و القفل**\n`.م8`  ⦙ **اوامر التنظيف والتكرار**\n`.م9`  ⦙ **اوامر التخصيص والفارات**\n`.م10` ⦙ **اوامر الوقتي و التشغيل**\n`.م11` ⦙ **اوامر الكشف و الروابط**\n`.م12` ⦙ **اوامر المساعدة والإذاعة** \n`.م13` ⦙ **اوامر الارسال والاذكار**\n`.م14` ⦙ **اوامر المـلصقات وكوكل**\n`.م15` ⦙ **اوامر التسلية والميمز والتحشيش** \n`.م16` ⦙ **اوامر الصيغ والجهات**\n`.م17` ⦙ **اوامر التمبلر والزغرفة والمتحركة**\n`.م18` ⦙ **اوامر الحساب والترفيه**\n`.م19` **اوامر بصمات الميمز**\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n **⌁︙ {FFlXlX} **"
	)
@dragoiq.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الادمن لسورس دراكو **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)
		
@dragoiq.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المجـموعه لسورس دراكو **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)

@dragoiq.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـترحيب والـردود **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)
@dragoiq.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر حـماية الخاص والتلكراف **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)
@dragoiq.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـمنشن والانتحال **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)

@dragoiq.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التحميل والترجمه **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)

@dragoiq.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر القفل والمنع **:\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)

@dragoiq.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التكرار والتنظيف **:\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)

@dragoiq.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة التخصيص والفارات **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التخصيص` )\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n- ( `.اوامر الفارات` )\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
		)

@dragoiq.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الوقتي والتشغيل **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر الكروب الوقتي` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)	

@dragoiq.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الكـشف و الروابط **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)
@dragoiq.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المساعدة  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)
@dragoiq.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الارسال **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)
@dragoiq.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الملصقات وكوكل **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)

@dragoiq.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التسلية والتحشيش **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)

@dragoiq.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر تحويل الصيغ و الجهات **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"
)

@dragoiq.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الحساب و الترفيه **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌔︙CH : @Drago_dr"

)

@dragoiq
@dragoiq.ar_cmd(
    pattern="م19$",
    command=("م19", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
			"** قائمة اوامر بصمات الميمز **:\n ★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n ⌁︙ اختر احدى هذه القوائم\n\n- ( `.بصمات ميمز` )\n- ( `.بصمات ميمز2` )\n- ( `.بصمات ميمز3` )\n- ( `.بصمات ميمز4` )\n- ( `.بصمات ميمز5` )\n★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n⌁︙CH : @Drago_dr"

		)
