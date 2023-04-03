import mo 
import json
import time
import requests as req

env = mo.read_jsonfile()

def test_get_tags():
    url = f"{env['test-superAPIHost']}/v1/tags"
    header = {"Authorization":f"Bearer {env['test-superAPIKey']}"}
    param = {"organization":f"{env['test-organizationId']}","customerId":f"{env['test-customerId']}"}
    res = req.get(url,params=param,headers=header)
    assert res.status_code == 200

def test_add_tags():
    url = f"{env['test-superAPIHost']}/v1/tags"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "customerId": f"{env['test-customerId']}",
                "tags": ["hihi台南josh","ROCK TING"]
               }
    res = req.post(url,json=payload,headers=header)
    assert res.status_code == 200

def test_broadcast_for_send_text_message():
    url = f"{env['test-superAPIHost']}/v2/broadcast"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "query": {
                    "platform": "line",
                    "tags":  ["hihi台南josh"],
                },
                "messageType": "text",
                "message": {
                    "contentType": "text/plain",
                    "data": {
                    "content": "SUPER8 API SAND TEXT MESSAGE"
                    }
                }
                }
    res = req.post(url,json=payload,headers=header)
    time.sleep(1.5)
    assert mo.check_customer_message()[0]["data"]["content"] == "SUPER8 API SAND TEXT MESSAGE"

def test_broadcast_for_send_photo_message():
    url = f"{env['test-superAPIHost']}/v2/broadcast"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "query": {
                    "platform": "line",
                    "tags":  ["hihi台南josh","ROCK TING"],
                },
                "messageType": "text",
                "message": {
                    "contentType": "application/x-image",
                    "data": {
                    "url": "https://i1.sndcdn.com/avatars-000029916391-gd642k-t500x500.jpg"
                    }
                }
                }
    res = req.post(url,json=payload,headers=header)
    time.sleep(1.5)
    assert mo.check_customer_message()[0]["contentType"] == "application/x-image"
    assert mo.check_customer_message()[0]["data"]["url"] == "https://i1.sndcdn.com/avatars-000029916391-gd642k-t500x500.jpg"

def test_broadcast_for_send_template_message():
    url = f"{env['test-superAPIHost']}/v2/broadcast"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "query": {
                    "platform": "line",
                    "tags":  ["hihi台南josh","ROCK TING"],
                },
                "messageType": "template",
                "templateId": f"{env['test-templateId']}",
                }
    res = req.post(url,json=payload,headers=header)
    time.sleep(1.5)
    assert mo.check_customer_message()[0]["contentType"] == "application/x-template"

def test_delete_tags():
    url = f"{env['test-superAPIHost']}/v1/tags"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "customerId": f"{env['test-customerId']}",
                "tags": ["hihi台南josh","ROCK TING"]
               }
    res = req.delete(url,json=payload,headers=header)
    assert res.status_code == 200

def test_Notification_for_send_text_message():
    url = f"{env['test-superAPIHost']}/v1/notifications"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "customerId": f"{env['test-customerId']}",               
                "messageType": "text",
                "message": {
                    "contentType": "text/plain",
                    "data": {
                    "content": "xyz API發送"
                    }
                },
                "quiet": False
                }
    res = req.post(url,json=payload,headers=header)
    assert res.status_code == 200

def test_Notification_for_send_photo_message():
    url = f"{env['test-superAPIHost']}/v1/notifications"
    header = {"Authorization":f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "customerId": f"{env['test-customerId']}",
                "messageType": "text",
                "message": {
                            "contentType": "application/x-image",
                            "data": {"url": "https://pic.pimg.tw/babywinru/1632761236-484576045-g.png"}
                            }
                }
    res = req.post(url,json=payload,headers=header)
    assert mo.check_customer_message()[0]["data"]["url"] == "https://pic.pimg.tw/babywinru/1632761236-484576045-g.png"

def test_Notification_for_send_options_card_message(temp_tpye= "card"):
    url = f"{env['test-superAPIHost']}/v1/notifications"
    header = {"Authorization":f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "customerId": f"{env['test-customerId']}",
                "messageType": "template",
                "template": {
                    "data": {
                            "templateType": "card",
                            "elements": [{"title": "奇摩",
                                        "subtitle": "9999",
                                        "imageUrl": "https://s.yimg.com/cv/apiv2/social/images/yahoo_default_logo.png",
                                        "buttons": [{
                                            "type": "url",
                                                "title": "奇摩",
                                                "data": "https://tw.yahoo.com",
                                                "tags": ["哈哈哈"]}]}]
                            }},
                "templateName": "優化"
                }
    res = req.post(url,json=payload,headers=header)
    assert mo.check_customer_message()[0]["data"]["name"] == "優化"
    assert mo.check_customer_message()[0]["data"]["templateType"] == "card"

def test_Notification_for_send_image_message(temp_tpye = "image"):
    url = f"{env['test-superAPIHost']}/v1/notifications"
    header = {"Authorization":f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "customerId": f"{env['test-customerId']}",
                "messageType": "template",
                "template": {
                    "data": {
                            "templateType": temp_tpye,
                            "elements": [{"title": "奇摩",
                                        "subtitle": "9999",
                                        "imageUrl": "https://s.yimg.com/cv/apiv2/social/images/yahoo_default_logo.png",
                                        "buttons": [{
                                            "type": "url",
                                                "title": "奇摩",
                                                "data": "https://tw.yahoo.com",
                                                "tags": ["哈哈哈"]}]}]
                            }},
                "templateName": "優化"
                }
    res = req.post(url,json=payload,headers=header)
    assert mo.check_customer_message()[0]["data"]["name"] == "優化"
    assert mo.check_customer_message()[0]["data"]["templateType"] == "image"

