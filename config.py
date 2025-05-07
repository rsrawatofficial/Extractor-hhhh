import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7609528498:AAGqcl_h-Cygc4v_oiXqD4cbp-yGypVcakY"
    # Telegram API ki ID
    API_ID = 27900743
    # Telegram API ki hash key
    API_HASH = "ebb06ea8d41420e60b29140dcee902fc"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '7804396225'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://rsrawat9521:bjdchdgcyuwhckhdcwkgckwyd@cluster0.pfie6h0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002543168633
    # Authentication log channel ki ID
    AUTH_LOG = -1002543168633
    # Hit log channel ki ID
    HIT_LOG = -1002543168633
    # DRM dump channel ki ID
    DRM_DUMP =  -1002543168633
    # Main channel ki ID
    CHANNEL = -1002543168633
    # Channel ka link
    CH_URL = "https://t.me/+YSYsx3Z4cXA5MTg1"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/chiru52"
    # Thumbnail image ka URL
    THUMB_URL = "https://te.legra.ph/file/11366447de3410810a383-d29ae883f7add39f2a.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

