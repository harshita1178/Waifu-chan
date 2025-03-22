class Config(object):
    LOGGER = True
    # Get this value from my.telegram.org/apps
    OWNER_ID = 6675050163  # Updated Owner ID
    sudo_users = [7640076990, 7756901810, 7885908019]  # Only 3 sudo users
    GROUP_ID = -1002499806698  # Ensure it's an integer
    TOKEN = "7583740884:AAHNM9iVB-bWa3T4USseHrTavjBV8P6lAag"
    mongo_url = "mongodb+srv://naruto:hinatababy@cluster0.rqyiyzx.mongodb.net"
    
    # Ensure full URLs are used in the list
    PHOTO_URL = [
        "https://graph.org/file/09e83a1d89aceabd480c5-2afc46a31083fe23f2.jpg"
    ]
    
    SUPPORT_CHAT = "Anime_Circle_Club"
    UPDATE_CHAT = "Waifu_Chan_Bot_updates"
    BOT_USERNAME = "@Waifu_Chan_Robot"
    CHARA_CHANNEL_ID = -1002640379822  # Ensure it's an integer
    api_id = 28480539  # Ensure it's an integer
    api_hash = "6320d9f1bc1f0b72ad66ebdb9d6bfc2c"

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
    
