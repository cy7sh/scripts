#!/usr/bin/env python3

import telegram_send
import requests
import time
import xml.etree.ElementTree as ET

def findData(root):
    for child in root:
        if child.tag == "data":
            return child.text
        # check if child has data
        data = findData(child)
        if data != None:
            return data

session = requests.session()

burp0_url = "https://wsr.pearsonvue.com:443/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE/2022238"
burp0_cookies = {"JSESSIONID": "DAE3F1D9354A3F54F1D0CB45A3221CB4", "oam.Flash.RENDERMAP.TOKEN": "-dehrsxuwz", "wg-startOverUrl": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "wg-externalAuth": "true", "wg-clientCode": "PEARSONLANGUAGE", "singleSignOnTimeoutURL": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "BIGipServer~managed~prd_wsr_pool_blue": "!AwlD3VgXplxBupVBP6jH124VbQXmHzhj2VRe8LGKcxKqwOvrmgjECXLeU4xsQzAAQsQjZX26CAxbMHoNHrXFLASgRYsFIINk5n1L0ier", "__uzma": "11d8d67f-e9a3-4b76-a129-43dc6fab2a96", "__uzmb": "1647251514", "__uzmc": "145751933278", "__uzmd": "1647251632"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Faces-Request": "partial/ajax", "Origin": "https://wsr.pearsonvue.com", "Dnt": "1", "Referer": "https://wsr.pearsonvue.com/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE?conversationId=2022238", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
burp0_data = {"geoCodeLatitude": "27.6280864", "geoCodeLongitude": "83.4748498", "threeCharCountryCode": '', "fullAddress": "Alfa Beta Complex, 1st floor, New Baneshwor, Kathmandu, Bagmati, Kathmandu, 44600, Nepal", "geoCodeTwoCharCountryCode": '', "preferredDateHidden": "06/29/2022", "resultCardID": "5", "preferredDateHidden_1": '', "preferredDateHiddenForAriaLabel_1": "07/07/2022", "preferredDateShown_1": "07 July 2022", "appt_menu_1": "1657224000000:71336", "preferredDateHidden_2": '', "preferredDateHiddenForAriaLabel_2": "07/08/2022", "preferredDateShown_2": "08 July 2022", "appt_menu_2": "1657323000000:81358", "preferredDateHidden_3": '', "preferredDateHiddenForAriaLabel_3": "07/10/2022", "preferredDateShown_3": "10 July 2022", "appt_menu_3": "1657456200000:47729", "preferredDateHidden_4": '', "preferredDateHiddenForAriaLabel_4": "07/18/2022", "preferredDateShown_4": "18 July 2022", "appt_menu_4": "1658152800000:85564", "preferredDateHidden_5": '', "preferredDateHiddenForAriaLabel_5": "06/29/2022", "preferredDateShown_5": "29 June 2022", "appt_menu_5": "1656514800000:83406", "combinedtestCenterFormId_SUBMIT": "1", "javax.faces.ViewState": "JcSezaj+H068eJqYf6yD6l2iCT5PNJ6HhH28rjNBkO/+v/Ac", "year": "2022", "month": "6", "testCenterId": "71336", "org.richfaces.ajax.component": "j_id_43_1_1_0_1_2", "j_id_43_1_1_0_1_2": "j_id_43_1_1_0_1_2", "rfExt": "null", "AJAX:EVENTS_COUNT": "1", "javax.faces.partial.event": "undefined", "javax.faces.source": "j_id_43_1_1_0_1_2", "javax.faces.partial.ajax": "true", "javax.faces.partial.execute": "@component", "javax.faces.partial.render": "@component", "combinedtestCenterFormId": "combinedtestCenterFormId"}

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
