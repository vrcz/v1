
import re
import base64
import asyncio
import logging
from telethon import events
from config import *
from asyncio import sleep
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("404")
logger.info("النشر التلقائي شغال الان استمتع ✓")

anti = False
async def bot(shadow, sleeptimet, chat, message, seconds):
    global anti
    anti = True
    while anti:
        if message.media:
            sent_message = await shadow.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await shadow.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.ا (\d+) (@?\S+)$"))
async def Hussein(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("اكتب الامر بشكل صحيح"
)
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    shadow = event.client
    global anti
    anti = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await shadow.get_entity(chat_username)
            await bot(shadow, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await event.reply(f" لا يمكن العثور على المجموعة   {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)

    
async def aljoker_allnshr(shadow, sleeptimet, message):
    global anti
    anti = True
    aljoker_chats = await shadow.get_dialogs()
    while anti:
        for chat in aljoker_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await shadow.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await shadow.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.قروبات (\d+)$"))
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("اكتب الامر بشكل صحيح")
    shadow = event.client
    global anti
    anti = True
    await aljoker_allnshr(shadow, sleeptimet, message)

super_groups = ["super", "سوبر"]
async def aljoker_supernshr(shadow, sleeptimet, message):
    global anti
    anti = True
    aljoker_chats = await shadow.get_dialogs()
    while anti:
        for chat in aljoker_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await shadow.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await shadow.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)

@shadow.on(events.NewMessage(outgoing=True, pattern='.ايقاف'))
async def stop_aljoker(event):
    global anti
    anti = False
    await event.edit("** تم ايقاف البوت ✅ ** ")
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def Hussein(event):
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        commands = """**
- اوامر بوت النشر⁴⁰⁴🔰

للنشر فقروب مع عدد الثواني 
.ا عدد الثواني رابط القروب
مثال:
.ا 300 @ccnre

للنشر في كل القروبات
.قروبات عدد الثواني
مثال: 
.قروبات 500

لكي توقف النشر 
.ايقاف


قناة البوت: @botnshr 📍
**"""

        await event.reply(file='https://telegra.ph/file/7e6d415ba12fa13a87aae.jpg', message=commands)
    elif event.pattern_match.group(1) == "فحص":
        test = "**البوت يعمل بنجاح ✅\n قناة البوت: @botnshr 📍**"
        await event.reply(file='https://telegra.ph/file/7e6d415ba12fa13a87aae.jpg', message=test)


@shadow.on(events.NewMessage(outgoing=True, pattern=r"\.قلب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️", "🖤", "💜", "🧡", "💛", "💚", "💙"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])

@shadow.on(events.NewMessage(outgoing=True, pattern=r"\.قلوب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️",
        "❤️🖤",
        "❤️🖤💜",
        "❤️🖤💜🧡",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛💚💙",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡",
        "❤️🖤💜",
        "❤️🖤",
        "💓"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])

print('تم تشغيل بوت النشر التلقائي  ')
shadow.run_until_disconnected()




import re
import base64
import asyncio
import logging
from telethon import events
from config import *
from asyncio import sleep
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("404")
logger.info("النشر التلقائي شغال الان استمتع ✓")

anti = False
async def bot(shadow, sleeptimet, chat, message, seconds):
    global anti
    anti = True
    while anti:
        if message.media:
            sent_message = await shadow.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await shadow.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.ا (\d+) (@?\S+)$"))
async def Hussein(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("اكتب الامر بشكل صحيح"
)
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    shadow = event.client
    global anti
    anti = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await shadow.get_entity(chat_username)
            await bot(shadow, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await event.reply(f" لا يمكن العثور على المجموعة   {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)

    
async def aljoker_allnshr(shadow, sleeptimet, message):
    global anti
    anti = True
    aljoker_chats = await shadow.get_dialogs()
    while anti:
        for chat in aljoker_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await shadow.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await shadow.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.قروبات (\d+)$"))
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("اكتب الامر بشكل صحيح")
    shadow = event.client
    global anti
    anti = True
    await aljoker_allnshr(shadow, sleeptimet, message)

super_groups = ["super", "سوبر"]
async def aljoker_supernshr(shadow, sleeptimet, message):
    global anti
    anti = True
    aljoker_chats = await shadow.get_dialogs()
    while anti:
        for chat in aljoker_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await shadow.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await shadow.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)

@shadow.on(events.NewMessage(outgoing=True, pattern='.ايقاف'))
async def stop_aljoker(event):
    global anti
    anti = False
    await event.edit("**᯽︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
@shadow.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def Hussein(event):
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        commands = """**
- اوامر بوت النشر⁴⁰⁴🔰

للنشر فقروب مع عدد الثواني 
.ا عدد الثواني رابط القروب
مثال:
.ا 300 @ccnre

للنشر في كل القروبات
.قروبات عدد الثواني
مثال: 
.قروبات 500

لكي توقف النشر 
.ايقاف


قناة البوت: @botnshr 📍
**"""

        await event.reply(file='https://telegra.ph/file/7e6d415ba12fa13a87aae.jpg', message=commands)
    elif event.pattern_match.group(1) == "فحص":
        test = "**البوت يعمل بنجاح ✅\n قناة البوت: @botnshr 📍**"
        await event.reply(file='https://telegra.ph/file/7e6d415ba12fa13a87aae.jpg', message=test)


@shadow.on(events.NewMessage(outgoing=True, pattern=r"\.قلب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️", "🖤", "💜", "🧡", "💛", "💚", "💙"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])

@shadow.on(events.NewMessage(outgoing=True, pattern=r"\.قلوب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️",
        "❤️🖤",
        "❤️🖤💜",
        "❤️🖤💜🧡",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛💚💙",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡",
        "❤️🖤💜",
        "❤️🖤",
        "💓"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])

print('تم تشغيل بوت النشر التلقائي  ')
shadow.run_until_disconnected()



