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
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "musicupdates12")
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
UPTIME_IMG = getenv("UPTIME_IMG", "https://te.legra.ph/file/1864dfe3c8a58ca2feac3.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "assets/Youtube.jpeg") 

## BOT IMG
START_IMG_URL = [
 "https://telegra.ph/file/c2ff65c5f7ddbb6a52170.jpg", 
 "https://te.legra.ph/file/449a5c8301dc0f48f842e.jpg", 
 "https://te.legra.ph/file/39e707ee27325867e27b1.jpg", 
 "https://te.legra.ph/file/90812b7fa0538389943ab.jpg", 
 "https://te.legra.ph/file/914fc426bed31dbe4bdc2.jpg", 
 "https://te.legra.ph/file/28f95b221efbefede9988.jpg", 
 "https://telegra.ph/file/290e055a47df326b6e908.jpg", 
 "https://telegra.ph/file/4a2c348dc10f4799ecc23.jpg", 
 "https://telegra.ph/file/e5d14734cc62fb45ebb80.jpg", 
 "https://telegra.ph/file/52771fab9aa447154ecfd.jpg", 
 "https://telegra.ph/file/28af6e4d2f6c9849ccd8e.jpg", 
 "https://telegra.ph/file/de94973a185e70e207363.jpg"
]
