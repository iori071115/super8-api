import mo 
import json
import requests as req
import time
env = mo.read_jsonfile()

def test_create_broadcast_for_Push_notifications():
    url = f"{env['test-next-url']}/broadcast/create"
    payload = {
                "name": "測試推播",
                "orgId": f"{env['test-organizationId']}",
                "query": {
                    "orgId":  f"{env['test-organizationId']}",
                    "platforms": [
                        "line"
                    ],
                    "customerObjectIds": [
                        f"{env['test-user-objectId']}"
                    ],
                    "tags": [],
                    "externalTag": [],
                    "partnerTag": []
                },
                "messages": [
                    {
                        "contentType": "text/plain",
                        "data": {
                            "content": "第二則文字"
                        },
                        "index": 1,
                        "version": 2
                    }
                ],
                "templates": [
                    {
                        "className": "Template",
                        "name": "預設回覆-確認",
                        "templateType": "confirm",
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
                        "index": 0,
                        "altText": "測試推播通知內容",
                        "version": 2
                    }
                ],
                "options": {
                    "name": "測試推播",
                    "applyFacebook24Policy": True,
                    "applyLineUnfollowFilter": True,
                    "customerNum": 1
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    env["test-broadcast_id"] = res.json()["taskId"]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-broadcast_id"] == res.json()["taskId"]

def test_manual_broadcast_for_designated_customer():
    url = f"{env['test-next-url']}/broadcast/create"
    payload = {
                "name": "文字＋圖片+卡片",
                "orgId": f"{env['test-organizationId']}",
                "query": {
                    "orgId": f"{env['test-organizationId']}",
                    "platforms": [
                        "line"
                    ],
                    "customerObjectIds": [
                        f"{env['test-user-objectId']}"
                    ],
                    "tags": []
                },
                "messages": [
                    {
                        "contentType": "text/plain",
                        "data": {
                            "content": "send message by v2 api <%=name%> 客戶姓名測試\n表情😁"
                        },
                        "index": 0,
                        "version": 2
                    },
                    {
                        "contentType": "application/x-image",
                        "data": {
                            "name": "截圖 2023-01-19 下午5.01.58.png",
                            "url": "https://assets.no8.io/app-api-uploader/stag/1675062622355/%E6%88%AA%E5%9C%96_2023-01-19_%E4%B8%8B%E5%8D%885.01.58.png",
                            "contentType": "image/png"
                        },
                        "index": 1,
                        "version": 2
                    }
                ],
                "templates": [
                    {
                        "className": "Template",
                        "name": "templateNameTest",
                        "templateType": "confirm",
                        "data": {
                            "elements": [
                                {
                                    "title": "確認型卡片 0216",
                                    "buttons": [
                                        {
                                            "type": "postback",
                                            "title": "帥哥",
                                            "data": "帥哥",
                                            "tags": [
                                                "bbb"
                                            ]
                                        },
                                        {
                                            "type": "postback",
                                            "title": "美女",
                                            "data": "美女",
                                            "tags": [
                                                "ggg"
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "templateType": "confirm"
                        },
                        "index": 2,
                        "version": 2
                    }
                ],
                "options": {
                    "name": "broadcast_by_api",
                    "applyFacebook24Policy": True,
                    "applyLineUnfollowFilter": True,
                    "customerNum": 1
                },
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    env["test-broadcast_id"] = res.json()["taskId"]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-broadcast_id"] == res.json()["taskId"]


def test_confirm_sending_single_data():
    url = f"{env['test-next-url']}/broadcast/tasks?"
    payload = {
                "orgId": f"{env['test-organizationId']}",
                "limit": 15,
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.get(url,params=payload)
    for jsondata in res.json()["results"] :
        if jsondata["status"] == "done" and jsondata["options"]["name"] == "broadcast_by_api":
            break
        else:
            continue
    assert jsondata["options"]["name"] == "broadcast_by_api"
    assert jsondata["options"]["messages"][0]["contentType"] == "text/plain"
    assert jsondata["options"]["messages"][1]["contentType"] == "application/x-image"

def test_confirm_message_center_message_eceived():
    time.sleep(1.5)
    result = mo.check_customer_message()
    assert result[0]["data"]["templateType"] == "confirm"
    assert result[1]["data"]["contentType"] == "image/png"
    assert result[2]["data"]["content"] != "image/png"
    assert result[2]["data"]["content"] == f"send message by v2 api {env['test-originalDisplayName']} 客戶姓名測試\n表情😁"
    assert result[3]["data"]["content"] != f"send message by v2 api {env['test-originalDisplayName']} 客戶姓名測試\n表情😁"

def test_create_broadcast_for_scheduled():
    t = mo.set_time(1)
    url = f"{env['test-next-url']}/broadcast/create"
    payload = {
                "name": "broadcast_scheduled_by_api",
                "orgId": f"{env['test-organizationId']}",
                "query": {
                    "orgId": f"{env['test-organizationId']}",
                    "platforms": [
                    "line"
                    ],
                    "customerObjectIds": [
                                          f"{env['test-user-objectId']}"
                    ],
                    "tags": [],
                    "externalTag": [],
                    "partnerTag": [],
                    "ecShopline": {}
                },
                "scheduleAt": f"{t}",
                "messages": [
                    {
                    "contentType": "text/plain",
                    "data": {
                        "content": "ffff"
                    },
                    "index": 0,
                    "version": 2
                    }
                ],
                "templates": [],
                "options": {
                    "name": "fff",
                    "applyFacebook24Policy": True,
                    "applyLineUnfollowFilter": True,
                    "customerNum": 1
                },
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    env["test-broadcast_id"] = res.json()["taskId"]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-broadcast_id"] == res.json()["taskId"]

def test_pause_sheduled():
    url =f"{env['test-next-url']}/broadcast/pause"
    payload = {
                "orgId":f"{env['test-organizationId']}",
                "taskId":f"{env['test-broadcast_id']}",
                "query": {
                    "orgId": f"{env['test-organizationId']}",
                    "taskId": f"{env['test-broadcast_id']}"
                },
                    "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    assert res.status_code == 200
    
def test_delete_sheduled():
    url =f"{env['test-next-url']}/broadcast/delete/{env['test-broadcast_id']}"
    payload = {
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.put(url,json=payload)
    assert res.status_code == 200