@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    try:
        chat = message.chat
        try:
            link = await app.export_chat_invite_link(chat.id)
        except Exception:
            link = "Unavailable"

        me = await app.get_me()
        for member in message.new_chat_members:
            if member.id == me.id:
                count = await app.get_chat_members_count(chat.id)
                msg = (
                    f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                    f"____________________________________\n\n"
                    f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {chat.title}\n"
                    f"🍂 ᴄʜᴀᴛ ɪᴅ: {chat.id}\n"
                    f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{chat.username}\n"
                    f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                    f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                    f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
                )
                await app.send_photo(LOGGER_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("sᴇᴇ ɢʀᴏᴜᴘ👀", url=link if link != "Unavailable" else "https://t.me/")]
                ]))
    except Exception as e:
        print(f"[ERROR] join_watcher failed: {e}")