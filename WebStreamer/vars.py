# (c) @PredatorHackerzZ | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID','2980496')
    API_HASH = str(getenv('API_HASH','9415a61fedcc0f00f33667ca46e577a3')
    BOT_TOKEN = str(getenv('BOT_TOKEN','1687590985:AAEyKb3P65kDBY1vtwMScqenkEokByEh7io')
    SESSION_NAME = str(getenv('SESSION_NAME', 'UMR_FILE_STORE_BOT'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '1'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(getenv('OWNER_ID', '1086432320'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU else APP_NAME+'.herokuapp.com'
    DATABASE_URL = str(getenv('DATABASE_URL'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
