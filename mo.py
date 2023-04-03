import json
import requests as req
import time 


Environment = "env_prod.json"
# Environment = "env_stage.json"

def read_jsonfile():
    with open(Environment,"r",encoding="utf-8") as f:
        j = json.load(f)
    return j

def write_jsonfile(data):
    with open(Environment,"w",encoding="utf-8") as f:
        j = json.dump(data, f, indent=4)
    return j

def set_time(t):
    tl =time.localtime(time.time())
    t1 = time.strftime("%Y-%m-%dT%H:%M:00.000Z",tl)
    t2 = time.strftime("%Y-%m-%d %H:%M",tl)
    Mon = time.strftime("%m",tl)
    Mon = int(Mon)+1
    t3 = time.strftime(f"%Y-{Mon}-%d %H:%M",tl)

    if t == 1:
        return t1
    elif t == 2:
        return t2
    elif t == 3:
        return t3
    
def sand_line_massage(mt,message):
    env = read_jsonfile()
    t = str(time.time())
    url =  f"{env['test-mes-url']}/line/gun/{env['test-organizationId']}"
    payload = {
                "events": [
                    {
                        "type": mt,
                        "replyToken": "fakeReplyTokennnnnnnnnnnnnnnnn",
                        "source": {
                            "userId": f"{env['test-customerId']}",
                            "type": "user"
                        },
                        "timestamp": t,
                        "mode": "active",
                        "message": {
                            "type": "text",
                            "id": "13402131486883",
                            "text": message
                        }
                    }
                ],
                "destination": f"{env['test-customerId']}"
              }
    res = req.post(url,json=payload)
    return res.json()

def webhook_trigger_event(keyword,text):
    env = read_jsonfile()
    url = f"{env['test-mes-url']}/bot/{env['test-organizationId']}"
    param = {"ref": keyword}
    header = {"X-Partner-Api-Webhook-Key": f"{env['test-webhook']}"}
    payload = {
                "identity": f"{env['test-customerId']}",
                "payload": {"text1": text}
                }
    res = req.post(url,params=param,headers=header,json=payload)
    return res.json()
     
def confirm_customer_stutas():
    env = read_jsonfile()
    url = f"{env['parse-url']}/functions/findCustomerV3"
    payload = {
                "where": {
                    "organization": {
                    "className": "Organization",
                    "objectId": f"{env['test-organizationId']}"
                    },
                    "customer": [
                    {
                        "inbox": ["all"]
                    }
                    ]
                },
                "options": {
                    "message": True
                },
                "sort": {
                    "lastMessageAt": -1
                },
                "limit": 20,
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    return res.json()["result"]

def check_customer_info():
    env = read_jsonfile()
    url = f"{env['parse-url']}/classes/Customer"
    payload = {
                "limit": 1,
                "where": {"objectId": f"{env['test-user-objectId']}"},
                "keys": "ec,bind,extra,friendship,customerId,originalDisplayName,lastMessageAt,joinedAt,birthday,about,nation,location,language,gender,customField3,customField2,customField1,cellPhone,displayName,email,externalTag,picture,platform,tag",
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
            }            
    res = req.post(url,json=payload)
    return res.json()["results"][0]

def check_customer_message():
    env = read_jsonfile()
    url = f"{env['parse-url']}/classes/Message"
    payload = {"where":{
                        "organization":{
                                        "__type":"Pointer",
                                        "className":"Organization",
                                        "objectId":f"{env['test-organizationId']}"
                                        },
                        "conversation":{
                                        "__type":"Pointer",
                                        "className":"Conversation",
                                        "objectId":f"{env['test-conversationId']}"
                                        },
                        "data":{
                                        "$ne":""
                                }
                        },
                        "keys":"sendType,senderType,sender,contentType,data,createdAt,organization,conversation,error,errorOrigin,invalid,platform,lockedRoleId,fMid,errorDetails,taskId",
                        "limit":16,
                        "order":"-createdAt",
                        "_method":"GET",
                        "_ApplicationId": f"{env['parse-app-id']}",
                        "_JavaScriptKey": "javascriptKey",
                        "_SessionToken": f"{env['sessionToken']}",}
    res = req.post(url,json=payload)
    return res.json()["results"]

def confirm_favorites():
    env = read_jsonfile()
    url = f"{env['parse-url']}/classes/Message"
    payload = {
                "where": {
                    "conversation": {
                        "__type": "Pointer",
                        "className": "Conversation",
                        "objectId":f"{env['test-conversationId']}"
                    },
                    "data": {
                        "$ne": ""
                    }
                },
                "keys": "senderType,sender,contentType,data,createdAt,error,errorOrigin,invalid",
                "limit": 25,
                "order": "-createdAt",
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_ClientVersion": "js1.11.1",
                "_SessionToken": f"{env['sessionToken']}",
            }
    res = req.post(url,json=payload)
    return res.json()["results"][0]

def functions_inboxesV3():
    env = read_jsonfile()
    url = f"{env['parse-url']}/functions/inboxesV3"
    payload = {
                "_method": "POST",
                "where": {
                    "orgId":f"{env['test-organizationId']}" ,
                    "inboxes": [
                    "all",
                    "unassigned",
                    "done",
                    "private",
                    "self",
                    "bot",
                    "spam",
                    "unfollow"
                    ]
                },
                "options": {
                    "showPrivateDetail": True
                },
                    "_ApplicationId": f"{env['parse-app-id']}",
                    "_JavaScriptKey": "javascriptKey",
                    "_SessionToken": f"{env['sessionToken']}",
                }
    res = req.post(url,json=payload)
    return res.json()["result"]

def get_customer_info():
    env = read_jsonfile()
    url = f"{env['parse-url']}/classes/Customer"
    payload = {
                "limit": 1,
                "where": {
                    "objectId": f"{env['test-user-objectId']}"
                },
                "keys": "ec,bind,extra,friendship,customerId,originalDisplayName,lastMessageAt,joinedAt,birthday,about,nation,location,language,gender,customField3,customField2,customField1,cellPhone,displayName,email,externalTag,picture,platform,tag",
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}",
                }
    res = req.post(url,json=payload)
    return res.json()["results"][0]

