import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#import pycurl



# bot = Client(

#     "bot",

#     api_id=api_id,

#     api_hash=api_hash,

#     bot_token=bot_token)



from logging.handlers import RotatingFileHandler



logging.basicConfig(

    level=logging.DEBUG,

    format=

    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",

    datefmt="%d-%b-%y %H:%M:%S",

    handlers=[

        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),

        logging.StreamHandler(),

    ],

)

logging.getLogger("pyrogram").setLevel(logging.WARNING)





logging = logging.getLogger()





bot = Client("bot",

             bot_token=os.environ.get("BOT_TOKEN"),

             api_id=int(os.environ.get("API_ID")),

             api_hash=os.environ.get("API_HASH"))

auth_users = [1318247204,6004318404,1511103739,5986734743,5971411129,6488555238,6488555238]

sudo_users = auth_users

sudo_groups = [-4088348095,-4073031859]



shell_usage = f"**USAGE:** Executes terminal commands directly via bot.\n\n<pre>/shell pip install requests</pre>"

def one(user_id):

    if user_id in sudo_users:

        return True

    return False

@bot.on_message(filters.command(["shell"]))

async def shell(client, message: Message):

    """

    Executes terminal commands via bot.

    """

    logging.info('hh')

    if not one(message.from_user.id):

        return



    if len(message.command) < 2:

        return await message.reply_text(shell_usage, quote=True)



    user_input = message.text.split(None, 1)[1].split(" ")



    try:

        shell = subprocess.Popen(

            user_input, stdout=subprocess.PIPE, stderr=subprocess.PIPE

        )



        stdout, stderr = shell.communicate()

        result = str(stdout.decode().strip()) + str(stderr.decode().strip())



    except Exception as error:

        logging.info(f"{error}")

        return await message.reply_text(f"**Error**:\n\n{error}", quote=True)



    if len(result) > 2000:

        file = BytesIO(result.encode())

        file.name = "output.txt"

        await message.reply_text("Output is too large (Sending it as File)", quote=True)

        await client.send_document(message.chat.id, file, caption=file.name)

    else:

        await message.reply_text(f"**Output:**:\n\n{result}", quote=True)







keyboard = InlineKeyboardMarkup(

    [

        [

            InlineKeyboardButton(

                text="Devloper",

                url="nothing",

            ),

            InlineKeyboardButton(

                text="Repo",

                url="https://github.com/",

            ),

        ],

    ]

)





@bot.on_message(filters.command(["aditya"]))

async def account_login(bot: Client, m: Message):



 editable = await m.reply_text("**Hi Press**\n**Text** = /pro_txt\n**Top** = /pro_top\n**Vision** = /pro_vision\n**Jw** = /pro_jw\n**Olive** = /pro_olive\n**Addapdf** = /adda_pdf")





@bot.on_message(filters.command(["cancel"]))

async def cancel(_, m):

    editable = await m.reply_text("Canceling All process Plz wait\n🚦🚦 Last Process Stopped 🚦🚦")

    global cancel

    cancel = True

    await editable.edit("cancled")

    return





@bot.on_message(filters.command("restart"))

async def restart_handler(_, m):

    await m.reply_text("Restarted!", True)

    os.execl(sys.executable, sys.executable, *sys.argv)





@bot.on_message(filters.command(["pro_txt"]))

