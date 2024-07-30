from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\n𝚃𝙷𝙸𝚂 𝙸𝚂 𝙰𝙽 𝚂𝚃𝚁𝙸𝙽𝙶 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁 𝙱𝙾𝚃 𝙷𝙴𝚁𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙶𝙴𝙽𝙴𝚁𝙰𝚃 𝚂𝚃𝚁𝙸𝙽𝙶 𝚂𝙴𝚂𝚂𝙸𝙾𝙽.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