def superapi_get_customer_info():
    env = read_jsonfile()
    url = f"{env['test-superAPIHost']}/v1/customer"
    header = {"Authorization":f"Bearer {env['test-superAPIKey']}"}
    param = {"organization":f"{env['test-organizationId']}","customerId":f"{env['test-customerId']}"}
    res = req.get(url,params=param,headers=header)
    return res.json()

def create_template():
    env = read_jsonfile()
    url = f"{env['parse-url']}/functions/publishTemplate"
    payload = {
                "template": {"className": "Template",
                             "templateType": "image",
                             "name": "template for api test",
                             "data": {"elements": [{"goodsURL": "template for test 0 ",
                                                    "imageType": "url",
                                                    "imageUrl": "https://www.delft.com/storage/banner-Vermeer-zonder-embleem-960x960.png",
                                                    "buttons": [{"type": "postback",
                                                                 "title": "text button",
                                                                 "data": "text button",
                                                                 "tags": []}],
                                                    "aspectRatio": "1:1"},
                                                    {"goodsURL": "template for test 1",
                                                    "imageType": "url",
                                                    "imageUrl": "https://media.gq.com.tw/photos/6040645c4c047b6da81d3b07/1:1/w_960,h_960,c_limit/Mercedes-Benz-C-Class-2022-1280-1e.jpg",
                                                    "buttons": [{"type": "url",
                                                                "title": "",
                                                                "data": "https://www.mercedes-benz.com.tw/passengercars.html",
                                                                "tags": []}],
                                                    "aspectRatio": "1:1"}],
                             "templateType": "image" },
                             "organization": {"__type": "Pointer",
                                              "className": "Organization",
                                              "objectId": f"{env['test-organizationId']}"},
                             "hidden": False,
                             "version": 2},
                             "_ApplicationId": f"{env['parse-app-id']}",
                             "_JavaScriptKey": "javascriptKey",
                             "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload,)
    return res.json()

def get_test_templates():
    env = read_jsonfile()
    url = f"{env['parse-url']}/functions/queryTemplate"
    payload = {
                "where": {
                           "organization": {"__type": "Pointer",
                                            "className": "Organization",
                                            "objectId": f"{env['test-organizationId']}"},
                            "vendor": {"$ne": True}
                          },
                            "skip": 0,
                            "limit": 50,
                            "sort": {"createdAt": -1},
                            "group": True,
                            "_ApplicationId": f"{env['parse-app-id']}",
                            "_JavaScriptKey": "javascriptKey",
                            "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload,)
    return res.json()["result"]

def get_test_file():
    env = read_jsonfile()
    url = f"{env['parse-url']}/classes/File"
    payload = {
                "where": {
                    "organization": {"__type": "Pointer",
                                     "className": "Organization",
                                     "objectId": f"{env['test-organizationId']}"}
                          },
                "include": "uploadedBy",
                "limit": 50,
                "order": "-updatedAt",
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload,)
    return res.json()["results"]

def get_customergroup():    
    env = read_jsonfile()
    url = f"{env['parse-url']}/classes/CustomerGroup"
    payload = {
                "count": True,
                "_method": "GET",
                "where": {"organization": {"className": "Organization",
                                     "__type": "Pointer",
                                     "objectId": "hKGNnMM33M"},
                                     "expired": {"$ne": True},
                                                "status": {"$ne": "creating"}},
                "limit": 40,
                "skip": 0,
                "order": "-updatedAt",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload,)
    return res.json()["results"]

