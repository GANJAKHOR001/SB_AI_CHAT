import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from ChatBot import app
from pyrogram.errors import RPCError
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode
from config import LOGGER_ID
photo = [

"https://telegra.ph/file /1949480f01355b4e87d26.jpg",

"https://telegra.ph/file /3ef2cc0ad2bc548bafb30.jpg",

"https://telegra.ph/file /a7d663cd2de689b811729.jpg",

"https://telegra.ph/file /6f19dc23847f5b005e922.jpg",

"https://telegra.ph/file /2973150dd62fd27a3a6ba.jpg", ]

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        chat_id = message.chat.id
        chat_title = message.chat.title
        added_by = message.from_user.mention if message.from_user else "Unknown User"
        chatusername = f"@{message.chat.username}" if message.chat.username else "Private Chat"

        try:
            invite_link = await client.export_chat_invite_link(chat_id)
        except Exception:
            invite_link = "Not Available"

        await add_chat(chat_id, chat_title)

        await message.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("ᴧᴅᴅ ϻє ʙᴧʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"),
                    InlineKeyboardButton("ᴊσɪη sᴜᴘᴘσʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ])
        )

        log_msg = (
            f"<b>✦ ʙᴏᴛ #ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɢʀᴏᴜᴘ</b>\n\n"
            f"**⚘ ɢʀᴏᴜᴘ ɴᴀᴍᴇ :** {chat_title}\n"
            f"**⚘ ɢʀᴏᴜᴘ ɪᴅ :** {chat_id}\n"
            f"**⚘ ᴜsᴇʀɴᴀᴍᴇ :** {chatusername}\n"
            f"**⚘ ɢʀᴏᴜᴘ ʟɪɴᴋ : [ᴛᴀᴘ ʜᴇʀᴇ]({invite_link})**\n"
            f"**⚘ ᴀᴅᴅᴇᴅ ʙʏ :** {added_by}"
        )

        await app.send_photo(
            LOGGER_GROUP_ID,
            photo=random.choice(IMG),
            caption=log_msg,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ɢʀᴏᴜᴘ ʟɪɴᴋ", url=invite_link if invite_link != "Not Available" else "https://t.me/TNJBotSupport")]
            ])
        )


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    if (await client.get_me()).id == message.left_chat_member.id:
        chat_id = message.chat.id
        chat_title = message.chat.title
        remove_by = message.from_user.mention if message.from_user else "Unknown User"

        await chatsdb.delete_one({"chat_id": chat_id})

        left_msg = (
            f"<b>✦ ʙᴏᴛ #ʟᴇғᴛ ᴀ ɢʀᴏᴜᴘ</b>\n\n"
            f"**⚘ ɢʀᴏᴜᴘ ɴᴀᴍᴇ :** {chat_title}\n"
            f"**⚘ ɢʀᴏᴜᴘ ɪᴅ :** {chat_id}\n"
            f"**⚘ ʀᴇᴍᴏᴠᴇᴅ ʙʏ :** {remove_by}"
        )

        await app.send_photo(
            LOGGER_GROUP_ID,
            photo=random.choice(IMG),
            caption=left_msg,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("sᴇᴇ ɢʀᴏᴜᴘ", url=f"https://t.me/{message.chat.username}" if message.chat.username else "https://t.me/TNJBOTSUPPORT")]
            ])
        )