#!/usr/bin/env python3

import telegram_send
import requests
import time
import xml.etree.ElementTree as ET
import datetime

def findData(root):
    for child in root:
        if child.tag == "data":
            return child.text
        # check if child has data
        data = findData(child)
        if data != None:
            return data

telegram_send.send(messages=["-------------BOT STARTED {} -------------".format(datetime.datetime.now())])

session = requests.session()

burp0_url = "https://wsr.pearsonvue.com:443/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE/2026684"
burp0_cookies = {"JSESSIONID": "CAEA7861384478D6EE642A5332EF187D", "oam.Flash.RENDERMAP.TOKEN": "-dehrsxcj2", "wg-startOverUrl": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "wg-externalAuth": "true", "wg-clientCode": "PEARSONLANGUAGE", "singleSignOnTimeoutURL": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "BIGipServer~managed~prd_wsr_pool_blue": "!kUDPDq3bwmVfHJxBP6jH124VbQXmH2Nz4nnTj66JMCfteOmTBhikVDC9KvVKC8iJVC6AvejIN1qZNJjMqOWxw4/BezIFBYqGAYr4ssAB", "__uzma": "3808662f-8c5c-418d-a806-f04704c13f4a", "__uzmb": "1647254062", "__uzmc": "380329185796", "__uzmd": "1647255130"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Faces-Request": "partial/ajax", "Origin": "https://wsr.pearsonvue.com", "Dnt": "1", "Referer": "https://wsr.pearsonvue.com/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE?conversationId=2026684", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
burp0_data = {"geoCodeLatitude": "27.6280864", "geoCodeLongitude": "83.4748498", "threeCharCountryCode": '', "fullAddress": "Alfa Beta Complex, 1st floor, New Baneshwor, Kathmandu, Bagmati, Kathmandu, 44600, Nepal", "geoCodeTwoCharCountryCode": '', "preferredDateHidden": "06/13/2022", "resultCardID": "5", "preferredDateHidden_1": '', "preferredDateHiddenForAriaLabel_1": '', "preferredDateShown_1": "Select a date for appointment times", "preferredDateHidden_2": '', "preferredDateHiddenForAriaLabel_2": '', "preferredDateShown_2": "Select a date for appointment times", "preferredDateHidden_3": '', "preferredDateHiddenForAriaLabel_3": '', "preferredDateShown_3": "Select a date for appointment times", "preferredDateHidden_4": '', "preferredDateHiddenForAriaLabel_4": '', "preferredDateShown_4": "Select a date for appointment times", "preferredDateHidden_5": '', "preferredDateHiddenForAriaLabel_5": "06/14/2022", "preferredDateShown_5": "14 June 2022", "appt_menu_5": "1655218800000:83406", "combinedtestCenterFormId_SUBMIT": "1", "javax.faces.ViewState": "OjCXdZBT38K8eJqYf6yD6lrnlkuhyRjpx0CQKXywWJ4pEIBq", "year": "2022", "month": "5", "testCenterId": "71336", "org.richfaces.ajax.component": "j_id_43_1_1_0_1_2", "j_id_43_1_1_0_1_2": "j_id_43_1_1_0_1_2", "rfExt": "null", "AJAX:EVENTS_COUNT": "1", "javax.faces.partial.event": "undefined", "javax.faces.source": "j_id_43_1_1_0_1_2", "javax.faces.partial.ajax": "true", "javax.faces.partial.execute": "@component", "javax.faces.partial.render": "@component", "combinedtestCenterFormId": "combinedtestCenterFormId"}

nextMonth = 4

while True:
    burp0_data["month"] = str(nextMonth)

    request = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    root = ET.fromstring(request.text)
    data = findData(root)
    if data == None:
        print("session expired")
        telegram_send.send(messages=["SESSION EXPIRED PLEASE UPDATE! BOT SHUTTING DOWN."])
        break
    # confirmation sake
    print(data)

    if nextMonth == 4:
        if len(data) != 58:
            telegram_send.send(messages=["CHANGE IN RESPONSE FOR MONTH 4! NEW RESPONSE:", data])
        nextMonth = 5
    elif nextMonth == 5:
        if len(data) != 58:
            telegram_send.send(messages=["CHANGE IN RESPONSE FOR MONTH 5! NEW RESPONSE:", data])
        nextMonth = 6
    else:
        if len(data) != 58:
            telegram_send.send(messages=["CHANGE IN RESPONSE FOR MONTH 6! NEW RESPONSE:", data])
        nextMonth = 4
    time.sleep(60)
