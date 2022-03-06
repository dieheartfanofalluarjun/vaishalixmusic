import os
from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SESSION_NAME = getenv("SESSION_NAME", "session")

# mandatory vars
BOT_NAME = getenv("BOT_NAME")
OWNER_USERNAME = getenv("OWNER_USERNAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/santhosh-podili/santhoshpodili")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "santhuvc")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "santhubotupadates")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/ce7dec913a00dc2d76bb9.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/ad1f8bcc4d044d3f25fb3.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/7569d601b34af1bb14570.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/35700a88d56fd6064822a.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/19814cb8155e0a06a1da9.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/9f9a3b5b0822fa621d4c1.jpg")
UPTIME_IMG = getenv("UPTIME_IMG", "https://te.legra.ph/file/cb90632e3a8be66760c0b.jpg") 
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/52771fab9aa447154ecfd.jpg")
