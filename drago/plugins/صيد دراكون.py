

import random

import requests

import time

from asyncio import sleep

import telethon

from telethon.sync import functions

from user_agent import generate_user_agent



from drago import dragoiq



a = "qwertyuiopassdfghjklzxcvbnm"

b = "1234567890"

e = "qwertyuiopassdfghjklzxcvbnm1234567890"



trys, trys2 = [0], [0]

isclaim = ["off"]

isauto = ["off"]





def check_user(username):

    url = "https://t.me/" + str(username)

    headers = {

        "User-Agent": generate_user_agent(),

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

        "Accept-Encoding": "gzip, deflate, br",

        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",

    }



    response = requests.get(url, headers=headers)

    if (

        response.text.find(

            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'

        )

        >= 0

    ):

        return True

    else:

        return False





def gen_user(choice):

    if choice == "ثلاثيات":

        c = random.choices(a)

        d = random.choices(b)

        s = random.choices(e)

        f = [c[0], "_", d[0], "_", s[0]]

        username = "".join(f)



    elif choice == "خماسيات":

        c = d = random.choices(a)

        d = random.choices(b)

        f = [c[0], c[0], c[0], c[0], d[0]]

        random.shuffle(f)

        username = "".join(f)



    elif choice == "خماسي حرفين":

        c = d = random.choices(a)

        d = random.choices(e)

        f = [c[0], d[0], c[0], c[0], d[0]]

        random.shuffle(f)

        username = "".join(f)



    elif choice == "سداسيات":

        c = d = random.choices(a)

        d = random.choices(e)

        f = [c[0], c[0], c[0], c[0], c[0], d[0]]

        random.shuffle(f)

        username = "".join(f)



    elif choice == "سداسي حرفين":

        c = d = random.choices(a)

        d = random.choices(b)

        f = [c[0], d[0], c[0], c[0], c[0], d[0]]

        random.shuffle(f)

        username = "".join(f)



    elif choice == "سباعيات":

        c = d = random.choices(a)

        d = random.choices(b)

        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]

        random.shuffle(f)

        username = "".join(f)



    elif choice == "بوتات":

        c = random.choices(a)

        d = random.choices(e)

        s = random.choices(e)

        f = [c[0], s[0], d[0]]

        username = "".join(f)

        username = username + "bot"



    elif choice == "تيست":

        c = d = random.choices(a)

        d = random.choices(b)

        f = [c[0], d[0], c[0], d[0], d[0], c[0], c[0], d[0], c[0], d[0]]

        random.shuffle(f)

        username = "".join(f)

    else:

        raise ValueError("Invalid choice for username generation.")

    return 



@dragoiq.zed_cmd(pattern="النوع")

async def cmd(dragolll):

    await edit_or_reply(dragolll, dragoType_cmd)



@dragoiq.zed_cmd(pattern="صيد (.*)")

