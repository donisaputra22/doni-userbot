# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time
from datetime import datetime
from secrets import choice


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd import DEVS
from AyiinXd.events import register
from .ping import get_readable_time


absen = [
    "**𝙃𝙖𝙙𝙞𝙧 𝙙𝙤𝙣𝙜 𝙏𝙤𝙙** 😁",
    "**𝙃𝙖𝙙𝙞𝙧 𝙆𝙖𝙠𝙖 𝙂𝙖𝙣𝙩𝙚𝙣𝙜** 😉",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝘾𝙤𝙣𝙩𝙤𝙡** 😁",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝙂𝙖𝙣𝙩𝙚𝙣𝙜** 🥵",
    "**𝙃𝙖𝙙𝙞𝙧 𝙉𝙜𝙖𝙗** 😎",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝘼𝙗𝙖𝙣𝙜** 🥺",
    "**𝙎𝙞 𝘾𝙖𝙠𝙚𝙥 𝙃𝙖𝙙𝙞𝙧 𝘽𝙖𝙣𝙜** 😎",
    "**Hadir kak maap telat** 🥺",
    "**Hadir Tuan** 🙏🏻",
    "**Hadir Majikan** 🙏🏻",
    "**Hadir Sayang** 😳",
    "**Hadir Bro Nande** 😁",
    "**maaf ka habis nemenin ka Nandee** 🥺",
    "**maaf ka habis disuruh Tuan Nandee** 🥺🙏🏻",
    "**Hadir Sayang** 😘"
    "**Hadir Nande Akuuuuhhh** ☺️",
    "**Hadir Nande brother Aku** 🥰",
]

pacar = [
    "**Kamu mau jadi pacar aku ga?** 💘",
    "**Memek mending sama aku** 😎",
    "**Hai ganteng** 🐷",
    "**Mau ga bang jadi pacar aku?** 😁",
    "**Mending pc aku bang** 🥺",
    "**Ngewe Sama Aku yuk**🥵🥵💦",
    "**Kly Mau Aku Crotin??**🥵",
    "**kly Mau Aku Sepongin??**",
    "**kly Aku Sayang Kamu ,Mwahhh😘**",
]

salam = [
    "**Wa'alaikumsalam ganteng** 🥰🥰",
    "**Wa'alaikumsalam WR WB** 👋🏻",
    "**Iyah Waalaikusalam** 🥵",
    "**Wa'alaikumsalam bang**",
    "**Wa'alaikumsalam** 🥰",
    "**Wa'alaikumsalan Warohmatullohi Wabarokatu**",
    "**Wa'alaikumsalam Ustad**",
]

ayiincakep = [
    "**𝙄𝙮𝙖 𝙂𝙖𝙣𝙩𝙚𝙣𝙜 𝘽𝙖𝙣𝙜𝙚𝙩** 😍",
    "**𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝙂𝙖𝙠 𝘼𝙙𝙖 𝙇𝙖𝙬𝙖𝙣** 😚",
    "**𝙠𝙖𝙢𝙪 𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝘼𝙠𝙪 𝙆𝙖𝙣** 😍",
    "**𝙞𝙮𝙖𝙖 𝙜𝙖𝙙𝙖 𝙖𝙙𝙖 𝙨𝙖𝙞𝙣𝙜** 😎",
    "**𝙠𝙖𝙢𝙪 𝙟𝙖𝙢𝙚𝙩 𝙏𝙖𝙥𝙞 𝘽𝙤𝙤𝙣𝙜** 😚",
]


@register(incoming=True, from_users=DEVS, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**㋱ 𝙽𝚊𝚗𝚍𝚎 - 𝚄𝚜𝚎𝚛𝚋𝚘𝚝 ㋱**\n\n✧ **ᴘɪɴɢᴇʀ :** `{} ms`\n✧ **ᴜᴘᴛɪᴍᴇ :** `{}`\n✧ **ᴏᴡɴᴇʀ :** `{}`\n✧ **ɪᴅ :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>

@register(incoming=True, from_users=DEVS, pattern=r"^Absen$")
async def ayiinabsen(ganteng):
    await ganteng.reply(choice(absen))


@register(incoming=True, from_users=DEVS, pattern=r"^Aku ganteng kan$")
async def ayiin(ganteng):
    await ganteng.reply(choice(ayiincakep))

@register(incoming=True, from_users=DEVS, pattern=r"^kly$")
async def ayiin(kly):
    await kly.reply(choice(pacar))

@register(incoming=True, from_users=DEVS, pattern=r"^dancok$")
async def ayiin(yeuh):
    await yeuh.reply(choice(salam))

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsping": f"**Plugin:** `yinsping`\
        \n\n  »  **Perintah : **`Perintah Ini Hanya Untuk Devs 𝙽𝚊𝚗𝚍𝚎 - 𝚄𝚜𝚎𝚛𝚋𝚘𝚝 Tod.`\
        \n  »  **Kegunaan :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
)
