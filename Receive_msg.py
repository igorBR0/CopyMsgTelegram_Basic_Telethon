import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)
import time
import os

import configparser
import json
import re

import time
import os
from flask import Flask, jsonify
import threading
import mysql.connector

from datetime import datetime





api_id = "**********************" your API ID - GET SITE TELEGRAM
api_hash = "****************************" Your API HASH - GET SITE TELEGRAM

phone = Your number cell
name = "Your count name"

client = TelegramClient(name, api_id, api_hash)

chat_ids = [-100123562772, -55627728]    

def run_db(tip,tabela):
    mydb = mysql.connector.connect(host='**************',database='***********',user='***********',password='*************')
    mycursor = mydb.cursor()
    sql = "INSERT INTO "+tabela+" (id,tip,datetimes) VALUES (%s,%s,%s)"
    
    val = ("DEFAULT",tip,datetime.now())
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    if mydb.is_connected():
        mydb.close()
        mycursor.close()
    print("Finish conection")
    

@client.on(events.NewMessage(chats="ID CHAT!!! HERE")) #****
async def newMessageListener(event):
    newMessage = event.message.message
    print(newMessage)
    run_db(newMessage,"YOUR TABLE DATABASE")



with client:
    client.run_until_disconnected()
 







