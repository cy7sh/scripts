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

burp0_url = "https://wsr.pearsonvue.com:443/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE/1845065"
burp0_cookies = {"JSESSIONID": "2B099BF1E55453E84D5BDB7B7AA0AA01", "oam.Flash.RENDERMAP.TOKEN": "fvrh3zq4a", "wg-startOverUrl": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "wg-externalAuth": "true", "wg-clientCode": "PEARSONLANGUAGE", "singleSignOnTimeoutURL": "https%3A%2F%2Fmypte.pearsonpte.com%2Ftimeout", "BIGipServer~managed~prd_wsr_pool_blue": "!bC0vlgjZRKocYztBP6jH124VbQXmHx58m/MhTdJ/OdJxMt4Fs3m2/W+CEO/zWVeEQh3402fHO3McXohlIdZ0dPPGPN7L3ephO+dPI9Dj", "__uzma": "77fe0092-4265-42bf-ac58-bfd3122e67e1", "__uzmb": "1647143021", "__uzmc": "391641937004", "__uzmd": "1647143085"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Faces-Request": "partial/ajax", "Origin": "https://wsr.pearsonvue.com", "Dnt": "1", "Referer": "https://wsr.pearsonvue.com/testtaker/registration/CombinedTestCenterSearchPage/PEARSONLANGUAGE?conversationId=1845065", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
burp0_data = {"geoCodeLatitude": "27.6280864", "geoCodeLongitude": "83.4748498", "threeCharCountryCode": '', "fullAddress": "Alfa Beta Complex, 1st floor, New Baneshwor, Kathmandu, Bagmati, Kathmandu, 44600, Nepal", "geoCodeTwoCharCountryCode": '', "preferredDateHidden": "06/29/2022", "resultCardID": "5", "preferredDateHidden_1": '', "preferredDateHiddenForAriaLabel_1": "07/07/2022", "preferredDateShown_1": "07 July 2022", "appt_menu_1": "1657206000000:71336", "preferredDateHidden_2": '', "preferredDateHiddenForAriaLabel_2": "07/07/2022", "preferredDateShown_2": "07 July 2022", "appt_menu_2": "1657193400000:81358", "preferredDateHidden_3": '', "preferredDateHiddenForAriaLabel_3": "07/07/2022", "preferredDateShown_3": "07 July 2022", "appt_menu_3": "1657221300000:47729", "preferredDateHidden_4": '', "preferredDateHiddenForAriaLabel_4": "07/14/2022", "preferredDateShown_4": "14 July 2022", "appt_menu_4": "1657807200000:85564", "preferredDateHidden_5": '', "preferredDateHiddenForAriaLabel_5": "06/29/2022", "preferredDateShown_5": "29 June 2022", "appt_menu_5": "1656514800000:83406", "combinedtestCenterFormId_SUBMIT": "1", "javax.faces.ViewState": "Fky6qYQDCrUJWSONkzyxc4czyPKTajN4Nby91ETUnVedbnxC", "year": "2022", "month": "6", "testCenterId": "71336", "org.richfaces.ajax.component": "j_id_43_1_1_0_1_2", "j_id_43_1_1_0_1_2": "j_id_43_1_1_0_1_2", "rfExt": "null", "AJAX:EVENTS_COUNT": "1", "javax.faces.partial.event": "undefined", "javax.faces.source": "j_id_43_1_1_0_1_2", "javax.faces.partial.ajax": "true", "javax.faces.partial.execute": "@component", "javax.faces.partial.render": "@component", "combinedtestCenterFormId": "combinedtestCenterFormId"}

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
