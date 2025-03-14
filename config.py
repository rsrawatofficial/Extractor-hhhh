import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7527954976:AAG18eVvsB3BezEzo4e3UYeiYmSRzL-Osfk"
    # Telegram API ki ID
    API_ID = 18116358
    # Telegram API ki hash key
    API_HASH = "80e7597f27a57df271dfc500120d4ea9"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '7836088695'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://mewadonlinestudy:yYjxKiZGQag8DnWH@cpvod.ywpecvo.mongodb.net/?retryWrites=true&w=majority&appName=cpvodak"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002382878293
    # Authentication log channel ki ID
    AUTH_LOG = -1002156464632
    # Hit log channel ki ID
    HIT_LOG = -1002384141550
    # DRM dump channel ki ID
    DRM_DUMP = -1002363712791
    # Main channel ki ID
    CHANNEL = -1002307483076
    # Channel ka link
    CH_URL = "https://t.me/+jkYFQeHgOpZkOTg9"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/SEM2JOB"
    # Thumbnail image ka URL
    THUMB_URL = "https://te.legra.ph/file/11366447de3410810a383-d29ae883f7add39f2a.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

