class Config(object):
    LOGGER = True
    OWNER_ID = 8156600797
    sudo_users = [7640076990, 7756901810, 7885908019]
    GROUP_ID = -1002499806698
    TOKEN = "7699976588:AAGltTt0NN-lS6m5daTfdIWUBjbX7OKZ1Wc"
    
    # Updated MongoDB URI
    mongo_url = "mongodb+srv://PASSTGDARK11798:TGDARK11798@passtgdark11798.aoqyfdb.mongodb.net/?retryWrites=true&w=majority&appName=PASSTGDARK11798"

    PHOTO_URL = [
        "https://graph.org/file/09e83a1d89aceabd480c5-2afc46a31083fe23f2.jpg"
    ]
    
    SUPPORT_CHAT = "Anime_Circle_Club"
    UPDATE_CHAT = "@Madara_X_Ultra_Waifus_Updates"
    BOT_USERNAME = "@Madara_X_Ultra_WaifusBot"
    CHARA_CHANNEL_ID = -1002510711682
    api_id = 28159105
    api_hash = "a0936ddf210a7e091e19947c7dc70c91"

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
    
