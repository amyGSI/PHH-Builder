# Thanks to github.com/usernein

import os
import pyrogram


rom = os.getenv('ROM_NAME')
da = os.getenv('DOWNLOAD_A')
dab = os.getenv('DOWNLOAD_AB')

with pyrogram.Client('bot', os.getenv('API_ID'), os.getenv('API_HASH'), bot_token=os.getenv('BOT_TOKEN')) as client:
    client.send_message(
        text=f"""<b>{zip} GSI For ARM 32 Binder 64 A/AB Devices</b>

<b>Information:</b>
<code>Built from AOSP source code with PHH patches</code>

<b>Download A-Only:</b> <a href="{da}">HERE</a>
<b>Download AB:</b> <a href="{dab}">HERE</a>

<b>amyGSI</b> - <i>Channel</i>: @amyGSI

<a href="https://github.com/HitaloSama/ErfanGSIs">Ported using my fork of Hitsuki's ErfanGSIs Edit</a>""",
        chat_id=os.getenv('CHAT_ID'),
        parse_mode="html",
        disable_web_page_preview=True
    )
