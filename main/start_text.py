from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="This is DarkLord. I am not interested in replying..."
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("Find-Hub", url="https://t.me/find_hub")
        ],[
        InlineKeyboardButton("Updates", url="https://t.me/findhubupdates")
    ]])
    if msg.from_user.id != ADMIN:
        await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
        return
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"Hi {msg.from_user.mention} bro, Sorry to say I am busy cannot help you."                                     
    button= [[
        InlineKeyboardButton("Find-Hub", url="https://t.me/find_hub")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt=f"I don't think you need help Oni'chan"
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"I am my own Master"  
    Origin="My origin is earth"
    More =f"<b> NOTHING TO KNOW MORE UWU </b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


