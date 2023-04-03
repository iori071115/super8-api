import mo 
import time
import json
import requests as req

env = mo.read_jsonfile()

# def test_get_organization_info():
#     url = f"{env['test-vendorAPI-url']}/classes/Organization"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     param = {
#             "objectId": f"{env['test-organizationId']}",
#             "displayName": f"{env['test-organization-name']}",
#             "icon":"",
#             "category":"enterprise"
#               }
#     res = req.get(url,params=param,headers=header)
#     assert res.json()["category"] == "enterprise"
#     assert res.json()["displayName"] == f"{env['test-organization-name']}"

# def test_send_Message_to_customer():
#     url = f"{env['test-vendorAPI-url']}/function/message"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     paylaod = {
#                 "customerId": f"{env['test-customerId']}",
#                 "messages": [{
#                               "contentType": "text/plain",
#                               "data": {"content": "test to sand message by partnerapi"}
#                               }]
#                 }
#     res = req.post(url,json=paylaod,headers=header)
#     time.sleep(1.5)
#     assert res.status_code == 200
#     assert mo.check_customer_message()[0]["data"]["content"] == "test to sand message by partnerapi"

# def test_update_customer_tag():
#     url= f"{env['test-vendorAPI-url']}/classes/Tag/test partner api tag"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     param ={
#             "customerId": f"{env['test-customerId']}"
#             }
#     res = req.put(url,params=param,headers=header)
#     assert res.status_code == 200

# def test_get_customer_tag_list():
#     url= f"{env['test-vendorAPI-url']}/classes/Tag"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     param ={
#             "customerId": f"{env['test-customerId']}"
#             }
#     res = req.get(url,params=param,headers=header)
#     assert res.status_code == 200

def test_create_customer_group():
    url= f"{env['test-vendorAPI-url']}/function/CustomerGroup/custom"
    header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
    payload ={
              "groupName": "test customer group"
              }
    res = req.post(url,json=payload,headers=header)
    env["test-groupId"] = res.json()["groupId"]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-groupId"] == res.json()["groupId"]

def test_import_customers():
    url= f"{env['test-vendorAPI-url']}/function/CustomerGroup/custom/{env['test-groupId']}"
    header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
    payload ={
              "action": "import",
              "customerIdList": [
                                  f"{env['test-customerId']}",
                                  f"{env['test-customer1Id']}"
                                 ]
              }
    res = req.post(url,json=payload,headers=header)
    assert res.status_code == 200

def test_complete_the_import():
    url= f"{env['test-vendorAPI-url']}/function/CustomerGroup/custom/{env['test-groupId']}"
    header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
    payload ={
              "action": "finish"
              }
    res = req.post(url,json=payload,headers=header)
    assert res.status_code == 200

def test_get_customer_group():
    url= f"{env['test-vendorAPI-url']}/function/CustomerGroup/custom/{env['test-groupId']}"
    header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
    param ={
              "groupId": f"{env['test-groupId']}"
              }
    res = req.get(url,params=param,headers=header)
    assert res.json()["groupId"] == env["test-groupId"]

# def test_send_broadcast_text_message():
#     url = f"{env['test-vendorAPI-url']}/function/broadcast"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     paylaod = {
#                 "broadcastName": "broadcast example 1",
#                 "platform": "line",
#                 "query": {"tags": ["test partner api tag"],
#                 },
#                 "messages": [{
#                               "contentType": "text/plain",
#                               "data": {"content": "test to sand broadcast text message by partnerapi"}
#                                 }]
#                 }
#     res = req.post(url,json=paylaod,headers=header)
#     time.sleep(1.5)
#     assert mo.check_customer_message()[0]["data"]["content"] == "test to sand broadcast text message by partnerapi"

# def test_send_broadcast_options_card_message():
#     url = f"{env['test-vendorAPI-url']}/function/broadcast"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     paylaod = {
#                 "broadcastName": "card message by api",
#                 "groupId": f"{env['test-groupId']}",
#                 "platform": "line",
#                 "messages": [
#                     {
#                     "contentType": "application/x-template",
#                     "data": {
#                         "templateType": "card",
#                         "elements": [
#                         {
#                             "title": "card message by api",
#                             "subtitle": "Card Desc",
#                             "imageUrl": "https://imgur.com/E06Mjzf.jpg",
#                             "imageType": "url",
#                             "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Click Me",
#                                 "data": "Click Me",
#                                 "tags": [
#                                 "tagName1",
#                                 "tagName2"
#                                 ]
#                             }
#                             ],
#                             "aspectRatio": "1:1"
#                         }
#                         ]
#                     }
#                     }
#                 ]
#                 }
#     res = req.post(url,json=paylaod,headers=header)
#     time.sleep(1.5)
#     assert mo.check_customer_message()[0]["data"]["elements"][0]["title"] == "card message by api"
#     assert mo.check_customer_message()[0]["data"]["templateType"] == "card"

