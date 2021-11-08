#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) gautamajay52 | Shrimadhav U K

import asyncio
import logging
import math
import os
import re
import subprocess
import time
from datetime import datetime
from pathlib import Path

from pyrogram import Client, filters
from tobrot import DOWNLOAD_LOCATION, LOGGER, TELEGRAM_LEECH_UNZIP_COMMAND
from tobrot.helper_funcs.create_compressed_archive import unzip_me, get_base_name
from tobrot.helper_funcs.display_progress import Progress
from tobrot.helper_funcs.upload_to_tg import upload_to_gdrive


async def down_load_media_f(client, message):
    user_command = message.command[0]
    user_id = message.from_user.id
    LOGGER.info(user_id)
    mess_age = await message.reply_text("⏳𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐...", quote=True)
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    if message.reply_to_message is not None:
        start_t = datetime.now()
        download_location = str(Path().resolve()) + "/"
        c_time = time.time()
        prog = Progress(user_id, client, mess_age)
        try:
            the_real_download_location = await client.download_media(
                message=message.reply_to_message,
                file_name=download_location,
                progress=prog.progress_for_pyrogram,
                progress_args=("𝚃𝚛𝚢 𝚃𝚘 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍", c_time),
            )
        except Exception as g_e:
            await mess_age.edit(str(g_e))
            LOGGER.error(g_e)
            return
        end_t = datetime.now()
        ms = (end_t - start_t).seconds
        LOGGER.info(the_real_download_location)
        await asyncio.sleep(10)
        if the_real_download_location:
            await mess_age.edit_text(
                f"🥳𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚍 𝚃𝚘 <code>{the_real_download_location}</code> 𝙸𝚗 <u>{ms}</u> 𝚜𝚎𝚌𝚘𝚗𝚍𝚜"
            )
        else:
            await mess_age.edit_text("😔𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙲𝚊𝚗𝚌𝚎𝚕𝚕𝚎𝚍 𝚘𝚛 𝚜𝚘𝚖𝚎 𝚎𝚛𝚛𝚘𝚛 𝚑𝚊𝚙𝚙𝚎𝚗𝚎𝚍")
            return
        the_real_download_location_g = the_real_download_location
        if user_command == TELEGRAM_LEECH_UNZIP_COMMAND.lower():
            try:
                check_ifi_file = get_base_name(the_real_download_location)
                file_up = await unzip_me(the_real_download_location)
                if os.path.exists(check_ifi_file):
                    the_real_download_location_g = file_up
            except Exception as ge:
                LOGGER.info(ge)
                LOGGER.info(
                    f"😑𝙲𝚊𝚗'𝚝 𝚎𝚡𝚝𝚛𝚊𝚌𝚝 {os.path.basename(the_real_download_location)}, 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚝𝚑𝚎 𝚜𝚊𝚖𝚎 𝚏𝚒𝚕𝚎"
                )
        await upload_to_gdrive(the_real_download_location_g, mess_age, message, user_id)
    else:
        await mess_age.edit_text(
            "𝚁𝚎𝚙𝚕𝚢 𝚝𝚘 𝚊 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙼𝚎𝚍𝚒𝚊, 𝚝𝚘 𝚞𝚙𝚕𝚘𝚊𝚍 𝚝𝚘 𝚝𝚑𝚎 𝙲𝚕𝚘𝚞𝚍 𝙳𝚛𝚒𝚟𝚎."
        )


async def download_tg(client, message):
    user_id = message.from_user.id
    LOGGER.info(user_id)
    mess_age = await message.reply_text("⏳𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐...", quote=True)
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    if message.reply_to_message is not None:
        start_t = datetime.now()
        download_location = str(Path("./").resolve()) + "/"
        c_time = time.time()
        prog = Progress(user_id, client, mess_age)
        try:
            the_real_download_location = await client.download_media(
                message=message.reply_to_message,
                file_name=download_location,
                progress=prog.progress_for_pyrogram,
                progress_args=("𝚃𝚛𝚢 𝚃𝚘 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍", c_time),
            )
        except Exception as g_e:
            await mess_age.edit(str(g_e))
            LOGGER.error(g_e)
            return
        end_t = datetime.now()
        ms = (end_t - start_t).seconds
        LOGGER.info(the_real_download_location)
        await asyncio.sleep(5)
        if the_real_download_location:
            await mess_age.edit_text(
                f"🥳𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚍 𝚃𝚘 <code>{the_real_download_location}</code> 𝙸𝚗 <u>{ms}</u> 𝚜𝚎𝚌𝚘𝚗𝚍𝚜"
            )
        else:
            await mess_age.edit_text("😔 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙲𝚊𝚗𝚌𝚎𝚕𝚕𝚎𝚍 𝚘𝚛 𝚜𝚘𝚖𝚎 𝚎𝚛𝚛𝚘𝚛 𝚑𝚊𝚙𝚙𝚎𝚗𝚎𝚍")
            return
    return the_real_download_location, mess_age
