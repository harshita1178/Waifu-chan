import random
from html import escape
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler
from shivu import application, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection
import logging
# Private aur group image links update kiye gaye hain
private = [
    "https://graph.org/file/f8d15f0e2ce23398fc3f1-ccce8de39c4edbd925.jpg",
    "https://graph.org/file/a3f5d8adc0de5639d5fc7-f5e71146b6e1d4e656.jpg",
    "https://graph.org/file/90344336f0da2961141a8-9129c1a27bb0bf675f.jpg"
]
group = [
    "https://graph.org/file/cb5bb601b668116408d11-d80e06bd461a3bcdbd.jpg",
    "https://graph.org/file/7e3552b9e3f5da0703288-9da63ef27ecdaefdc7.jpg",
    "https://graph.org/file/64e08a121a44740faf827-0968e6d0b694092e4a.jpg"
]
# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
# Button labels aur URLs
ADD_BUTTON_TEXT = "ADD ME"
ADD_BUTTON_URL = f'http://t.me/Madara_Husbando_grabber_Bot?startgroup=new'
SUPPORT_BUTTON_TEXT = "SUPPORT"
UPDATE_BUTTON_TEXT = "UPDATES"
HELP_BUTTON_TEXT = "HELP"
SOURCE_BUTTON_TEXT = "SOURCE"
# Message templates
START_CAPTION = """*Heyyyy...* ✨
*I am An Open Source Character Catcher Bot... Add me in your group, and I will send random cha>
"""
GROUP_CAPTION = "🎴 Alive!?... Connect to me in PM for more information."
