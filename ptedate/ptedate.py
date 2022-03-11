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

#telegram_send.send(messages=["-------------BOT STARTED {} -------------".format(datetime.datetime.now())])

session = requests.session()

burp0_url = "https://wsr.pearsonvue.com:443/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE/1704691"
burp0_cookies = {"JSESSIONID": "4A0730DD37F0A332E9329DB21CA40786", "oam.Flash.RENDERMAP.TOKEN": "-182c4lv9ad", "wg-startOverUrl": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "wg-externalAuth": "true", "wg-clientCode": "PEARSONLANGUAGE", "singleSignOnTimeoutURL": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "BIGipServer~managed~prd_wsr_pool_blue": "!f/ALehpp1yHPPhlBP6jH124VbQXmHwAzj73aU6ERn9tmjA3D70VJF/1cXSG3OpuOc16jTd3QsJkWuWUagVzwLS/4Dl0H+bTaOZn0biZd", "__uzma": "7cc5103b-2429-42b2-8b53-e3a8f8968d1e", "__uzmb": "1646999745", "__uzmc": "940592549051", "__uzmd": "1646999998"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Faces-Request": "partial/ajax", "Origin": "https://wsr.pearsonvue.com", "Dnt": "1", "Referer": "https://wsr.pearsonvue.com/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE?conversationId=1704691", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
burp0_data = {"geoCodeLatitude": "27.6280864", "geoCodeLongitude": "83.4748498", "threeCharCountryCode": '', "fullAddress": "Alfa Beta Complex, 1st floor, New Baneshwor, Kathmandu, Bagmati, Kathmandu, 44600, Nepal", "geoCodeTwoCharCountryCode": '', "preferredDateHidden": "06/29/2022", "resultCardID": "5", "preferredDateHidden_1": '', "preferredDateHiddenForAriaLabel_1": "06/30/2022", "preferredDateShown_1": "30 June 2022", "preferredDateHidden_2": '', "preferredDateHiddenForAriaLabel_2": "07/06/2022", "preferredDateShown_2": "06 July 2022", "appt_menu_2": "1657107000000:81358", "preferredDateHidden_3": '', "preferredDateHiddenForAriaLabel_3": "07/07/2022", "preferredDateShown_3": "07 July 2022", "appt_menu_3": "1657197000000:47729", "preferredDateHidden_4": '', "preferredDateHiddenForAriaLabel_4": "07/13/2022", "preferredDateShown_4": "13 July 2022", "appt_menu_4": "1657738800000:85564", "preferredDateHidden_5": '', "preferredDateHiddenForAriaLabel_5": "06/29/2022", "preferredDateShown_5": "29 June 2022", "appt_menu_5": "1656514800000:83406", "combinedtestCenterFormId_SUBMIT": "1", "javax.faces.ViewState": "y6vIeVnYuXTOGtQQmiq3ssAB42bQYPNRfNFwBvyqelV0qBCe", "year": "2022", "month": "4", "testCenterId": "71336", "org.richfaces.ajax.component": "j_id_43_1_1_0_1_2", "j_id_43_1_1_0_1_2": "j_id_43_1_1_0_1_2", "rfExt": "null", "AJAX:EVENTS_COUNT": "1", "javax.faces.partial.event": "undefined", "javax.faces.source": "j_id_43_1_1_0_1_2", "javax.faces.partial.ajax": "true", "javax.faces.partial.execute": "@component", "javax.faces.partial.render": "@component", "combinedtestCenterFormId": "combinedtestCenterFormId"}

prevData = ""
nextMonth = 4
while True:
    burp0_data["month"] = str(nextMonth)
    if nextMonth == 4:
        nextMonth = 5
    else:
        nextMonth = 4

    request = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    root = ET.fromstring(request.text)
    data = findData(root)
    # confirmation sake
    print(data)
    if data != prevData:
        telegram_send.send(messages=["CHANGE IN REQUEST FOR MONTH {}! NEW REQUEST:".format(nextMonth), data])
    prevData = data
    time.sleep(5)
