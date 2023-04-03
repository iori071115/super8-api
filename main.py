import mo 
import json
import requests as req
import time
import payload as pl
from pprint import pprint as pp
import bcrypt

env = mo.read_jsonfile()

# class Point:
#     def __init__(self):
#         self.file = mo.read_jsonfile()

#     def test_file(self):
#         env = self.file
#         return env

# print(Point.test_file)


# t = mo.set_time(2)
# print(t)

plain_text = b'98cbabf7-9b47-4061-b5b9-b7d556e842e9'
hashed_text = b'$2a$12$xtj2nv5k.xrL6Q1pK9x8bOG4AEr4XS.o717EoKgLJhh02INQYxg..'

if bcrypt.checkpw(plain_text, hashed_text):
    print("Matched")
else:
    print("Not matched")

def test_sand_line_massage9():
    mt = "message"
    message = "LINE快速回覆"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["content"] == "LINE快速回覆按鈕"

def test_sand_line_massage10():
    mt = "message"
    message = "機器人關鍵字回應圖文訊息"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["elements"][0]["buttons"][0]["data"] == "機器人關鍵字回應圖文訊息"






