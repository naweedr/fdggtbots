import logging
import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import BOT_USERNAME, UPDATES_CHANNEL
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
UPDATES_CHANNEL = UPDATES_CHANNEL


@Client.on_message(filters.incoming & filters.command(['start', 'start@{BOT_USERNAME}']))
def _start(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               client.send_message(
                   chat_id=message.chat.id,
                   text="ببخشید قربان، شما ممنوع الکار هستید از من استفاده کنید. با من تماس بگیرید [Support Group](https://t.me/Music_naik_group).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            client.send_message(
                chat_id=message.chat.id,
                text="**لطفا برای استفاده از این ربات به کانال به روز رسانی های من بپیوندید!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("کانال", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            client.send_message(message.chat.id,
                text="**سلام [{}](tg://user?id={})**\n__من می توانم موسیقی را در چت صوتی گروه های تلگرام پخش کنم**".format(message.from_user.first_name, message.from_user.id),
	        reply_markup=InlineKeyboardMarkup(
                    [
                        [   
                           InlineKeyboardButton("کانال 📢", url="https://t.me/Music_naik"),
                           InlineKeyboardButton("گروه پشتیبانی 👥", url="https://t.me/Music_naik_group")
                      ],
                     [
                           InlineKeyboardButton("🧑‍💻سازنده🧑‍💻", url="https://t.me/ye_nik")
                     ],
                     [
                           InlineKeyboardButton("دستورات 📚", callback_data="cbcmds")
                     ]
                 ]
             ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
            return
    client.send_message(message.chat.id,
        text="**سلام [{}](tg://user?id={})**\n__من می توانم موسیقی را در چت صوتی گروه های تلگرام پخش کنم**".format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
		[
                           InlineKeyboardButton("کانال 📢", url="https://t.me/Music_naik"),
                           InlineKeyboardButton("گروه پشتیبانی 👥", url="https://t.me/Music_naik_group")
                ],
                [
                           InlineKeyboardButton("🧑‍💻سازنده🧑‍💻", url="https://t.me/ye_nik")
                ],
                [
                           InlineKeyboardButton("دستورات 📚", callback_data="cbcmds")
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**ربات آنلاین است ✅**",
        reply_markup=InlineKeyboardMarkup(
            [[
                           InlineKeyboardButton("کانال 📢", url="https://t.me/Music_naik"),
                           InlineKeyboardButton("گروه پشتیبانی 👥", url="https://t.me/Music_naik_group")
            ],
            [
            
            ]]
        )
    )


@Client.on_message(filters.command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text=f"""<b>✨ **خوش آمدید {query.message.from_user.mention}** \n

__× ابتدا مرا به گروه خود اضافه کنید..
× با تمام مجوزها مرا به عنوان مدیر گروه خود معرفی کنید..__

**🏷 دستورات مشترک.**

• `/play` : __از طریق یوتیوب پخش می شود__
• `/dplay` : __پخش از طریق Deezer__
• `/splay` : __پخش از طریق Jivo__
• `/playlist` : __نمایش لیست در حال پخش__
• `/current` : __نمایش در حال پخش__

• `/song` : __Get The Song From YouTube__
• `/vid` : __Get The Video From YouTube__
• `/deezer` : __download songs you want quickly via deezer__
• `/saavn` : __download songs you want quickly via saavn__
• `/search` : __(Get YouTube Search Query)__

**🏷 دستورات مدیریت گروه.**

• `/skip` : __موسیقی را رد می کند__
• `/pause` : __توقف پخش موسیقی__
• `/resume` : __پخش موسیقی را از سر بگیرید__
• `/end` : __پخش موسیقی را متوقف می کند__
• `/reload` : __بارگیری مجدد لیست مدیریت__
• `/userbotjoin` : __دستیار به گروه می پیوندد__
• `/userbotleave` : __دستیار از گروه خارج می شود.__
</b>""",
        reply_markup=InlineKeyboardMarkup(
              [[
                           InlineKeyboardButton("کانال 📢", url="https://t.me/Music_naik"),
                           InlineKeyboardButton("گروه پشتیبانی 👥", url="https://t.me/Music_naik_group")
              ],[
              InlineKeyboardButton("برگشت به صفحه اصلی 🏡", callback_data="cbstart")
              ]]
          )
      )
