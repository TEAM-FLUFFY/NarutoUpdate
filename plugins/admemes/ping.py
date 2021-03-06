"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് Start ചെയ്തു നോക്ക്..🙂" 
HELP = "Help ഒന്നും ഇല്ല ഓടിക്കോ......"
REPO = "Oops The repo is Vanished Because of CopyCats"
APPROVAL = "This command is made to be used in group chats, not in pm!"
APPROVE = "This command is made to be used in group chats, not in pm!"
APPROVED = "This command is made to be used in group chats, not in pm!"
UNAPPROVEALL = "This command is made to be used in group chats, not in pm!"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("approval", COMMAND_HAND_LER) & f_onw_fliter)
async def go_notavailable(_, message):
    await message.reply_text(APPROVAL)


@Client.on_message(filters.command("approve", COMMAND_HAND_LER) & f_onw_fliter)
async def go_notavailabl(_, message):
    await message.reply_text(APPROVE)


@Client.on_message(filters.command("approved", COMMAND_HAND_LER) & f_onw_fliter)
async def go_notavailab(_, message):
    await message.reply_text(APPROVED)


@Client.on_message(filters.command("unapproveall", COMMAND_HAND_LER) & f_onw_fliter)
async def go_notavailable(_, message):
    await message.reply_text(UNAPPROVEALL)
