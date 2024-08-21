import pytchat
import time
import logging

chat = pytchat.create(video_id='lD93mU3yRHQ')

logging.basicConfig(filename='chat.log', level=logging.INFO)

while chat.is_alive():
    for c in chat.get().sync_items():
        logging.info(f"{c.datetime} [{c.author.name}]: {c.message}")
