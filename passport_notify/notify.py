#!/usr/bin/env python3

import telegram_send
import datetime
import requests
import time

telegram_send.send(messages=["-------------BOT STARTED {} -------------".format(datetime.datetime.now())])

# get first request
prevRequest = requests.get("https://emrtds.nepalpassport.gov.np/iups-api/calendars/11/false")
telegram_send.send(messages=["Initial response:", prevRequest.text])

while True:
    # reqeust every 60 seconds
    time.sleep(60)
    newRequest = requests.get("https://emrtds.nepalpassport.gov.np/iups-api/calendars/11/false")
    if prevRequest.text != newRequest.text:
        telegram_send.send(messages=["CHANGE IN REQUEST", "New reqeust:", newRequest.text])
        prevRequest = newRequest
    # confirmation sake
    print(prevRequest.text)
