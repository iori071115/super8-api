import mo 
import payload as pl
import json
import time
import requests as req


env = mo.read_jsonfile()

def test_add_tag():
    url = f"{env['parse-url']}/functions/tagging"
    payload = { 
                "message": {
                            "apitag": True
                            },
                "where": {
                    "customer": {
                    "customerId": f"{env['test-customerId']}"
                    },
                    "organization": {
                    "className": "Organization",
                    "objectId": f"{env['test-organizationId']}"
                    }
                },
                "options": {
                    "version": 2
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    assert "apitag" in mo.check_customer_info()["tag"]

def test_delete_tag():
    url = f"{env['parse-url']}/functions/tagging"
    payload = { 
                "message": {"apitag": True},
                "method": "DELETE",
                "where": {
                    "customer": {
                    "customerId": f"{env['test-customerId']}"
                    },
                    "organization": {
                    "className": "Organization",
                    "objectId": f"{env['test-organizationId']}"
                    }
                },
                "options": {
                    "version": 2
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    req.post(url,json=payload)
    assert "apitag" not in mo.check_customer_info()["tag"]

def test_sand_options_card():
      url = f"{env['parse-url']}/functions/publishTemplate"
      payload = {
                     "template":{
                     "className":"Template",
                     "templateType":"card",
                     "name":"選項型卡片4種按鈕",
                     "data":{
                     "elements":[
                     {
                     "goodsURL":"",
                     "imageType":"upload",
                     "imageUrl":"",
                     "title":"預設回覆文字",
                     "subtitle":"1",
                     "buttons":[
                     {
                     "type":"postback",
                     "title":"文字",
                     "data":"文字",
                     "tags":[
                     ]
                     }
                     ]
                     },
                     {
                     "goodsURL":"",
                     "imageType":"upload",
                     "imageUrl":"",
                     "title":"預設回覆網址",
                     "subtitle":"2",
                     "buttons":[
                     {
                     "type":"url",
                     "title":"網址",
                     "data":"https://no8.io",
                     "tags":[
                     ]
                     }
                     ]
                     },
                     {
                     "goodsURL":"",
                     "imageType":"upload",
                     "imageUrl":"",
                     "title":"預設回覆通話",
                     "subtitle":"3",
                     "buttons":[
                     {
                     "type":"phone",
                     "title":"通話",
                     "data":"+886912345678",
                     "tags":[
                     ]
                     }
                     ]
                     },
                     {
                     "goodsURL":"",
                     "imageType":"upload",
                     "imageUrl":"",
                     "title":"預設回覆位置",
                     "subtitle":"4",
                     "buttons":[
                     {
                     "type":"location",
                     "title":"位置",
                     "data":"",
                     "tags":[
                     ]
                     }
                     ]
                     }
                     ],
                     "templateType":"card"
                     },
                     "organization":{
                     "__type":"Pointer",
                     "className":"Organization",
                     "objectId":f"{env['test-organizationId']}"
                     },
                     "hidden":False,
                     "version":2
                     },
                     "conversation":{
                     "__type":"Pointer",
                     "className":"Conversation",
                     "objectId":f"{env['test-conversationId']}"
                     },
                     "_ApplicationId": f"{env['parse-app-id']}",
                     "_JavaScriptKey": "javascriptKey",
                     "_ClientVersion":"js1.11.1",
                     "_SessionToken": f"{env['sessionToken']}"
                  }
      req.post(url,json=payload)
      assert mo.check_customer_message()[0]["data"]["name"] == "選項型卡片4種按鈕"

def test_confirm_created_options_card():
    url =  f"{env['parse-url']}/functions/queryTemplate"
    payload = {
                "where": {
                          "organization": {
                          "__type": "Pointer",
                          "className": "Organization",
                          "objectId": f"{env['test-organizationId']}"
                                            },
                           "vendor": {"$ne": True }},
                           "skip": 0,
                           "limit": 50,
                           "sort": {"createdAt": -1},
                           "group": True,
                           "_ApplicationId": f"{env['parse-app-id']}",
                           "_JavaScriptKey": "javascriptKey",
                           "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    env["test-templateId-long"] = res.json()["result"][0]["_id"]
    mo.write_jsonfile (env)
    assert mo.read_jsonfile()["test-templateId-long"] == res.json()["result"][0]["_id"]

def test_delete_Template_options_card():
     url =  f"{env['parse-url']}/functions/removeTemplate"
     payload = {
                "templateId": f"{env['test-organizationId']}",
                "organization": {
                    "__type": "Pointer",
                    "className": "Organization",
                    "objectId": f"{env['test-organizationId']}"
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_ClientVersion": "js1.11.1",
                "_SessionToken": f"{env['sessionToken']}"
                }
     res = req.post(url,json=payload)
     assert res.status_code == 200

def test_sand_confirm_card():
    url = f"{env['parse-url']}/functions/publishTemplate"
    payload = {
                "template": {
                            "className": "Template",
                            "templateType": "confirm",
                            "name": "確認型卡片位置按鈕",
                            "data": {
                                        "elements": [
                            {
                            "title": "確認型卡片按鈕測試",
                            "buttons": [
                                        {
                                        "type": "url",
                                        "title": "確認型卡片網址按鈕",
                                        "data": "https://no8.io",
                                        "tags": []
                                    },
                                {
                                        "type": "location",
                                        "title": "確認型卡片位置按鈕",
                                        "data": "",
                                        "tags": []
                                                        }
                                                    ]
                                                }
                                            ],
                                            "templateType": "confirm"
                                        },
                                        "organization": {
                                            "__type": "Pointer",
                                            "className": "Organization",
                                            "objectId": f"{env['test-organizationId']}"
                                        },
                                        "hidden": True
                                },
                            "options": {},
                            "conversation": {
                                                "__type": "Pointer",
                                                "className": "Conversation",
                                                "objectId": f"{env['test-conversationId']}"
                            },
                            "_ApplicationId": f"{env['parse-app-id']}",
                            "_JavaScriptKey": "javascriptKey",
                            "_ClientVersion": "js1.11.1",
                            "_SessionToken": f"{env['sessionToken']}"
        }
    req.post(url,json=payload)
    assert mo.check_customer_message()[0]["data"]["name"] == "確認型卡片位置按鈕"

def test_sand_images_card():
    url = f"{env['parse-url']}/functions/publishTemplate"
    payload = {
                "template": {
                    "className": "Template",
                    "templateType": "image",
                    "name": "多頁大圖-4種按鈕",
                    "data": {
                        "elements": [
                            {
                                "goodsURL": "",
                                "imageType": "upload",
                                "imageUrl": "https://assets.no8.io/app-api-uploader/stag/1661828623147/960x500_SS%E5%8F%B0%E7%81%A3_%E5%AE%9C%E8%98%AD_%E5%A4%AA%E5%B9%B3%E5%B1%B1_004_%E6%A5%93%E8%91%89%E6%AD%A5%E9%81%93.jpg",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "多頁大圖文字",
                                        "data": "多頁大圖文字",
                                        "tags": []
                                    }
                                ],
                                "aspectRatio": "1.92:1"
                            },
                            {
                                "goodsURL": "",
                                "imageType": "upload",
                                "imageUrl": "https://assets.no8.io/app-api-uploader/stag/1661828634168/960x500_SS%E5%8F%B0%E7%81%A3_%E5%AE%9C%E8%98%AD_%E5%A4%AA%E5%B9%B3%E5%B1%B1_011_%E8%A6%8B%E6%99%B4%E6%87%B7%E5%8F%A4%E6%AD%A5%E9%81%93.jpg",
                                "buttons": [
                                    {
                                        "type": "url",
                                        "title": "",
                                        "data": "https://no8.io",
                                        "tags": []
                                    }
                                ],
                                "aspectRatio": "1.92:1"
                            },
                            {
                                "goodsURL": "",
                                "imageType": "upload",
                                "imageUrl": "https://assets.no8.io/app-api-uploader/stag/1661828646707/960x960_SS%E5%8F%B0%E7%81%A3_%E5%AE%9C%E8%98%AD_%E5%A4%AA%E5%B9%B3%E5%B1%B1_004_%E6%A5%93%E8%91%89%E6%AD%A5%E9%81%93.jpg",
                                "buttons": [
                                    {
                                        "type": "phone",
                                        "title": "",
                                        "data": "+886912345678",
                                        "tags": []
                                    }
                                ],
                                "aspectRatio": "1:1"
                            },
                            {
                                "goodsURL": "",
                                "imageType": "upload",
                                "imageUrl": "https://assets.no8.io/app-api-uploader/stag/1661828677562/960x500_SS%E5%8F%B0%E7%81%A3_%E5%AE%9C%E8%98%AD_%E5%A4%AA%E5%B9%B3%E5%B1%B1_010_%E5%B1%B1%E6%AF%9B%E6%AB%B8.jpg",
                                "buttons": [
                                    {
                                        "type": "location",
                                        "title": "",
                                        "data": "",
                                        "tags": []
                                    }
                                ],
                                "aspectRatio": "1.92:1"
                            }
                        ],
                        "templateType": "image"
                    },
                    "organization": {
                        "__type": "Pointer",
                        "className": "Organization",
                        "objectId": f"{env['test-organizationId']}"
                    },
                    "hidden": True
                },
                "options": {},
                "conversation": {
                    "__type": "Pointer",
                    "className": "Conversation",
                    "objectId": f"{env['test-conversationId']}"
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_ClientVersion": "js1.11.1",
                "_SessionToken": f"{env['sessionToken']}"
                }
    req.post(url,json=payload)
    assert mo.check_customer_message()[0]["data"]["name"] == "多頁大圖-4種按鈕"

def test_add_template_options_card():
    url = f"{env['parse-url']}/functions/publishTemplate"
    payload = {
                "template": {
                    "className": "Template",
                    "templateType": "card",
                    "name": "預設回覆-選項",
                    "data": {
                        "elements": [
                            {
                                "title": "new1",
                                "subtitle": "1",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "new2",
                                        "data": "new2",
                                        "tags": [
                                            "2"
                                        ]
                                    }
                                ]
                            }
                        ],
                        "templateType": "card"
                    },
                    "organization": {
                        "__type": "Pointer",
                        "className": "Organization",
                        "objectId": f"{env['test-organizationId']}"
                    },
                    "hidden": False
                },
                "options": {},
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_ClientVersion": "js1.11.1",
                "_SessionToken": f"{env['sessionToken']}"
            }
    res = req.post(url,json=payload)
    env["test-templateId-long"] = res.json()["result"]["templateId"]
    env["test-templateId"] = res.json()["result"]["template"]
    mo.write_jsonfile (env)
    assert mo.read_jsonfile()["test-templateId-long"] == res.json()["result"]["templateId"]
    assert mo.read_jsonfile()["test-templateId"] == res.json()["result"]["template"]

def test_add_template_confirm_card():
    url = f"{env['parse-url']}/functions/publishTemplate"
    payload = {
                "template": {
                "className": "Template",
                "templateType": "confirm",
                "name": "預設回覆-確認",
                "data": {
                    "elements": [
                        {
                            "title": "confirm_card_title",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "aaa",
                                    "data": "aaa"
                                },
                                {
                                    "type": "postback",
                                    "title": "bbb",
                                    "data": "bbb"
                                }
                            ]
                        }
                    ],
                    "templateType": "confirm"
                },
                "organization": {
                    "__type": "Pointer",
                    "className": "Organization",
                    "objectId": f"{env['test-organizationId']}"
                },
                "hidden": False
                },
                "options": {},
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_ClientVersion": "js1.11.1",
                "_SessionToken": f"{env['sessionToken']}"
            }
    res = req.post(url,json=payload)
    env["test-templateId-confirm-long"] = res.json()["result"]["templateId"]
    env["test-templateId-confirm"] = res.json()["result"]["template"]
    mo.write_jsonfile (env)
    assert mo.read_jsonfile()["test-templateId-confirm-long"] == res.json()["result"]["templateId"]
    assert mo.read_jsonfile()["test-templateId-confirm"] == res.json()["result"]["template"]

def test_check_template_card():
    url =  f"{env['parse-url']}/functions/queryTemplate"
    payload = pl.queryTemplate_options_card()
    res = req.post(url,json=payload)
    assert res.json()["result"][0]["objectId"] == env["test-templateId"]
    assert res.json()["result"][0]["name"] == "預設回覆-選項"
    
    payload = pl.queryTemplate_confirm_card()
    res = req.post(url,json=payload)
    assert res.json()["result"][0]["objectId"]  == env["test-templateId-confirm"]
    assert res.json()["result"][0]["name"] == "預設回覆-確認"

def test_sand_line_massage_for_favorites():
    mt = "message"
    message = "測試收藏"
    url =  f"{env['test-mes-url']}/line/gun/{env['test-organizationId']}"
    payload = pl.sand_line_message(mt,message)
    res = req.post(url,json=payload)
    assert mo.check_customer_message()[0]["data"]["content"] == message

def test_add_favorites():
    env['test-tmp'] = mo.check_customer_message()[0]["objectId"]
    url = f"{env['parse-url']}/functions/keep"
    payload = pl.functions_keep(env['test-tmp'])
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_delete_favorites():
    url = f"{env['parse-url']}/classes/KeptMessage/{env['test-accountId']}{env['test-tmp']}"
    payload = {    
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}",
                "_method": "DELETE",
                }
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_get_unfollow_count():
    env['test-tmp'] = mo.functions_inboxesV3()["unfollow"]
    mo.write_jsonfile(env)
    assert env['test-tmp'] == mo.functions_inboxesV3()["unfollow"]

