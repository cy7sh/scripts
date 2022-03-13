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

burp0_url = "https://wsr.pearsonvue.com:443/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE/1875888"
burp0_cookies = {"JSESSIONID": "6332D4DB1711A1E3EB243D345612CA6B", "oam.Flash.RENDERMAP.TOKEN": "143y3tn4lr", "wg-startOverUrl": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "wg-externalAuth": "true", "wg-clientCode": "PEARSONLANGUAGE", "singleSignOnTimeoutURL": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "BIGipServer~managed~prd_wsr_pool_blue": "!QUZK1PlMGJ03rBZBP6jH124VbQXmHw+ejM2W96WZfoFc0IgO9mJzFT/J4aP9jXtPGR9Q0P3j8HWheWBIw780ZmPLGK5+Tgxi8C9jKWha", "__uzma": "e5db6fb3-6e35-4999-b26a-0599d9550e46", "__uzmb": "1647171071", "__uzmc": "874801951642", "__uzmd": "1647171133"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Faces-Request": "partial/ajax", "Origin": "https://wsr.pearsonvue.com", "Dnt": "1", "Referer": "https://wsr.pearsonvue.com/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE?conversationId=1875888", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
burp0_data = {"geoCodeLatitude": "27.6280864", "geoCodeLongitude": "83.4748498", "threeCharCountryCode": '', "fullAddress": "Alfa Beta Complex, 1st floor, New Baneshwor, Kathmandu, Bagmati, Kathmandu, 44600, Nepal", "geoCodeTwoCharCountryCode": '', "preferredDateHidden": "06/29/2022", "resultCardID": "5", "preferredDateHidden_1": '', "preferredDateHiddenForAriaLabel_1": "07/08/2022", "preferredDateShown_1": "08 July 2022", "appt_menu_1": "1657310400000:71336", "preferredDateHidden_2": '', "preferredDateHiddenForAriaLabel_2": "07/08/2022", "preferredDateShown_2": "08 July 2022", "appt_menu_2": "1657323000000:81358", "preferredDateHidden_3": '', "preferredDateHiddenForAriaLabel_3": "07/08/2022", "preferredDateShown_3": "08 July 2022", "appt_menu_3": "1657283400000:47729", "preferredDateHidden_4": '', "preferredDateHiddenForAriaLabel_4": "07/15/2022", "preferredDateShown_4": "15 July 2022", "appt_menu_4": "1657893600000:85564", "preferredDateHidden_5": '', "preferredDateHiddenForAriaLabel_5": "06/29/2022", "preferredDateShown_5": "29 June 2022", "appt_menu_5": "1656514800000:83406", "combinedtestCenterFormId_SUBMIT": "1", "javax.faces.ViewState": "YUA761Fnzvh/WBVShJpfZo46NvUwyHJZ621QCBl5BFynvifx", "year": "2022", "month": "6", "testCenterId": "71336", "org.richfaces.ajax.component": "j_id_43_1_1_0_1_2", "j_id_43_1_1_0_1_2": "j_id_43_1_1_0_1_2", "rfExt": "null", "AJAX:EVENTS_COUNT": "1", "javax.faces.partial.event": "undefined", "javax.faces.source": "j_id_43_1_1_0_1_2", "javax.faces.partial.ajax": "true", "javax.faces.partial.execute": "@component", "javax.faces.partial.render": "@component", "combinedtestCenterFormId": "combinedtestCenterFormId"}

prevDataMonth4 = ""
prevDataMonth5 = ""
nextMonth = 4

while True:
    burp0_data["month"] = str(nextMonth)

    request = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    root = ET.fromstring(request.text)
    data = findData(root)
    if data == None:
        telegram_send.send(messages=["SESSION EXPIRED PLEASE UPDATE! BOT SHUTTING DOWN."])
        break
    # confirmation sake
    print(data)

    if nextMonth == 4:
        if data != prevDataMonth4:
            telegram_send.send(messages=["CHANGE IN REQUEST FOR MONTH 4! NEW REQUEST:", data])
        prevDataMonth4 = data
        nextMonth = 5
    else:
        if data != prevDataMonth5:
            telegram_send.send(messages=["CHANGE IN REQUEST FOR MONTH 5! NEW REQUEST:", data])
        prevDataMonth5 = data
        nextMonth = 4
    time.sleep(300)
