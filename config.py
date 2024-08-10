#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "29029800"))
    API_HASH = os.environ.get("API_HASH", "0258b310e9ebb9b5155b5740d6ecf126")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6790518589""1957816775""6899180574")
    PORT = int(os.environ.get("PORT", "8080"))  # Default to 8000 if not set
