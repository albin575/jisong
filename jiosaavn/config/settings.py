from os import getenv

API_ID = getenv("API_ID", "8733952")
API_HASH = getenv("API_HASH", "858e4d8e6f4986317031c0b83373d865")
BOT_TOKEN = getenv("BOT_TOKEN"), "6674445203:AAHOs8umDeNu-B-d-FOZrEv87wnVL_eNnKM"
BOT_COMMANDS = (
    ("start", "Initialize the bot and check its status"),
    ("settings", "Configure and manage bot settings"),
    ("help", "Get information on how to use the bot"),
    ("about", "Learn more about the bot and its features"),
)

DATABASE_URL = getenv("DATABASE_URL", None)
HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", "8080"))
KOYEB_URL = getenv("KOYEB_URL")
PING_INTERVAL = int(getenv("PING_INTERVAL", 600))
