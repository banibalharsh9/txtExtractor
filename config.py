#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7130342243:AAHGQ0sTu9SLiJJ58Q7XD5B0v4RF88pZfAI")
    API_ID = int(os.environ.get("API_ID", "23701738"))
    API_HASH = os.environ.get("API_HASH", "28f54cde54548df7354035c038ab3ddd")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1376801961")
    PORT = int(os.environ.get("PORT", "8080"))  # Default to 8000 if not set
