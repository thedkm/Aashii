"""Contains Message object."""


class Message:
    """Message contains text strings that is used in users interaction."""

    ADMIN_CONNECTED = (
        "<a href='tg://user?id={ADMIN_ID}'>{ADMIN_FULL_NAME}</a> "
        "has connected with "
        "<a href='tg://user?id={USER_ID}'>{USER_FULL_NAME}</a>"
    )

    ADMIN_CONNECTED_STATUS = "An admin has arrived"

    ANNOUNCEMENT_CANCELLED = (
        "Announcement cancelled in progress.\n"
        " • <b>Sent</b> : <code>{SENT}</code>\n"
        " • <b>Failed</b> : <code>{FAILED}</code>\n"
        " • <b>Progress</b> : <code>{PROGRESS}</code>%."
    )

    ANNOUNCEMENT_DONE = (
        "Announcement done.\n"
        " • <b>Sent</b> : <code>{SENT}</code>\n"
        " • <b>Failed</b> : <code>{FAILED}</code>\n"
        " • <b>Total</b> : <code>{TOTAL}</code>."
    )

    ANNOUNCEMENT_IN_DUE = (
        "There is already an announcement in due. "
        "Please /cancel it before starting new one."
    )

    ANNOUNCEMENT_INIT = (
        "An announcement has been initiated.\n"
        "<b>Audience</b> : <code>{TOTAL}</code> users."
    )

    ANNOUNCEMENT_PULSE = (
        "Announcement in due.\n"
        " • <b>Sent</b> : <code>{SENT}</code>\n"
        " • <b>Failed</b> : <code>{FAILED}</code>\n"
        " • <b>Progress</b> : <code>{PROGRESS}</code>%."
    )

    BLOCKED_USER = "<a href='tg://user?id={USER_ID}'>{FULL_NAME}</a> has been blocked successfully."

    BLOCKED_USER_STATUS = "You are blocked from contacting the admins."

    BLOCKED_BY_USER = "<a href='tg://user?id={USER_ID}'>{FULL_NAME}</a> has blocked me from contacting them."

    CANCELLED_ANNOUNCEMENT = (
        "Cancelled announcement at <code>{PROGRESS}</code>% progress."
    )

    DELETE_DONE = "Message deleted successfully!"

    DELETE_FAILED = "I can't delete that message …"

    ENTITY_FORWARD_ANONYMOUS = "<b>Forwarded from {SENDER_NAME}</b>\n{FROM}"

    ENTITY_FORWARD_CHAT = (
        "<b>Forwarded from <a href='https://t.me/c/{FROM_CHAT_ID}/{MESSAGE_ID}'>"
        "{FROM_CHAT_NAME}</a></b>\n"
        "{FROM}"
    )

    ENTITY_FORWARD_USER = "<b>Forwarded from <a href='tg://user?id={FROM_USER_ID}'>{FROM_FULL_NAME}</a></b>\n{FROM}"

    ENTITY_FROM = "<b><a href='tg://user?id={USER_ID}'>{FULL_NAME}</a></b>\n\n"

    ERROR = "Oops ! I faced an error : <code>{ERROR}</code>\n<code>{TRACEBACK}</code>"

    FALLBACK_STATUS = "Left"

    HELP_GROUP = (
        "Hey there ! It's <b>Aashii</b> here to help you "
        "in managing communication between members and admins.\n\n"
        "Since you are in <b>admins group</b>, the following commands are your exclusive.\n\n"
        " ⁃ /block - Blocks a user from contacting you.\n"
        " ⁃ /cancel - Cancels an announcement in progress.\n"
        " ⁃ /unblock - Unblocks a blocked user.\n\n"
        "All the above commands should be a reply to a message.\n"
        "For <code>block</code> and <code>unblock</code>, "
        "the replied message should be a forwarded message by me.\n\n"
        "Otherwise, you can pass the user ID as an argument. "
        "For example, <code>/block 2718281828</code> will block the user of given ID.\n\n"
       
    )

    HELP_PRIVATE = (
        "Welcome to @TheEolianSupportBot 👋"
        "Feel Free to ask any questions related to the group and any suggestions.\n\n"
        "Just send me any message you wish to inform the admins and As soon as an admin connects with you, you'll receive a notification.\n\n"
        "Open @eolianinvitelinkbot and Click /invite if you want to join the The Eolian Group."
        
    )

    INVALID_COMMAND = "I don't understand what you are talking about …"

    INVALID_REPLY = "I expected this as a reply to a valid message."

    NO_ANNOUNCEMENT = "No announcement is in due to cancel."

    NOT_LINKED = "I don't think that message corresponds to any user."

    NOT_PRIVATE_COMMAND = "Sorry, this command is meant to be used in admins group."

    START_GROUP = "I'm Up"

    START_PRIVATE = (
        "Welcome to @TheEolianSupportBot 👋. \n\n"
        "Feel Free to ask any questions related to the group and any suggestions.\n\n"
        "Just send me any message you wish to inform the admins and As soon as an admin connects with you, you'll receive a notification.\n\n"
        "Open @eolianinvitelinkbot and Click /invite if you want to join the The Eolian Group."
    )

    UNBLOCKED_USER = (
        "<a href='tg://user?id={USER_ID}'>{FULL_NAME}</a> has been unblocked."
    )

    UNBLOCKED_USER_STATUS = "You are now allowed to contact the admins."

    USER = (
        "Name : <a href='tg://user?id={USER_ID}'>{FULL_NAME}</a>\n"
        "Username : {USERNAME}\n"
        "User ID : <code>{USER_ID}</code>\n"
        "Membership : {MEMBERSHIP}\n"
        "Blocked : {BLOCKED}"
    )

    USER_CONNECTED = (
        "<a href='tg://user?id={USER_ID}'>{FULL_NAME}</a> has started the bot.\n" + USER
    )

    USER_NOT_FOUND = "I can't find the user in my database, something's wrong ..."