# def test_send_broadcast_confirm_card_message():
#     url = f"{env['test-vendorAPI-url']}/function/broadcast"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     paylaod = {
#                 "broadcastName": "card message by api",
#                 "groupId": f"{env['test-groupId']}",
#                 "platform": "line",
#                 "messages": [{"contentType": "application/x-template",
#                               "data": {
#                               "templateType": "confirm",
#                               "elements": [{"title": "confirm message by api",
#                                             "buttons": [{
#                                                           "type": "postback",
#                                                           "title": "Click Me",
#                                                           "data": "Click Me",
#                                                           "tags": []},
#                                                             {"type": "url",
#                                                              "title": "Click Me",
#                                                              "data": "https://tw.yahoo.com",
#                                                              "tags": []
#                                                             }],"aspectRatio": "1:1"}]
#                             }}]
#                 }
#     res = req.post(url,json=paylaod,headers=header)
#     time.sleep(1.5)
#     assert mo.check_customer_message()[0]["data"]["elements"][0]["title"] == "confirm message by api"
#     assert mo.check_customer_message()[0]["data"]["templateType"] == "confirm"

# def test_send_broadcast_template_message():
#     url = f"{env['test-vendorAPI-url']}/function/broadcast"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     payload = {
#                 "broadcastName": "broadcast example 3",
#                 "platform": "line",
#                 "groupId": f"{env['test-groupId']}",
#                 "messages": [{
#                     "contentType": "application/x-template",
#                     "data": {"templateId": f"{env['test-templateId']}"}
#                                 }]
#                 }
#     res = req.post(url, json=payload, headers=header)
#     time.sleep(1.5)
#     assert mo.check_customer_message()[0]["data"]["name"] == "template for api test"
#     assert mo.check_customer_message()[0]["data"]["templateType"] == "image"


# def test_delete_customer_tag():
#     url= f"{env['test-vendorAPI-url']}/classes/Tag/test partner api tag"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     param ={
#             "customerId": f"{env['test-customerId']}"
#             }
#     res = req.delete(url,params=param,headers=header)

# def test_added_partner_externaltag_by_put():
#     url = f"{env['test-vendorAPI-url']}/classes/externalTag"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     paylaod = {
#                 "customerId": f"{env['test-customerId']}",
#                 "tags": ["partner_tag1"],
#                 "vendor": "launchcart",
#                 "category": "intent"
#                 }
#     res = req.put(url,json=paylaod,headers=header)
#     assert res.status_code == 200
#     assert "partner_tag1" in mo.get_customer_info()["externalTag"]["launchcart"]

# def test_added_partner_externaltag_by_post():
#     url = f"{env['test-vendorAPI-url']}/classes/externalTag"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     paylaod = {
#                 "customerId": f"{env['test-customerId']}",
#                 "tags": ["partner_tag2"],
#                 "vendor": "launchcart",
#                 "category": "intent"
#                 }
#     res = req.post(url,json=paylaod,headers=header)
#     assert res.status_code == 200
#     assert "partner_tag2" in mo.get_customer_info()["externalTag"]["launchcart"]

# def test_delete_all_externaltag_tag():
#     url = f"{env['test-vendorAPI-url']}/classes/externalTag"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     paylaod = {
#                 "customerId": f"{env['test-customerId']}",
#                 "vendor": "launchcart"
#                 }
#     res = req.delete(url,json=paylaod,headers=header)
#     assert res.status_code == 200
#     assert mo.get_customer_info()["externalTag"]["launchcart"] == []

# def test_partnerapi_update_customer_info():
#     url = f"{env['test-vendorAPI-url']}/classes/Customer/{env['test-customerId']}"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     payload = {
#                 "displayName": "default name",
#                 "email": "Super8-2@no8.io",
#                 "cellPhone": "0922123456",
#                 "gender": "female",
#                 "birthday": "2000/02/23",
#                 "about": "about me - modify",
#                 "location": "Taipei",
#                 "language":"en-US",
#                 "nation":"中華民國",
#                 "customField1": "customField1 example,",
#                 "customField2": "customField2 example,",
#                 "customField3": "customField3 example,",
#                 "hiddenField1": "hiddenField1 example,",
#                 "hiddenField2": "hiddenField2 example,",
#                 "externalId": "externalId example"
#                }
    
#     res = req.patch(url,json=payload,headers=header)
#     assert res.status_code == 200

# def test_get_customer_info():
#     url= f"{env['test-vendorAPI-url']}/classes/Customer/{env['test-customerId']}"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     param ={
#               "customerId": f"{env['test-customerId']}"
#               }
#     res = req.get(url,params=param,headers=header)
#     assert res.json()["customer"]["gender"] == "female"
#     assert res.json()["customer"]["language"] == "en-US"

# def test_get_get_customer_list():
#     url= f"{env['test-vendorAPI-url']}/classes/Customer"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     payload ={
#             "where": {"platform": "line"},
#             "options": {"limit": 20,
#                         "skip": 1,
#                         "select": ["customerId"]}
#             }
#     res = req.post(url,json=payload,headers=header)
#     assert len(res.json()["customers"]) > 0

# def test_get_list_by_organization():
#     url= f"{env['test-vendorAPI-url']}/classes/Template"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     param ={
#               "count": 20,
#               "limit": 20,
#               "skip": 1
#               }
#     res = req.get(url,params=param,headers=header)
#     assert res.status_code == 200

# def test_get_one_by_templateId():
#     url= f"{env['test-vendorAPI-url']}/classes/Template/{env['test-templateId']}"
#     header = {"Authorization":f"Bearer {env['test-vendorAPI-Token']}"}
#     res = req.get(url,headers=header)
#     assert res.json()["templateId"] == env["test-templateId"]
#     assert res.json()["name"] == "template for api test"
