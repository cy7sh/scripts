#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from playsound import playsound

driver = webdriver.Chrome()
driver.get("https://mypte.pearsonpte.com/")
assert "myPTE" in driver.title

time.sleep(3)
# login
username_elm = driver.find_element(By.ID, "inputUsername")
password_elm = driver.find_element(By.ID, "inputPassword")
username_elm.clear()
username_elm.send_keys("shirishpokhrel1@gmail.com")
password_elm.clear()
password_elm.send_keys("sn0wBall")
password_elm.send_keys(Keys.RETURN)

time.sleep(10)
reschedule_link = driver.find_element(By.LINK_TEXT, "Reschedule")
reschedule_link.click()
time.sleep(15)

date_bt = driver.find_element(By.ID, "preferredDateShown_1")
date_bt.click()
time.sleep(2)

def wait_and_prev():
    time.sleep(3)
    check_avalability()
    prev_link = driver.find_element(By.XPATH, "//*[@id='datepicker_1']/div/div/a[1]/span")
    prev_link.click()

def wait_and_next():
    time.sleep(2)
    check_avalability()
    next_link = driver.find_element(By.XPATH, "//*[@id='datepicker_1']/div/div/a[2]/span")
    next_link.click()

def alarm():
    while True:
        playsound("./alarm.mp3")

def check_avalability():
    if not driver.find_element(By.ID, "warning_text_1").is_displayed():
        alarm()

def reload():
    driver.refresh()
    time.sleep(5)
    date_bt = driver.find_element(By.ID, "preferredDateShown_1")
    date_bt.click()
    time.sleep(2)

while True:
    try:
        wait_and_prev()
        wait_and_prev()
        wait_and_prev()

        wait_and_next()
        wait_and_next()
        wait_and_next()
        reload()
    except Exception as e:
        print(e)
        # wait for human intervention
        print("HUMAN INTERVENTION NEEDED!")
        alarm()
