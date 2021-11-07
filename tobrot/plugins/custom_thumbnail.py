"""ThumbNail utilities, © @AnyDLBot"""


import os

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image
from tobrot import DOWNLOAD_LOCATION


async def save_thumb_nail(client, message):
    thumbnail_location = os.path.join(DOWNLOAD_LOCATION, "thumbnails")
    thumb_image_path = os.path.join(
        thumbnail_location, str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("processing ...")
    if message.reply_to_message is not None:
        if not os.path.isdir(thumbnail_location):
            os.makedirs(thumbnail_location)
        download_location = thumbnail_location + "/"
        downloaded_file_name = await client.download_media(
            message=message.reply_to_message, file_name=download_location
        )
        # https://stackoverflow.com/a/21669827/4723940
        Image.open(downloaded_file_name).convert("RGB").save(downloaded_file_name)
        metadata = extractMetadata(createParser(downloaded_file_name))
        height = 0
        if metadata.has("height"):
            height = metadata.get("height")
        # resize image
        # ref: https://t.me/PyrogramChat/44663
        img = Image.open(downloaded_file_name)
        # https://stackoverflow.com/a/37631799/4723940
        # img.thumbnail((320, 320))
        img.resize((320, height))
        img.save(thumb_image_path, "JPEG")
        # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
        os.remove(downloaded_file_name)
        await ismgs.edit(
            "✔ 𝙲𝚞𝚜𝚝𝚘𝚖 𝚟𝚒𝚍𝚎𝚘 / 𝚏𝚒𝚕𝚎 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚜𝚊𝚟𝚎𝚍. "
            + "𝚃𝚑𝚒𝚜 𝚒𝚖𝚊𝚐𝚎 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚞𝚜𝚎𝚍 𝚒𝚗 𝚝𝚑𝚎 𝚞𝚙𝚕𝚘𝚊𝚍, 𝚝𝚒𝚕𝚕 /clearthumbnail."
        )
    else:
        await ismgs.edit("✗ 𝚁𝚎𝚙𝚕𝚢 𝚝𝚘 𝚊 𝚙𝚑𝚘𝚝𝚘 𝚝𝚘 𝚜𝚊𝚟𝚎 𝚌𝚞𝚜𝚝𝚘𝚖 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕")


async def clear_thumb_nail(client, message):
    thumbnail_location = os.path.join(DOWNLOAD_LOCATION, "thumbnails")
    thumb_image_path = os.path.join(
        thumbnail_location, str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("⏳𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐...")
    if os.path.exists(thumb_image_path):
        os.remove(thumb_image_path)
        await ismgs.edit("✔ 𝙲𝚞𝚜𝚝𝚘𝚖 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚌𝚕𝚎𝚊𝚛𝚎𝚍 𝚜𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢.")
    else:
        await ismgs.edit("✗ 𝙽𝚘𝚝𝚑𝚒𝚗𝚐 𝚝𝚘 𝚌𝚕𝚎𝚊𝚛.")
