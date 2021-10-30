from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import config
from config import BOT_USERNAME
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ابتدا من را به عنوان ادمین گروه خود اضافه کنید</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Music"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"طبق درخواست شما به اینجا ملحق شدم")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>کمک کننده در حال حاضر در چت شما</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 خطای Flood Wait 🛑 \n کاربر {user.first_name} نتوانست به گروه شما بپیوندد به دلیل درخواست‌های پیوستن زیاد برای کاربر ربات! اطمینان حاصل کنید که کاربر در گروه ممنوع نشده است."
            f"\n\nOr به صورت دستی @{BOT_USERNAME} را به گروه خود اضافه کنید و دوباره امتحان کنید</b>",
        )
        return
    await message.reply_text(
            "<b>ربات کاربر کمکی به چت شما پیوست</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>کاربر نتوانست گروه شما را ترک کند! ممکن است سیلابی باشد."
            "\n\nOr به صورت دستی مرا از گروه خود بیرون بیاورید</b>",
        )
        return