async def hunterusername(event):

    choice = str(event.pattern_match.group(1))

    replly = await event.get_reply_message()

    if choice not in ("ثلاثيات", "خماسيات", "خماسي حرفين", "سداسيات", "سداسي حرفين", "سباعي", "بوتات"): 

        return await event.edit(f"**- عـذرًا عـزيـزي\n- لايوجـد نوع** {choice} \n**- لـ عرض الانواع أرسـل (**`.النوع`**)**")



    try:

        if replly and replly.text.startswith('@'): 

            ch = replly.text

            await event.edit(f"**- تم بـدء الصيد .. بنجـاح ✓**\n**- النـوع** {choice} \n**- على القنـاة** {ch} \n**- لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**- لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

        else:

            ch = await dragoiq(

                functions.channels.CreateChannelRequest(

                    title="⎉ صيـد دراكـو العـربي - DraGo Arab",

                    about="This channel to hunt username by - @src_dra ",

                )

            )

            ch = ch.updates[1].channel_id

            await event.edit(f"**- تم بـدء الصيد .. بنجـاح ✓**\n**- علـى النـوع** {choice} \n**- لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**- لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

    except Exception as e:

        await dragoiq.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

        zedmod = False



    isclaim.clear()

    isclaim.append("on")

    zedmod = True

    while zedmod: 

        username = gen_user(choice)

        isav = check_user(username)

        if isav == True:

            try:

                await dragoiq(

                    functions.channels.UpdateUsernameRequest(

                        channel=ch, username=username

                    )

                )

                await event.client.send_message(

                    event.chat_id,

                    f"- Done : @{username} ✓\n- By : @src_dra \n- Hunting Log {trys[0]}",

                )

                await event.client.send_message(

                    "@UxUeU", f"- Done : @{username} ✓\n- By : @src_dra \n- Hunting Log {trys[0]}",

                )

                zedmod = False

                break

            except telethon.errors.FloodWaitError as e: 

                await sleep(e.seconds)

                pass

            except telethon.errors.rpcerrorlist.UsernameInvalidError:

                pass

            except Exception as baned:

                if "(caused by UpdateUsernameRequest)" in str(baned):

                    pass

            except telethon.errors.FloodError as e:

                await dragoiq.send_message(

                    event.chat_id,

                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",

                )

                zedmod = False

                break

            except Exception as eee:

                if "the username is already" in str(eee):

                    pass

                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):

                    pass

                else:

                    await dragoiq.send_message(

                        event.chat_id,

                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",

                    )

                    zedmod = False

                    break

        else:

            pass

        trys[0] += 1



    isclaim.clear()

    isclaim.append("off")

    trys[0] = 0

    return await event.client.send_message(event.chat_id, "**- تم الانتهاء من الصيد .. بنجـاح ✓**")





@dragoiq.zed_cmd(pattern="تثبيت (.*)")

async def _(event):

    drago = str(event.pattern_match.group(1))

    if not drago.startswith('@'): 

        return await event.edit("**- عـذرًا عـزيـزي المدخـل خطـأ ❌**\n**- استخـدم الامـر كالتالـي**\n**- أرسـل (**`.تثبيت`** + اليـوزر)**")

    try:

        ch = await dragoiq(

            functions.channels.CreateChannelRequest(

                title="تثبيت دراكـو العـربي - DraGo Arab",

                about="تم تثبيت اليـوزر بواسطـة سـورس دراكـو - @src_dra ",

            )

        )

        ch = ch.updates[1].channel_id

        await event.edit(f"**- تم بـدء التثبيت .. بنجـاح ✓**\n**- اليـوزر المثبت ( {drago} )**\n**- لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")

    except Exception as e:

        await dragoiq.send_message(

            event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"

        )

        swapmod = False



    isauto.clear()

    isauto.append("on")

    username = drago.replace("@", "")  

    swapmod = True

    while swapmod:

        isav = check_user(username)

        if isav == True:

            try:

                await dragoiq(

                    functions.channels.UpdateUsernameRequest(

                        channel=ch, username=username

                    )

                )

                await event.client.send_message(

                    event.chat_id,

                    f"- Done : @{username} \n- Save: ❲ Channel ❳\n- By : @src_dra \n- Hunting Log {trys2[0]}",

                )

                await event.client.send_message(

                    "@UxUeU",

                    f"- Done : @{username} \n- Save: ❲ Channel ❳\n- By : @src_dra \n- Hunting Log {trys2[0]}",

                )

                swapmod = False

                break

            except telethon.errors.rpcerrorlist.UsernameInvalidError:

                await event.client.send_message(

                    event.chat_id, f"**المعرف @{username} غير صالح ؟!**"

                )

                swapmod = False

                break

            except telethon.errors.FloodError as e:

                await dragoiq.send_message(

                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."

                )

                swapmod = False

                break

            except Exception as eee:

                await dragoiq.send_message(

                    event.chat_id,

                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",

                )

                swapmod = False

                break

        else:

            pass

        trys2[0] += 1



    isclaim.clear()

    isclaim.append("off")

    trys2[0] = 0

    return await dragoiq.send_message(event.chat_id, "**- تم الانتهاء من التثبيت .. بنجـاح ✓**")





@dragoiq.zed_cmd(pattern="ثبت (.*)")

async def _(event): 

    drago = str(event.pattern_match.group(1))

    if not drago.startswith('@'): 

        return await event.edit("**- عـذرًا عـزيـزي المدخـل خطـأ ❌**\n**- استخـدم الامـر كالتالـي**\n**- أرسـل (**`.ثبت`** + اليـوزر)**")

    await event.edit(f"**- تم بـدء التثبيت .. بنجـاح ✓**\n**- اليـوزر المثبت ( {drago} )**\n**- لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")

    isouto.clear()

    isouto.append("on")

    username = drago.replace("@", "")  

    swapmod = True

    while swapmod:

        isav = checker_user(username)

        if isav == True:

            try: 

                await dragoiq(functions.account.UpdateUsernameRequest(username=username))

                await event.client.send_message(

                    event.chat_id,

                    f"- Done : @{username} \n- Save: ❲ Account ❳\n- By : @src_dra \n- Hunting Log {trys2[0]}",

                )

                await event.client.send_message(

                    "@UxUeU",

                    f"- Done : @{username} \n- Save: ❲ Account ❳\n- By : @src_dra \n- Hunting Log {trys2[0]}",

                )

                swapmod = False

                break

            except telethon.errors.rpcerrorlist.UsernameInvalidError:

                pass

            except telethon.errors.FloodError as e:

                await dragoiq.send_message(

                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."

                )

                swapmod = False

                break

            except Exception as eee:

                await dragoiq.send_message(

                    event.chat_id,

                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",

                )

                swapmod = False

                break

        else:

            pass

        trys2[0] += 1



    isclaim.clear()

    isclaim.append("off")

    trys2[0] = 0

    return await dragoiq.send_message(event.chat_id, "**- تم الانتهاء من التثبيت .. بنجـاح ✓**")







@dragoiq.zed_cmd(pattern="حالة الصيد")

async def _(event):

    if "on" in isclaim:

        await event.edit(f"**- الصيد وصل لـ({trys[0]}) من المحـاولات**")

    elif "off" in isclaim:

        await event.edit("**- لا توجد عمليـة صيد جاريـة حـالـيًا!**")

    else:

        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")





@dragoiq.zed_cmd(pattern="حالة التثبيت")

async def _(event):

    if "on" in isauto:

        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")

    elif "off" in isauto:

        await event.edit("**- لا توجد عمليـة تثبيث جاريـة حـالـيًا!**")

    else:

        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")





@dragoiq.zed_cmd(pattern="ايقاف الصيد")

async def _(event): 

    if "on" in isclaim:

        isclaim.clear()

        isclaim.append("off")

        trys[0] = 0

        return await event.edit("**- تم إيقـاف عمليـة الصيد .. بنجـاح ✓**")

    elif "off" in isclaim:

        return await event.edit("**- لا تـوجـد عـملية صـيد جاريـة حـالـيًا .**")

    else:

        return await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")





@dragoiq.zed_cmd(pattern="ايقاف التثبيت")

async def _(event): 

    if "on" in isauto:

        isauto.clear()

        isauto.append("off")

        trys2[0] = 0

        return await event.edit("**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")

    elif "off" in isauto:

        return await event.edit("**لا توجـد عمـليـة تثبيت جاريـة حـالـيًا .**")

    else:

        return await event.edit("**-لقد حدث خطأ ما وتوقف الامر لديك**")
