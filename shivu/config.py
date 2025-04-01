import random
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

# List of DM pictures
dm_pics = [
    "https://graph.org/file/90344336f0da2961141a8-9129c1a27bb0bf675f.jpg",
    "https://graph.org/file/a3f5d8adc0de5639d5fc7-f5e71146b6e1d4e656.jpg",
    "https://graph.org/file/f8d15f0e2ce23398fc3f1-ccce8de39c4edbd925.jpg"
]

# List of GC pictures
gc_pics = [
    "https://graph.org/file/cb5bb601b668116408d11-d80e06bd461a3bcdbd.jpg",
    "https://graph.org/file/7e3552b9e3f5da0703288-9da63ef27ecdaefdc7.jpg",
    "https://graph.org/file/64e08a121a44740faf827-0968e6d0b694092e4a.jpg"
]

# Owner and sudo users IDs
owner_id = 'YOUR_ID'  # Replace with your Telegram user ID
sudo_users = ['SUDO_USER1', 'SUDO_USER2']  # Add your sudo users' IDs here

# Start command handler
def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    # Sending random DM image and message with buttons
    random_pic = random.choice(dm_pics)
    message = "Welcome to the Waifu Bot! Choose an option below."

    keyboard = [
        [KeyboardButton("Add Me"), KeyboardButton("Support")],
        [KeyboardButton("Updates"), KeyboardButton("Credits")],
        [KeyboardButton("Help")]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Send the random picture and message in DM
    update.message.reply_photo(photo=random_pic, caption=message, reply_markup=reply_markup)

# Help command handler
def help_command(update: Update, context: CallbackContext):
    help_text = """
    /start - Start the bot and see the options
    /help - List of all commands
    /addme - Adds the bot to your group
    /support - Support details
    /updates - Updates for the bot
    /credits - Information about the owner and sudo users
    """
    update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)

# Add Me command handler (For demonstration)
def add_me(update: Update, context: CallbackContext):
    update.message.reply_text("To add me to your group, use the following link:\n`https://t.me/your_bot_link`", parse_mode=ParseMode.MARKDOWN)

# Updates command handler
def updates(update: Update, context: CallbackContext):
    update.message.reply_text("Check back soon for updates!")

# Credits command handler
def credits(update: Update, context: CallbackContext):
    credits_text = f"Owner: {owner_id}\nSudo Users: {', '.join(sudo_users)}"
    update.message.reply_text(credits_text)

# Support command handler
def support(update: Update, context: CallbackContext):
    update.message.reply_text("For support, contact the owner.")

# Group message handler to send 3 GC image URLs
def send_gc_images(update: Update, context: CallbackContext):
    for pic in gc_pics:
        update.message.reply_photo(photo=pic)

def main():
    # Replace 'YOUR_BOT_API_KEY' with your bot's API token
    updater = Updater("YOUR_BOT_API_KEY", use_context=True)

    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("addme", add_me))
    dp.add_handler(CommandHandler("updates", updates))
    dp.add_handler(CommandHandler("credits", credits))
    dp.add_handler(CommandHandler("support", support))

    # Example: In group chat, send 3 pictures
    dp.add_handler(CommandHandler("sendgcimages", send_gc_images))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