def test_unfollow_line_event():
    x = 1
    mt = "unfollow"
    message = "unfollow event"
    while x <= 2:
        message = "unfollow event"
        url =  f"{env['test-mes-url']}/line/gun/{env['test-organizationId']}"
        payload = pl.sand_line_message(mt,message)
        res = req.post(url,json=payload)
        x+=1
    assert res.status_code == 200

def test_confirm_unfollow_puls_one():
    env['test-tmp']=mo.read_jsonfile()['test-tmp']+1
    mo.write_jsonfile(env)
    assert mo.functions_inboxesV3()["unfollow"] == mo.read_jsonfile()['test-tmp']

def test_confirm_lock_user_has_photo():
    url =  f"{env['parse-url']}/classes/Customer"
    payload = pl.classes_customer()
    res = req.post(url,json=payload)
    assert res.json()['results'][0]['picture'] != ""

def test_follow_line_event():
    x = 1
    mt = "follow"
    message = "follow event"
    while x <= 2:
        message = "unfollow event"
        url =  f"{env['test-mes-url']}/line/gun/{env['test-organizationId']}"
        payload = pl.sand_line_message(mt,message)
        res = req.post(url,json=payload)
        x+=1
    assert res.status_code == 200

def test_Confirm_unfollow_minus_one ():
    assert mo.functions_inboxesV3()["unfollow"] == mo.read_jsonfile()['test-tmp']-1

