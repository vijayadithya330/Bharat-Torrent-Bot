#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging

import pyrogram
from tobrot import AUTH_CHANNEL, LOGGER


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    # channel_id = str(AUTH_CHANNEL)[4:]
    # message_id = 99
    # display the /help

    await message.reply_text(
        """<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʙʜᴀʀᴀᴛ ᴛᴏʀʀᴇɴᴛ!\n\n ❯ <a href="https://telegra.ph/Bharat-Torrent-09-18"> ᴄʟɪᴄᴋ ᴛᴏ ʟᴇᴀʀɴ ɢʀᴏᴜᴘ ʀᴜʟᴇꜱ.</a>\n ❯ <a href="https://telegra.ph/-10-02-1238">ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ꜰɪʟᴇꜱ?</a>\n ❯ <a href="https://t.me/BharatTorrentPro/10">ᴄʟɪᴄᴋ ᴛᴏ ᴡᴀᴛᴄʜ ᴅᴇᴍᴏ ᴠɪᴅᴇᴏ</a> </b>""",
        disable_web_page_preview=True,
    )
