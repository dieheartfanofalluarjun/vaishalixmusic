import asyncio

from datetime import datetime
from sys import version_info
from time import time
import random

from config import (
    UPTIME_IMG, 
    START_IMG_URL, 
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from driver.decorators import check_blacklist
from program import __version__
from driver.core import bot, me_bot, me_user
from driver.filters import command
from driver.database.dbchat import add_served_chat, is_served_chat
from driver.database.dbpunish import is_gbanned_user
from driver.database.dbusers import add_served_user, is_served_user
from driver.database.dblockchat import blacklisted_chats

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from pyrogram.errors import UserNotParticipant

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)

force_channel = "santhubotupadates"

@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
@check_blacklist()
async def start_(c: Client, message: Message):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, message.from_user.id) 
            if user.status == "kicked out":
                await message.reply_text("You are banned") 
                return
        except UserNotParticipant:
            await message.reply_photo(
                photo=random.choice(START_IMG_URL),
                caption="?????????? ???????? s?????s???????????? ????? ????????????????? s?????s???????????? ???????? ???s??? ??????..????", 
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("?????????????????????? ?????????????????????", url=f"t.me/{force_channel}") 
                 ]]
                ) 
            )
            return
    user_id = message.from_user.id
    await add_served_user(user_id)
    await message.reply_photo(
        photo=random.choice(START_IMG_URL), 
        caption= f"""???? **???????????????????????? {message.from_user.mention()} !**\n
???? [{me_bot.first_name}](https://t.me/{BOT_USERNAME}) **?????????????s ???????? ?????? ?????????? ??????s????????? ???????? ?????????????????? ????? ?????????????s ????????????????? ???????? ????????????????????? ????????????? ?????????????? ???????????!**

???? **????????? ????????? ??????? ???????? ????????'s ????????????????????s ???????? ???????? ?????????? ??????????? ???? ??????????????????? ????? ???????? ?? ??????? ?????????????? ????????????????????s ????????????????!**

???? **?????? ??????????? ???????? ?????? ???s??? ???????s ????????, ???????????s??? ????????????? ????? ???????? ?? ???? ??????????? ?????s????? ????????????? ????????????????  ??????? ?????????? ???????? ??????????? ??????????? /help **
""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("????s?????????????????????", url="https://t.me/musicupdates12"), 
            InlineKeyboardButton("?????????????????????????", url="https://t.me/santhubotupadates"), 
            ],[
            InlineKeyboardButton("???????????????????", callback_data="repo"), 
            InlineKeyboardButton("?????????????????????????", url="https://t.me/santhu_music_bot"), 
            ],[
            InlineKeyboardButton("????s????????? ????????????????????s", callback_data="sudo_command"), 
            InlineKeyboardButton("????????????????? ?????????s", callback_data="admin_command"), 
            ],[
            InlineKeyboardButton("??????????????? ???????? ???????????????? ???????????????????????", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]]
            ) 
        ) 
        
@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
@check_blacklist()
async def help(c: Client, message: Message):
    BOT_NAME = me_bot.first_name
    await message.reply_text(
        f""" ??? **???????????? {message.from_user.mention()} !**\n
???? **?????? ??????????? ???????? ?????? s???????????? ???????s ????????? ??????????? ???? s??????????????? ?????? ???????s ???????? ???? ????????????? **\n
???? **?????? ??????????? ?????????? ??????????????/??????????????/??????????? ??????????? ???? ????????????? ???s??? ????????????????????s **\n
???? **?????? ??????????? ????????????? s??????????? ???????????????????? ????? ????????? ??????????? ???? ??????? ????????????????????s**\n """,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("?????????????s ?????????s", callback_data="admin_command"), 
            InlineKeyboardButton("s????????? ?????????s", callback_data="sudo_command"), 
            ],[
            InlineKeyboardButton("???s????? ?????????s", callback_data="user_command")
            ],[
            InlineKeyboardButton("????????????????????s ????s???", callback_data="command_list"), 
            InlineKeyboardButton("?????", callback_data="id")
            ]]
            ) 
        )  
        
@Client.on_message(
    command(["ghelp", f"ghelp@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
@check_blacklist()
async def ghelp(c: Client, message: Message):
    chat_id = message.chat.id
    BOT_NAME = me_bot.first_name
    await message.reply_text(
        f""" ??? **???????????? {message.from_user.mention()} !**\n
???? **?????? ??????????? ???????? ?????? s???????????? ???????s ????????? ??????????? ???? s??????????????? ?????? ???????s ???????? ???? ????????????? **\n
???? **?????? ??????????? ?????????? ??????????????/??????????????/??????????? ??????????? ???? ????????????? ???s??? ????????????????????s **\n
???? **?????? ??????????? ????????????? s??????????? ???????????????????? ????? ????????? ??????????? ???? ??????? ????????????????????s**\n """,
        reply_markup=InlineKeyboardMarkup(
        
        [
            [
                InlineKeyboardButton(
                                       "???????????????s??? ????????? ?????? ?????????? ?????????????????", url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton( 
                                       "????s????????? ????????????????????s????", callback_data="sudo_command"
                )
            ],
            [
                InlineKeyboardButton(
                                       "????????????????? ?????????s????", callback_data="admin_commands"
                )
            ],
            [
                InlineKeyboardButton(
                                       "????????????????????????s ????s???????", callback_data="command_list"
                )
            ],
            [
                InlineKeyboardButton("???????????????????????????", url="https://t.me/musicupdates12"),
                InlineKeyboardButton(
                    "???", callback_data="home_start"
                ),
            ]
            
        ]      
  ),
        disable_web_page_preview=True,
    )




@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
@check_blacklist()
async def alive(c: Client, message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    BOT_NAME = me_bot.first_name

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("???????????????????????????", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "?????????????????????????", url="https://t.me/musicupdates12"
                ),
            ]
        ]
    )

    alive = f"**???????????? {message.from_user.mention()}, ???????? {BOT_NAME}**\n\n???? ????????????? ??????????? ????: [{ALIVE_NAME}](https://t.me/{OWNER_USERNAME})\n???? ???????? ????????s???????: `v{__version__}`\n???? ?????????????????? ????????s???????: `{pyrover}`\n???? ??????????????? ????????s???????: `{__python_version__}`\n???? ????????????????????s ????????s???????: `{pytover.__version__}`\n???? ?????????????????: `{uptime}`\n???? ???????????????????? ????: '[{GROUP_SUPPORT}](https://t.me/{GROUP_SUPPORT})'\n???**?????????????s ??????? ??????????????? ?????? ??????????, ??????? ???????????????? ?????????????? & ??????s????? ????? ?????????? ?????????????'s ?????????????? ??????????? [???????????????????? ???? ????](https://t.me/santhu_music_bot)**"

    await c.send_photo(
        chat_id,
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
@check_blacklist()
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("???????????????...")
    delta_ping = time() - start
    await m_reply.edit_text("???? `??????????!!`\n" f"???? `{delta_ping * 1000:.3f} ms`")

@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@check_blacklist()
async def get_uptime(c: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=(UPTIME_IMG), 
        caption="???? s????????????? ???????? s????????????s:\n"
                f"??? **?????????????????:** `{uptime}`\n"
                f"??? **???s?????:** `{message.from_user.mention()}`\n"
                f"??? **s??????????? ???????????:** `{START_TIME_ISO}`\n"
                f"??? **???????????????????? ????:** `{GROUP_SUPPORT}`"
              ) 
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("???????????????????????????", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "?????????????????????????", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )


@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = me_user.username
    bot_id = me_bot.id
    for member in m.new_chat_members:
        if chat_id in await blacklisted_chats():
            await m.reply(
                "?????? This chat has blacklisted by sudo user and You're not allowed to use me in this chat."
            )
            return await bot.leave_chat(chat_id)
        if member.id == bot_id:
            return await m.reply(
                "?????? ?????????????s ??????? ??????????????? ?????? ?????? ???????? **Group** !\n\n"
                "??????????????????? ?????? ???s ???????????????s???????????????? ???? ???????? **Group**, ??????????????????s??? ?? ????????? ???????? ????? ?????????? ?????? ??????????? ????????????????????, ???????? ????????'??? ??????????????? ?????? ???????????  `/userbotjoin` ?????? ??????????????? ???????? ???ss??s??????????? ?????? ???????????.\n\n"
                "??????????? ???????????, ?????????? ??????????? `/reload`",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("?????????????????????????", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("???????????????????????????", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("???????ss??s???????????????", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )


chat_watcher_group = 10

@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message: Message):
    if message.from_user:
        user_id = message.from_user.id
        await add_served_user(user_id)
        return
    try:
        userid = message.from_user.id
    except Exception:
        return
    suspect = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.ban_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"???????? (> {suspect} <)\n\n**Gbanned** user detected, that user has been gbanned by sudo user and was blocked from this Chat !\n\n???? **Reason:** potential spammer and abuser."
        )


