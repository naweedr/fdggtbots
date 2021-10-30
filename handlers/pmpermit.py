from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"😍با سلام خدمت کاربران گرامی😍\n 🎶ربات موزیک نایک مخصوص موزیکال گروه میباشد🎵\n 💰هزینه شارژ ماهیانه 20/000تومان💰\n 👥جهت خرید و نصب ربات به ایدی زیر پیام ارسال فرماید👥\n 🆔 @ye_nik\n\n ✅ مبلغ رو با استفاده ازدرگاه زیر\n zarinp.al/@sir_hasan\n\n پرداخت یا کارت به کارت\n 💳6037697567147845\n\n ❤️‍🔥ساخت تیم فدرال نیک ❤️‍🔥")
  return                        
