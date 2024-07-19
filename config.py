import os
import logging
from logging.handlers import RotatingFileHandler

# token
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6776572844:AAEnthlAAl2_8b1WQ0oDQiav07tzw38_Njg")
# "6515426684:AAF8VimPWiDfpeWWyMkqw26snbFCVTSnaXM"

# api id
API_ID = int(os.environ.get("APP_ID", "6435225"))

# api hash
API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")

# Your db channel Id
# -1002219047037
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002092954715"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6259443940"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "paradoXstr")

# force sub channel id, if you want enable force sub
# Fsub 1
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002092954715"))

# Fsub 2
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002019228287"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Default admin IDs
admins_list = "6259443940, 6331067820, 5053815620, 5769925013, 6808832512, 1270076250"

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hᴇᴍʟᴏ {first}\n\nᴛʜɪs ɪs ᴀ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇ sᴛᴏʀᴀɢᴇ ʙᴏᴛ ғᴏʀ sᴛᴇʀɴʀɪᴛᴛᴇʀ.\n\nClick More Info to know more")

# Retrieve admin IDs from environment variables, if any, otherwise use defaults
admins_from_env = os.environ.get("ADMINS", admins_list)

try:
    ADMINS = [int(admin_id) for admin_id in admins_from_env.split(',')]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hemlo {first}\n\n<b>ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴀɴɪᴍᴇ ғɪʟᴇ, Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴏᴜʀ ᴀɴɪᴍᴇ ɢᴄ & ᴄʜᴀᴛ ɢᴄ ᴛᴏ ᴜsᴇ ᴍᴇ\n\n Jᴏɪɴ ᴛʜᴇ ɢɪᴠᴇɴ ᴄʜᴀɴɴᴇʟ & ɢʀᴏᴜᴘ ᴄʜᴀᴛ</b>")

# Set your Custom Caption here, Keep None to Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "Aɴɪᴍᴇ Fɪʟᴇs ʙʏ : @AnimePlaza_STR \n @OtakusMotel_STR")

# Set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', None) == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == 'True'

BOT_STATS_TEXT = "<b>ʙᴏᴛ ᴜᴘᴛɪᴍᴇ</b>⥤{uptime}"
USER_REPLY_TEXT = "You are not authorised! "

ADMINS.append(OWNER_ID)
ADMINS.append(6259443940)

LOG_FILE_NAME = "paradoXstr.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)