def test_confirm_unlock_user_has_photo():
    url =  f"{env['parse-url']}/classes/Customer"
    payload = pl.classes_customer()
    res = req.post(url,json=payload)
    assert res.json()['results'][0]['picture'] != ""

def test_delete_custom_field():
    url = f"{env['parse-url']}/functions/updateCustomFields"
    payload = {
                "where": {
                    "orgId": f"{env['test-organizationId']}"
                },
                "fields": [],
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    assert res.json()["result"]["ok"] == True

def test_confirm_custom_field_is_empty():
    assert mo.superapi_get_customer_info()["data"]["customers"][0]["extra"] == {}

def test_created_edit_custom_field():
    url = f"{env['parse-url']}/functions/updateCustomFields"
    payload = pl.functions_updateCustomFields("客製化欄位1")
    res = req.post(url,json=payload)
    assert res.json()["result"]["ok"] == True

def test_set_custom_field():
    url = f"{env['parse-url']}/classes/Customer/{env['test-user-objectId']}"
    payload = {
                "objectId": f"{env['test-organizationId']}",
                "displayName": f"{env['test-search-user']}",
                "cellPhone": "",
                "birthday": {
                    "iso": "1984-07-10T16:00:00.000Z",
                    "__type": "Date"
                },
                "gender": "male",
                "externalTag": {},
                "extra": {
                    "45dfd088-241c-43e2-a42d-1beb5f4eac88": "設定1"
                },
                "_method": "PUT",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                 }
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_confirm_custom_field():
    assert mo.superapi_get_customer_info()["data"]["customers"][0]["extra"]["客製化欄位1"] == "設定1"


def test_assign_to_a_member():
    url = f"{env['parse-url']}/functions/assign"
    payload = pl.functions_assign_for_private()
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_confirm_customer_was_assigned():
    result = mo.confirm_customer_stutas()
    assert env['test-adm-objectId_1'] in result[0]["inbox"]   

def test_complete_conversation():
    url = f"{env['parse-url']}/functions/assign"
    payload = pl.functions_assign("done")
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_confirm_complete_conversation():
    result = mo.confirm_customer_stutas()
    assert "done" in result[0]["inbox"]

def test_move_to_the_unassigned():
    url = f"{env['parse-url']}/functions/assign"
    payload = pl.functions_assign("unassigned")
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_confirm_move_to_the_unassigned():
    result = mo.confirm_customer_stutas()
    assert "unassigned"  in result[0]["inbox"]