# cfg.py

import re


HOST = 'irc.chat.twitch.tv'
PORT = 6667
NICK = 'xd_bot_xd'
PASS = 'oauth:qfo55414g1bnak5x0x40merhmm42yb'  # used for irc
CHAN = '#hwangbroxd'
ADMIN = ['hwangbroxd', 'unlord1', 'gay_zach']
CLIENT_ID = 'zfr9wyvljqfa3wn7acgse9bvo3xz2b'
secret = 'rvs7zybcbiksg969eyt34mj27nzpld'
CHANNEL_ID = '31561772'
TOKEN = 'cdnjlxxmdu5bupkvgj9bvvgpmw20m2'  # used for api
URL = 'https://api.twitch.tv/kraken/channels/31561772'
HEADERS = {'Client-ID': CLIENT_ID,
           'Accept': 'application/vnd.twitchtv.v5+json',
           'Authorization': f'OAuth {TOKEN}'}
SCOPES = 'channel_editor+channel_read'