async def account_login(bot: Client, m: Message):

    user = m.from_user.id if m.from_user is not None else None

    if user is not None and user not in sudo_users:

        await m.reply("**Please buy this bot", quote=True)

        return

    else:

        editable = await m.reply_text(

            "Hello Bro **I am Text Downloader Bot and made by Aditya**. I can download videos from **text** file one by one.**\n\nDeveloper** : Aditya**\nLanguage** : Python**\nFramework** : Pyrogram\n\nSend **TXT** File FORMAT {FileName : FileLink}")

    input: Message = await bot.listen(editable.chat.id)

    x = await input.download()

    await input.delete(True)

    logging.info(2333)

    path = f"./downloads/{m.chat.id}"



    try:

        with open(x, "r") as f:

            content = f.read()

        content = content.split("\n")

        links = []

        for i in content:

            links.append(i.split(":",1)) 

        os.remove(x)

        # print(len(links))

    except:

        await m.reply_text("Invalid file input.")

        os.remove(x)

        return



    editable = await m.reply_text(

        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"

    )

    input1: Message = await bot.listen(editable.chat.id)

    raw_text = input1.text



    try:

        arg = int(raw_text)

    except:

        arg = 0



    editable = await m.reply_text("**Enter batch name**")

    input0: Message = await bot.listen(editable.chat.id)

    raw_text0 = input0.text



    await m.reply_text("**Enter resolution**")

    input2: Message = await bot.listen(editable.chat.id)

    raw_text2 = input2.text



    editable4 = await m.reply_text(

        "Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**"

    )

    input6 = message = await bot.listen(editable.chat.id)

    raw_text6 = input6.text



    thumb = input6.text

    if thumb.startswith("http://") or thumb.startswith("https://"):

        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")

        thumb = "thumb.jpg"

    else:

        thumb == "no"



    if raw_text == '0':

        count = 1

    else:

        count = int(raw_text)

    editable = await m.reply_text("**Download by**")

    input9: Message = await bot.listen(editable.chat.id)

    raw_text9 = input9.text

    

    try:

        for i in range(arg, len(links)):



            url = links[i][1]

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()



            if raw_text2 == "144":



                cmd = f'yt-dlp -F "{url}"'

                k = await helper.run(cmd)

                out = helper.vid_info(str(k))

                # print(out)

                if '256x144' in out:

                    ytf = f"{out['256x144']}"

                elif '320x180' in out:

                    ytf = out['320x180']

                elif 'unknown' in out:

                    ytf = out["unknown"]

                else:

                    for data1 in out:

                        ytf = out[data1]

            elif raw_text2 == "180":



                cmd = f'yt-dlp -F "{url}"'

                k = await helper.run(cmd)

                out = helper.vid_info(str(k))

                # print(out)

                if '320x180' in out:

                    ytf = out['320x180']

                elif '426x240' in out:

                    ytf = out['426x240']

                elif 'unknown' in out:

                    ytf = out["unknown"]

                else:

                    for data2 in out:

                        ytf = out[data2]

            elif raw_text2 == "240":



                cmd = f'yt-dlp -F "{url}"'

                k = await helper.run(cmd)

                out = helper.vid_info(str(k))

                # print(out)

                if '426x240' in out:

                    ytf = out['426x240']

                elif '426x234' in out:

                    ytf = out['426x234']

                elif '480x270' in out:

                    ytf = out['480x270']

                elif '480x272' in out:

                    ytf = out['480x272']

                elif '640x360' in out:

                    ytf = out['640x360']

                elif 'unknown' in out:

                    ytf = out["unknown"]

                else:

                    for data3 in out:

                        ytf = out[data3]

            elif raw_text2 == "360":



                cmd = f'yt-dlp -F "{url}"'

                k = await helper.run(cmd)

                out = helper.vid_info(str(k))

                # print(out)

                if '640x360' in out:

                    ytf = out['640x360']

                elif '638x360' in out:

                    ytf = out['638x360']

                elif '636x360' in out:

                    ytf = out['636x360']

                elif '768x432' in out:

                    ytf = out['768x432']

                elif '638x358' in out:

                    ytf = out['638x358']

                elif '852x316' in out:

                    ytf = out['852x316']

                elif '850x480' in out:

                    ytf = out['850x480']

                elif '848x480' in out:

                    ytf = out['848x480']

                elif '854x480' in out:

                    ytf = out['854x480']

                elif '852x480' in out:

                    ytf = out['852x480']

                elif '854x470' in out:

                    ytf = out['852x470']

                elif '1280x720' in out:

                    ytf = out['1280x720']

                elif 'unknown' in out:

                    ytf = out["unknown"]

                else:

                    for data4 in out:

                        ytf = out[data4]

            elif raw_text2 == "480":



                cmd = f'yt-dlp -F "{url}"'

                k = await helper.run(cmd)

                out = helper.vid_info(str(k))

                # print(out)

                if '854x480' in out:

                    ytf = out['854x480']

                elif '852x480' in out:

                    ytf = out['852x480']

                elif '854x470' in out:

                    ytf = out['854x470']

                elif '768x432' in out:

                    ytf = out['768x432']

                elif '848x480' in out:

                    ytf = out['848x480']

                elif '850x480' in out:

                    ytf = ['850x480']

                elif '960x540' in out:

                    ytf = out['960x540']

                elif '640x360' in out:

                    ytf = out['640x360']

                elif 'unknown' in out:

                    ytf = out["unknown"]

                else:

                    for data5 in out:

                        ytf = out[data5]



            elif raw_text2 == "720":



                cmd = f'yt-dlp -F "{url}"'

                k = await helper.run(cmd)

                out = helper.vid_info(str(k))

                # print(out)

                if '1280x720' in out:

                    ytf = out['1280x720']

                elif '1280x704' in out:

                    ytf = out['1280x704']

                elif '1280x474' in out:

                    ytf = out['1280x474']

                elif '1920x712' in out:

                    ytf = out['1920x712']

                elif '1920x1056' in out:

                    ytf = out['1920x1056']

                elif '854x480' in out:

                    ytf = out['854x480']

                elif '640x360' in out:

                    ytf = out['640x360']

                elif 'unknown' in out:

                    ytf = out["unknown"]

                else:

                    for data6 in out:

                        ytf = out[data6]

            elif "player.vimeo" in url:

                if raw_text2 == '144':

                    ytf = 'http-240p'

                elif raw_text2 == "240":

                    ytf = 'http-240p'

                elif raw_text2 == '360':

                    ytf = 'http-360p'

                elif raw_text2 == '480':

                    ytf = 'http-540p'

                elif raw_text2 == '720':

                    ytf = 'http-720p'

                else:

                    ytf = 'http-360p'

            else:

                cmd = f'yt-dlp -F "{url}"'

                k = await helper.run(cmd)

                out = helper.vid_info(str(k))

                for dataS in out:

                    ytf = out[dataS]



            try:

                if "unknown" in out:

                    res = "NA"

                else:

                    res = list(out.keys())[list(out.values()).index(ytf)]



                name = f'{str(count).zfill(3)}) {name1} {res}'

            except Exception:

                res = "NA"



            # if "youtu" in url:

            # if ytf == f"'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]'" or "acecwply" in url:

            if "acecwply" in url:

                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'

            elif "youtu" in url:

                cmd = f'yt-dlp -i -f "bestvideo[height<={raw_text2}]+bestaudio" --no-keep-video --remux-video mkv --no-warning "{url}" -o "{name}.%(ext)s"'

            elif "player.vimeo" in url:

                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            elif "m3u8" or "livestream" in url:

                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            elif ytf == "0" or "unknown" in out:

                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            elif ".pdf" or "download" in url:

                cmd = "pdf"

            else:

                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'



            try:

                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`"

                prog = await m.reply_text(Show)

                cc = f"**Name :** {name1} {res}A͜͡d͜͡i͜͡t͜͡y͜͡a͜͡.mkv\n**Batch :** {raw_text0}\n**Index :** {str(count).zfill(3)}\n\n**Downloaded By** :- {raw_text9}"

                cc1 = f"**Name :** ** {name1} {res}A͜͡d͜͡i͜͡t͜͡y͜͡a͜͡.pdf\n**Batch :** {raw_text0}\n**Index :** {str(count).zfill(3)}\n\n**Downloaded By** :- {raw_text9}"

                #                         await prog.delete (True)

                #                 if cmd == "pdf" or "drive" in url:

                #                     try:

                #                         ka=await helper.download(url,name)

                #                         await prog.delete (True)

                #                         time.sleep(1)

                #                         # await helper.send_doc(bot,m,cc,ka,cc1,prog,count,name)

                #                         reply = await m.reply_text(f"Uploading - `{name}`")

                #                         time.sleep(1)

                #                         start_time = time.time()

                #                         await m.reply_document(ka,caption=cc1)

                #                         count+=1

                #                         await reply.delete (True)

                #                         time.sleep(1)

                #                         os.remove(ka)

                #                         time.sleep(3)

                #                     except FloodWait as e:

                #                         await m.reply_text(str(e))

                #                         time.sleep(e.x)

                #                         continue

                if cmd == "pdf" or ".pdf" in url or ".pdf" in name:

                    try:

                        ka = await helper.aio(url, name)

                        await prog.delete(True)

                        time.sleep(1)

                        reply = await m.reply_text(f"Uploading - ```{name}```")

                        time.sleep(1)

                        start_time = time.time()

                        await m.reply_document(

                            ka,

                            caption=

                            f"**Name »** {name1} {res}A͜͡d͜͡i͜͡t͜͡y͜͡a͜͡.pdf\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"

                        )

                        count += 1

                        # time.sleep(1)

                        await reply.delete(True)

                        time.sleep(1)

                        os.remove(ka)

                        time.sleep(3)

                    except FloodWait as e:

                        await m.reply_text(str(e))

                        time.sleep(e.x)

                        continue

                else:

                    res_file = await helper.download_video(url, cmd, name)

                    filename = res_file

                    await helper.send_vid(bot, m, cc, filename, thumb, name,

                                          prog)

                    count += 1

                    time.sleep(1)



            except Exception as e:

                await m.reply_text(

                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"

                )

                continue



    except Exception as e:

        logging.error(e)

                        

        await m.reply_text(e)

    await m.reply_text("🚦Done🚦")





