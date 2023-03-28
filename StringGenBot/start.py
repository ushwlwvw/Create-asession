from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID

def filter(cmd: str):

    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))

async def start(bot: Client, msg: Message):

    me2 = (await bot.get_me()).mention

    await bot.send_message(

        chat_id=msg.chat.id,

        text=f"""**مرحبا** {msg.from_user.mention},

انا بوت {me2},

استطيع استخراج جلسات على 4 مكاتب

 مكتوب بلغة بايثون

• مطور البوت • 🖤 ʙʏ : [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](tg://user?id={OWNER_ID}) !""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(text="✠ استخراج جلسات  ✠", callback_data="generate")

                ],

                [

                    InlineKeyboardButton("✠ السورس ✠️", url="https://t.me/aaaalqp"),

                    InlineKeyboardButton("「 𝗗𝗲𝘃𝗲𝗟𝗼𝗣𝗲𝗥 」", user_id=OWNER_ID)

                ]

            ]

        ),

        disable_web_page_preview=True,

    )

  
