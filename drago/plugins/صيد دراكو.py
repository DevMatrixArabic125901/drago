import random
import requests
from telethon import events
from fake_useragent import UserAgent
from drago import dragoiq
from drago import BOTLOG_CHATID
client = dragoiq
@dragoiq.on(events.NewMessage(pattern=r"^\.خماسي (\d+)$"))
async def Ahmed(event):
    if event.sender_id == bot.uid:
        await event.edit("** ⌁︙ يتم الان صيد يوزرات خماسية اذهب الى مجموعة الاشعارات **")
    drago = int(event.pattern_match.group(1)) 
    xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
    xa = "1234567890"
    while drago > 0:
        us = ''.join(random.choice(xu) for _ in range(1))
        ua = ''.join(random.choice(xa) for _ in range(1))
        xn = ''.join(random.choice(xa) for _ in range(1))
        us1 = ua + us + us + xn + us
        us2 = us + xn + us + ua + us
        us3 = us + ua + us + xn + us
        us4 = us + xn + us + us + ua
        d = [us1, us2, us3, us4]
        drago = random.choice(d)
        url = "https://t.me/" + drago
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        session = requests.Session()
        response = session.get(url, headers=headers)
        if (
            response.text.find(
                'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
            )
            >= 0
        ):
            drago -= 1
            try:
                await client.send_message(BOTLOG_CHATID,
                    f"‹ يوزرات تلي خماسية  ✓\n────────────\n‹ صدتلك يوزر : @{drago}\n "
                )
            except:
                pass
@dragoiq.on(events.NewMessage(pattern=r"^\.ثلاثي (\d+)$"))
async def Ahmed(event):
    if event.sender_id == bot.uid:
        await event.edit("** ⌁︙ يتم الان صيد يوزرات ثلاثيه اذهب الى مجموعة الاشعارات **")
    drago = int(event.pattern_match.group(1)) 
    xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
    xn = "1234567890"
    xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
    while drago > 0:
        us = str(''.join(random.choice(xu)for i in range(1)))
        u2s = str(''.join(random.choice(xu)for i in range(1)))
        u1s = str(''.join(random.choice(xu)for i in range(1)))
        un = str(''.join(random.choice(xn)for i in range(1)))
        u1n = str(''.join(random.choice(xn)for i in range(1)))
        ua = str(''.join(random.choice(xa)for i in range(1)))
        u1= str(us)+"_"+str(un)+"_"+str(u1s)
        u2= str(us)+"_"+str(u1s)+"_"+str(un)
        u3= str(us)+"_"+str(u1n)+"_"+str(un)
        u4= str(us)+"_"+str(u1s)+"_"+str(u2s)
        S = [u1,u2,u3,u4]
        drago = random.choice(S)
        url = "https://t.me/" + drago
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        session = requests.Session()
        response = session.get(url, headers=headers)
        if (
            response.text.find(
                'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
            )
            >= 0
        ):
            drago -= 1
            try:
                await client.send_message(BOTLOG_CHATID,
                    f"‹ يوزرات تلي ثلاثية  ✓\n────────────\n‹ صدتلك يوزر : @{drago}\n "
                )
            except:
                pass
@dragoiq.on(events.NewMessage(pattern=r"^\بوتات(\d+)$"))
async def usernameAldrago6(event):
    if event.sender_id == bot.uid:
        await event.edit("** ⌁︙ يتم الآن صيد يوزرات للبوتات اذهب الى مجموعة الاشعارات **")
    drago = int(event.pattern_match.group(1))
    xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
    xn = "1234567890"
    xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
    
    while drago > 0:
        us = ''.join(random.choice(xu) for i in range(1))
        u2s = ''.join(random.choice(xu) for i in range(1))
        u1s = ''.join(random.choice(xu) for i in range(1))
        un = ''.join(random.choice(xn) for i in range(1))
        u1n = ''.join(random.choice(xn) for i in range(1))
        ua = ''.join(random.choice(xa) for i in range(1))
        
        u1 = us + u1s + u2s + un + "bot"
        u2 = us + un + u2s + u1s + "bot"
        u3 = us + u1s + un + u2s + "bot"
        g = [u1, u2, u3]
        
        drago = random.choice(g)
        url = "https://t.me/" + drago
        ua = UserAgent()
        
        headers = {
            "User-Agent": ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        
        session = requests.Session()
        response = session.get(url, headers=headers)
        
        if (
            response.text.find(
                'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
            ) >= 0
        ):
            drago -= 1
            try:
                await client.send_message(BOTLOG_CHATID,
                    f"‹ يوزرات تلي بوتات  ✓\n────────────\n‹ صدتلك يوزر : @{drago}\n "
                )
            except:
                pass
@dragoiq.on(events.NewMessage(pattern=r"^\.سداسي (\d+)$"))
async def usernameAldrago6(event):
    if event.sender_id == bot.uid:
        await event.edit("** ⌁︙ يتم الان صيد يوزرات سداسية اذهب الى مجموعة الاشعارات **")
    drago = int(event.pattern_match.group(1))
    xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
    xn = "1234567890"
    xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
    
    while drago > 0:
        us = ''.join(random.choice(xu) for i in range(1))
        un = ''.join(random.choice(xn) for i in range(1))
        ua = ''.join(random.choice(xa) for i in range(1))
        
        h1 = us + un + us + us + us + us
        h2 = us + us + un + us + us + us
        h3 = us + us + us + un + us + us
        h4 = us + us + us + us + un + us
        h5 = us + us + us + us + us + un
        
        j = [h1, h2, h3, h4, h5]
        drago = random.choice(j)
        
        url = "https://t.me/" + drago
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        
        session = requests.Session()
        response = session.get(url, headers=headers)
        
        if (
            response.text.find(
                'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
            ) >= 0
        ):
            drago -= 1
            try:
                await client.send_message(BOTLOG_CHATID,
                    f"‹ يوزرات تلي سداسيه  ✓\n────────────\n‹ صدتلك يوزر : @{drago}\n "
                )
            except:
                pass
@dragoiq.on(events.NewMessage(pattern=r"^\.ثلاثي_(\w)$"))
async def Ahmed(event):
    if event.sender_id == bot.uid:
        await event.edit("** ⌁︙ يتم الان صيد يوزرات ثلاثيه بأختيارك اذهب الى مجموعة الاشعارات **")
    drago = 10
    start_letter = event.pattern_match.group(1).upper()  
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    aldrago_usernames = []
    while drago > 0:
        v1 = start_letter
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc1) for _ in range(1)))
        username = f"{v1}_{v2}_{v3}"
        if not await Ya_Ali_Mdd(username):
            aldrago_usernames.append(username)
            drago -= 1
    if aldrago_usernames:
        usernames_text = "\n".join([f"@{username}" for username in aldrago_usernames])
        await client.send_message(BOTLOG_CHATID, f"**⌁︙ تم إنشاء {len(aldrago_usernames)} يوزرات ثلاثيه جديدة:**\n\n{usernames_text}")

async def Ya_Ali_Mdd(username):
    try:
        entity = await dragoiq.get_entity(username)
        if entity and hasattr(entity, 'username'):
            return True
        else:
            return False
    except Exception:
        return False
