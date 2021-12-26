"""Contains commands used by the bot."""

import os
from telegram import BotCommand


commands = {
    "admins": [
        BotCommand("announce", "Announce all users"),
        BotCommand("block", "Block the user"),
        BotCommand("cancel", "Cancel the announcement"),
        BotCommand("delete", "Delete the message of admin"),
        BotCommand("unblock", "Unblock the user"),
        BotCommand("whois", "Get the details of replied user"),
    ],
    "all": [
        BotCommand("help", "Help on usage"),
        BotCommand("start", "Start the adventure"),
        BotCommand("link", "Get an invite link")
    ],
    "private": [],
}
