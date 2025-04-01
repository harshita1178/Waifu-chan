import random
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, Application, ContextTypes

# Private aur group image links
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
*I am An Open Source Character Catcher Bot... Add me in your group, and I will send random character images.*
"""
GROUP_CAPTION = "🎴 Alive!?... Connect to me in PM for more information."

# Error handler function
async def error_handler(update: Update, context: CallbackContext) -> None:
    """Log the error and send a telegram message to notify the developer."""
    # Log the error
    logger.error("Exception while handling an update:", exc_info=context.error)
    # Send a message to the developer
    await context.bot.send_message(
        chat_id=YOUR_CHAT_ID,  # Replace with your chat ID
        text=f"An error occurred: {context.error}",
    )

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message to the user when they start the bot."""
    keyboard = [
        [InlineKeyboardButton(ADD_BUTTON_TEXT, url=ADD_BUTTON_URL)],
        [InlineKeyboardButton(SUPPORT_BUTTON_TEXT, url=SUPPORT_CHAT)],
        [InlineKeyboardButton(UPDATE_BUTTON_TEXT, url=UPDATE_CHAT)],
        [InlineKeyboardButton(HELP_BUTTON_TEXT, url=BOT_USERNAME)],
        [InlineKeyboardButton(SOURCE_BUTTON_TEXT, url="https://github.com/your-repo")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(START_CAPTION, reply_markup=reply_markup)

# Group command handler
async def group(update: Update, context: CallbackContext) -> None:
    """Send random group image links."""
    random_image = random.choice(group)
    await update.message.reply_text(GROUP_CAPTION)
    await update.message.reply_photo(random_image)

# Private command handler
async def private(update: Update, context: CallbackContext) -> None:
    """Send random private image links."""
    random_image = random.choice(private)
    await update.message.reply_text("Here is your private image!")
    await update.message.reply_photo(random_image)

# Main function to start the bot
async def main():
    """Start the bot."""
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    application = Application.builder().token("YOUR_BOT_TOKEN").build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("group", group))
    application.add_handler(CommandHandler("private", private))

    # Add error handler
    application.add_error_handler(error_handler)

    # Run the bot
    await application.run_polling()

# Run the bot
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
