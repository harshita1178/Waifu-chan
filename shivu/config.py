class Config(object):
    LOGGER = True
    OWNER_ID = 6675050163
    sudo_users = [7640076990, 7756901810, 7885908019]
    GROUP_ID = -1002499806698
    TOKEN = "7583740884:AAHNM9iVB-bWa3T4USseHrTavjBV8P6lAag"
    
    # Updated MongoDB URI
    mongo_url = "mongodb+srv://Harsh0987:ukdxckfSzJqlMwqQ@cluster0.mlw...mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    PHOTO_URL = [
        "https://graph.org/file/09e83a1d89aceabd480c5-2afc46a31083fe23f2.jpg"
    ]
    
    SUPPORT_CHAT = "Anime_Circle_Club"
    UPDATE_CHAT = "Waifu_Chan_Bot_updates"
    BOT_USERNAME = "@Waifu_Chan_Robot"
    CHARA_CHANNEL_ID = -1002640379822
    api_id = 28480539
    api_hash = "6320d9f1bc1f0b72ad66ebdb9d6bfc2c"

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
    
