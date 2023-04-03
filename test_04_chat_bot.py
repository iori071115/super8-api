import mo 
import payload as pl
import json
import time
import requests as req

env = mo.read_jsonfile()

def test_sand_line_massage1():
    mt = "message"
    message = "流程1:被顧客傳送內容觸發"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["content"] == f"嗨，{env['test-search-user']} 您好！"
    assert check[1]["contentType"] == "application/x-video"
    assert check[2]["contentType"] == "application/x-image"
    assert check[3]["data"]["content"] == "流程2:被其他流程觸發_回應文字"
    assert check[4]["data"]["elements"][0]["buttons"][0]["title"] == "開發者回傳 Button"
    assert check[4]["data"]["elements"][0]["buttons"][0]["data"] == "回傳Button"
    assert check[4]["data"]["elements"][0]["buttons"][1]["title"] == "位置Button"
    assert check[4]["data"]["elements"][0]["buttons"][1]["data"] == "位置Button"
    assert check[5]["data"]["elements"][0]["buttons"][0]["title"] == "電話"
    assert check[5]["data"]["elements"][0]["buttons"][0]["data"] == "0933333333"
    assert check[5]["data"]["elements"][0]["buttons"][1]["title"] == "開發者webview Button"
    assert check[5]["data"]["elements"][0]["buttons"][1]["data"] == "http://tw.yahoo.com"
    assert check[6]["data"]["elements"][0]["buttons"][0]["title"] == "Bot 回應文字"
    assert check[6]["data"]["elements"][0]["buttons"][0]["data"] == "Bot 回應文字"
    assert check[6]["data"]["elements"][0]["buttons"][1]["title"] == "Button"
    assert check[6]["data"]["elements"][0]["buttons"][1]["data"] == "http://www.google.com"
    assert check[7]["data"]["elements"][0]["buttons"][0]["title"] == "Button"
    assert check[7]["data"]["elements"][0]["buttons"][0]["data"] == "https://www.google.com"
    assert check[7]["data"]["elements"][0]["buttons"][1]["title"] == "通話按鈕"
    assert check[7]["data"]["elements"][0]["buttons"][1]["data"] == "0966666666"
    assert check[7]["data"]["elements"][0]["buttons"][2]["title"] == "Bot 回應文字"
    assert check[7]["data"]["elements"][0]["buttons"][2]["data"] == "Bot 回應文字"
    assert check[7]["data"]["elements"][1]["buttons"][0]["title"] == "開發者webview Button"
    assert check[7]["data"]["elements"][1]["buttons"][0]["data"] == "http://tw.yahoo.com"
    assert check[7]["data"]["elements"][1]["buttons"][1]["title"] == "開發者回傳 Button"
    assert check[7]["data"]["elements"][1]["buttons"][1]["data"] == "回傳Button"
    assert check[7]["data"]["elements"][1]["buttons"][2]["title"] == "位置Button"

def test_sand_line_massage2():
    mt = "message"
    message = "gotostep"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True

def test_sand_line_massage3():
    mt = "message"
    message = "發送訊息"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["content"] == "請輸入您的預約日期："

def test_sand_line_massage4():
    mt = "message"
    message = "2021/01/01"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["content"] == "請回應:是 or 否"

def test_sand_line_massage5():
    mt = "message"
    message = "2021/01/01"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["content"] == "請回應:是 or 否"

def test_sand_line_massage5():
    mt = "message"
    message = "否"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["content"] == "請輸入您的預約日期："

def test_sand_line_massage6():
    mt = "message"
    message = "2020/12/30"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["content"] == "請回應:是 or 否"

def test_sand_line_massage7():
    mt = "message"
    message = "是"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["content"] == "請按下列三個選項"

def test_sand_line_massage8():
    mt = "message"
    message = "按鈕B"
    sand = mo.sand_line_massage(mt,message)
    time.sleep(1.5)
    check = mo.check_customer_message()
    assert sand["ok"] == True
    assert check[0]["data"]["content"] == "Done"

def test_delete_taging():
    url = f"{env['parse-url']}/functions/tagging"
    paylaod = {
                "message": {"按鈕B": True},
                "where": {"customer": {"customerId": f"{env['test-customerId']}"},
                          "organization": {"className": "Organization",
                                           "objectId": f"{env['test-organizationId']}"}},
                "options": {"version": 2},
                "method": "DELETE",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}",
                }
    res = req.post(url,json=paylaod)
    assert res.json()["result"]["ok"] == True
    assert  "按鈕B" not in mo.check_customer_info()["tag"]

def test_move_to_unassigned():
    url = f"{env['parse-url']}/functions/assign"
    paylaod = {
                "inbox": "unassigned",
                "from": {"className": "_User",
                         "objectId": f"{env['test-adm-objectId_2']}"},
                "customer": {"className": "Customer",
                             "objectId": f"{env['test-user-objectId']}"},
                "organization": {"className": "Organization",
                                 "objectId": f"{env['test-organizationId']}"},
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_ClientVersion": "js1.11.1",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=paylaod)
    assert res.json()["result"] == "done"

def test_webhook_trigger_bot():
    result = mo.webhook_trigger_event("輸入webhook關鍵字",123456)
    time.sleep(1.5)
    assert result["message"] == "ok"
    assert mo.check_customer_message()[0]["data"]["content"] == "嗨，此為webhook觸發訊息！\n123456 "

def test_special_characters_trigger_webhook():
    result = mo.webhook_trigger_event("+ /?%#&=@",123456)
    time.sleep(1.5)
    assert result["message"] == "ok"
    assert mo.check_customer_message()[0]["data"]["content"] == f"嗨，{env['test-organization-name']} 您好！\nwebhook特殊字元觸發成功\n輸入數字123456 "