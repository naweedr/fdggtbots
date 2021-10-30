from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import BOT_USERNAME
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery



@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**گروه موسیقی ربات: منوی راهنما**

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
            [
                [
                    InlineKeyboardButton(text="گروه پشتیبانی 👥", url="https://t.me/Music_naik_group"),
                    InlineKeyboardButton(text="کانال 📢", url=f"https://t.me/Music_naik")
                ],
                [
                    InlineKeyboardButton(
                        "برگشت به صفحه اصلی 🏡", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
    
    
    
@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        text="**سلام [{}](tg://user?id={})**\n__من می توانم موسیقی را در چت صوتی گروه های تلگرام پخش کنم**".format(message.from_user.first_name, message.from_user.id),
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(text="گروه پشتیبانی 👥", url="https://t.me/Music_naik_group"),
                    InlineKeyboardButton(text="کانال 📢", url=f"https://t.me/Music_naik")
                ],[
                    InlineKeyboardButton("خرید ربات", url="https://t.me/Music_naik_group"),
                    InlineKeyboardButton("سازنده", url="https://t.me/ye_nik")	
                ],[
                    InlineKeyboardButton("دستورات 📚", callback_data="cbcmds")
                ]
            ]
        ),
     disable_web_page_preview=True
    )
