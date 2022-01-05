import logging
import os
import threading
import time
import subprocess
import requests
import socket
import faulthandler
import aria2p
import json
import qbittorrentapi as qba
from pyrogram import Client
from dotenv import load_dotenv


load_dotenv('config.env', override=True)
def getConfig(name: str):
    return os.environ[name]
  
try:
    PORT = getConfig('PORT')
    if len(SERVER_PORT) == 0:
        raise KeyError
except KeyError:
    SERVER_PORT = 8080
    
try:
    API_ID = getConfig('API_ID')
except KeyError as e:
    LOGGER.error("Error!! Add Session string")
    exit(1)

try:
    SESSION_STRING = getConfig('SESSION_STRING')
    if len(SESSION_STRING) == 0:
        raise KeyError
except KeyError:
    LOGGER.error("Error!! Add Session string")
    exit(1)
try:
  API_HASH = getConfig('API_HASH')
except KeyError:
  LOGGER.error("Error!! API_HASH Missing")
  exit(1)
