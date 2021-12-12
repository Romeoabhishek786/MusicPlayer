import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Avenger")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "mkspali")
ALIVE_NAME = getenv("ALIVE_NAME", "Avenger")
BOT_USERNAME = getenv("BOT_USERNAME", "BotsClub_AvengerBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BotsClubMusicAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BotsClubDiscussion")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BotsClubOfficial")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b5d7c890858c43228ce7b.mp4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/BotsClub/MusicPlayer")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/bde98b16b519205325119.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a54cfaa73918badb18741.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/80cfe80e23bd7ac4ebc08.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/3f5d95249737bba8f3e82.png")
