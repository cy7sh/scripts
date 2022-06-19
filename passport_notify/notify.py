#!/usr/bin/env python3

import telegram_send
import datetime
import requests
import time

telegram_send.send(messages=["-------------BOT STARTED {} -------------".format(datetime.datetime.now())])

# get first request
global prevRequest
while True:
    try:
        prevRequest = requests.get("https://emrtds.nepalpassport.gov.np/iups-api/calendars/79/false")
        telegram_send.send(messages=["Initial response:", prevRequest.text])
        print("Initial response:", prevRequest.text)
        break
    except:
        time.sleep(30)
        continue

while True:
    # confirmation sake
    print(prevRequest.text)
    time.sleep(300)
    try:
        newRequest = requests.get("https://emrtds.nepalpassport.gov.np/iups-api/calendars/79/false")
    except:
        continue
    if prevRequest.text != newRequest.text:
        telegram_send.send(messages=["CHANGE IN REQUEST", "New reqeust:", newRequest.text])
        print("CHANGE IN REQUEST", "New reqeust:", newRequest.text)
        prevRequest = newRequest