def test_Notification_for_send_confirmation_card_message(temp_tpye = "confirm"):
    url = f"{env['test-superAPIHost']}/v1/notifications"
    header = {"Authorization":f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "customerId": f"{env['test-customerId']}",
                "messageType": "template",
                "template": {
                             "data": {
                                      "templateType": temp_tpye,
                                      "elements": [
                                        {
                                            "title": "123222",
                                            "buttons": [
                                                {
                                                    "type": "postback",
                                                    "title": "119",
                                                    "data": "119",
                                                    "tags": []
                                                },
                                                {
                                                    "type": "url",
                                                    "title": "119",
                                                    "data": "https://www.google.com",
                                                    "tags": []
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "templateName": "優化3310"
                }
    res = req.post(url,json=payload,headers=header)
    assert mo.check_customer_message()[0]["data"]["name"] == "優化3310"
    assert mo.check_customer_message()[0]["data"]["templateType"] == "confirm"

def test_Notification_for_send_confirmation_card_message(temp_tpye = "confirm"):
    url = f"{env['test-superAPIHost']}/v1/notifications"
    header = {"Authorization":f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "customerId": f"{env['test-customerId']}",
                "messageType": "template",
                "template": {
                             "data": {
                                      "templateType": temp_tpye,
                                      "elements": [
                                        {
                                            "title": "123222",
                                            "buttons": [
                                                {
                                                    "type": "postback",
                                                    "title": "119",
                                                    "data": "119",
                                                    "tags": []
                                                },
                                                {
                                                    "type": "url",
                                                    "title": "119",
                                                    "data": "https://www.google.com",
                                                    "tags": []
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "templateName": "優化3310"
                }
    res = req.post(url,json=payload,headers=header)
    assert mo.check_customer_message()[0]["data"]["name"] == "優化3310"
    assert mo.check_customer_message()[0]["data"]["templateType"] == "confirm"

def test_Notification_for_send_imagemap_message(temp_tpye = "imagemap"):
    url = f"{env['test-superAPIHost']}/v1/notifications"
    header = {"Authorization":f"Bearer {env['test-superAPIKey']}"}
    payload = {
                "organization": f"{env['test-organizationId']}",
                "customerId": f"{env['test-customerId']}",
                "messageType": "template",
                "template": {
                    "data": {
                        "templateType": "imagemap",
                        "elements": [
                            {
                                "title": "Notification 圖文訊息 by api",
                                "imageUrl": "https://assets.no8.io/app-api-uploader/stag/1665463999929/1040x1040_jpg.jpg",
                                "size": {
                                    "width": 1040,
                                    "height": 1040
                                },
                                "aspectRatio": "1:1",
                                "messageTemplateType": "ImagemapTemplate1",
                                "buttons": [
                                    {
                                        "title": "圖文訊息Text by api",
                                        "type": "postback",
                                        "data": "圖文訊息Text by api",
                                        "tags": [
                                            "圖文訊息Text by api"
                                        ],
                                        "x": "0%",
                                        "y": "0%",
                                        "width": "100%",
                                        "height": "100%"
                                    }
                                ]
                            }
                        ]
                    }
                },
                "templateName": "Notification 圖文訊息 by api"
            }
    res = req.post(url,json=payload,headers=header)
    assert mo.check_customer_message()[0]["data"]["name"] == "Notification 圖文訊息 by api"
    assert mo.check_customer_message()[0]["data"]["templateType"] == "imagemap"


def test_get_customer_info():
    url = f"{env['test-superAPIHost']}/v1/customer"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    param = {"organization":f"{env['test-organizationId']}","customerId":f"{env['test-customerId']}"}

    res = req.get(url,params=param,headers=header)
    assert res.status_code == 200

def test_update_customer_info():
    url = f"{env['test-superAPIHost']}/v1/customer"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {"organization": f"{env['test-organizationId']}",
               "customerId": f"{env['test-customerId']}",
               "customerInfo": {
                                  "displayName": "XXY",
                                  "cellPhone": "0909090909",
                                  "email": "iori071115@gmail.net",
                                  "birthday": "1984-07-11",
                                  "gender": "male",
                                  "language": "zh-TW",
                                  "nation": "R.O.C",
                                  "location": "TPI",
                                  "about": "凸",
                                  "customField1": "你",
                                  "customField2": "我",
                                  "customField3": "他"
                                 }
                }
    res = req.post(url,json=payload,headers=header)
    assert res.status_code == 200

def test_trigger_ma():
    url = f"{env['test-superAPIHost']}/v1/marketing_automation/trigger"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {"organization": f"{env['test-organizationId']}",
               "customerId": f"{env['test-customerId']}",
               "procedureId":f"{env['test-MA_Id']}"
                }
    res = req.post(url,json=payload,headers=header)
    assert mo.check_customer_message()[0]["data"]["content"] == "s8 api觸發~~"

def test_number_of_tags_report():
    url = f"{env['test-superAPIHost']}/v1/report/tagsCount"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {"organization": f"{env['test-organizationId']}",
               "startDate": "2023-03-01",
                "endDate": "2023-03-08"
                }

    res = req.post(url,json=payload,headers=header)
    assert res.status_code == 200

def test_number_of_customers_report():
    url = f"{env['test-superAPIHost']}/v1/report/customerJoinCount"
    header = {"Authorization": f"Bearer {env['test-superAPIKey']}"}
    payload = {"organization": f"{env['test-organizationId']}",
               "customerId": f"{env['test-customerId']}",
               "startDate": "2023-03-01",
               "endDate": "2023-03-08",
               "platform": "whatsapp",
               "statistic": "sum"
                }

    res = req.post(url,json=payload,headers=header)
    assert res.status_code == 200


