from src.common import sleep, typeText
from src.account import Account
import pyautogui as py
import time

accounts = []

def makeAccount(name,password,mail):
    account = Account(name,password,mail)
    return account

def getAccountList():
    with open('accounts.txt') as f:
        accountLines = f.read().splitlines()
    for _ in accountLines:
        parts = _.split(':')
        accounts.append(makeAccount(parts[0], parts[1], parts[2]))
        parts.clear()
    return accounts

def run(channel):
    accounts = getAccountList()
    for account in accounts:
        #profile icon
        py.click(1900,100)
        time.sleep(1)
        #log in
        py.click(1800,200)
        sleep()
        #username
        py.click(1000,500)
        sleep()
        typeText(account.name)



def chat(channel):
    run(channel)
