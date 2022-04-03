import asyncio

from config import BOT_USERNAME, SUDO_USERS

from program.utils.function import get_calls

from driver.queues import QUEUE
from driver.core import user, me_bot
from driver.filters import command, other_filters
from driver.database.dbchat import remove_served_chat
from driver.database.dbqueue import remove_active_chat
from driver.decorators import authorized_users_only, bot_creator, check_blacklist

from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired


@Client.on_message(
    command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & other_filters
)
@check_blacklist()
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = (await c.get_chat(chat_id)).invite_link
        if not invitelink:
            await c.export_chat_invite_link(chat_id)
            invitelink = (await c.get_chat(chat_id)).invite_link
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
        await user.join_chat(invitelink)
        await remove_active_chat(chat_id)
        return await user.send_message(chat_id, "✅ userbot joined chat")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "✅ userbot already in chat")


@Client.on_message(
    command(["userbotleave", f"userbotleave@{BOT_USERNAME}"]) & other_filters
)
@check_blacklist()
@authorized_users_only
async def leave_chat(_, m: Message):
    chat_id = m.chat.id
    try:
        await user.leave_chat(chat_id)
        await remove_active_chat(chat_id)
        return await _.send_message(
            chat_id,
            "✅ ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠᴇᴅ ᴄʜᴀᴛ",
        )
    except UserNotParticipant:
        return await _.send_message(
            chat_id,
            "❌ ᴜsᴇʀʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ʟᴇᴀᴠᴇ ᴄʜᴀᴛ",
        )


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]) & ~filters.edited)
@bot_creator
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    
    msg = await message.reply("🔄 ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ !")
    async for dialog in user.iter_dialogs():
        try:
            await user.leave_chat(dialog.chat.id)
            await remove_active_chat(dialog.chat.id)
            left += 1
            await msg.edit(
                f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
            )
        except BaseException:
            failed += 1
            await msg.edit(
                f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
            )
        await asyncio.sleep(0.7)
    await msg.delete()
    await client.send_message(
        message.chat.id, f"✅ ʟᴇғᴛ ғʀᴏᴍ: {left} ᴄʜᴀᴛs.\n❌ ғᴀɪʟᴇᴅ ɪɴ: {failed} ᴄʜᴀᴛs."
    )


@Client.on_message(command(["vc_on", f"vc_on@{BOT_USERNAME}"]) & other_filters)
@check_blacklist()
@authorized_users_only
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    msg = await c.send_message(chat_id, "❖**sᴛᴀʀᴛɪɴɢ ᴠᴄ...**")
    try:
        peer = await user.resolve_peer(chat_id)
        await user.send(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=user.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("🔥 ɢʀᴏᴜᴘ ᴄᴀʟʟ sᴛᴀʀᴛᴇᴅ !")
    except ChatAdminRequired:
        await msg.edit_text(
            "ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄᴀʟʟ ʏᴏᴜ ᴍᴜsᴛ ᴘʀᴏᴍᴏᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ғɪʀsᴛ ᴡɪᴛʜ ᴘᴇʀᴍɪssɪᴏɴ:\n\n» 💗 ᴍᴀɴᴀɢᴇ_ᴠɪᴅᴇᴏ_ᴄʜᴀᴛs"
        )


@Client.on_message(command(["vc_stop", f"vc_stop@{BOT_USERNAME}"]) & other_filters)
@check_blacklist()
@authorized_users_only
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    msg = await c.send_message(chat_id, "❖**sᴛᴏᴘᴘɪɴɢ ᴠᴄ**...")
    if not (
        group_call := (
            await get_calls(m, err_msg="ɢʀᴏᴜᴘ ᴄᴀʟʟ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
        )
    ):
        await msg.edit_text("❌ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄᴀʟʟ ᴀʟʀᴇᴀᴅʏ ᴇɴᴅᴇᴅ")
        return
    await user.send(
        DiscardGroupCall(
            call=group_call
        )
    )
    await msg.edit_text("💝 ɢʀᴏᴜᴘ ᴄᴀʟʟ ʜᴀs ᴇɴᴅᴇᴅ !")


@Client.on_message(filters.left_chat_member)
async def bot_kicked(c: Client, m: Message):
    bot_id = me_bot.id
    chat_id = m.chat.id
    left_member = m.left_chat_member
    if left_member.id == bot_id:
        if chat_id in QUEUE:
            await remove_active_chat(chat_id)
            return
        try:
            await user.leave_chat(chat_id)
            await remove_served_chat(chat_id)
        except BaseException as err:
            print(err)
