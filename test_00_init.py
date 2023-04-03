import mo
import json
import requests as req

env = mo.read_jsonfile()

def test_login():
    url = f"{env['parse-url']}/login"
    payload = {
                "username": f"{env['loginId']}",
                "password": f"{env['loginpw']}",
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey"
                }
    res = req.post(url,json=payload)
    env["sessionToken"] = res.json()['sessionToken']
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()['sessionToken'] == res.json()['sessionToken']

def test_check_customers_info_two_female():
    url = f"{env['test-next-url']}/broadcast/getCustomers"
    payload = {
                "where": {
                    "originalDisplayName": "",
                    "displayName": "",
                    "tags": [],
                    "externalTag": [],
                    "partnerTag": [],
                    "platforms": ["line"],
                    "cellPhone": "",
                    "email": {"op_exists": True},
                    "friendship": "",
                    "inboxes": [],
                    "gender": ["female"],
                    "orgId": f"{env['test-organizationId']}"
                },
                "select": [
                    "joinedAt",
                    "lastMessageAt",
                    "friendship",
                    "conversation"
                ],
                "options": {
                    "isNoTagCustomer": False
                },
                "skip": 0,
                "limit": 40,
                "sliceTagsCount": 12,
                "_SessionToken": f"{env['sessionToken']}"
                }

    res = req.post(url,json=payload)
    assert len(res.json()["result"]["customers"])>= 2
    
def test_get_user_and_set_parameter():
    result = mo.confirm_customer_stutas()
    env["test-customerId"] = result[0]["customerId"]
    env["test-originalDisplayName"] = result[0]["originalDisplayName"]
    env["test-user-objectId"]  = result[0]["objectId"]
    env["test-conversationId"] = result[0]["conversation"]["_id"]
    env["test-customer1Id"] = result[1]["customerId"]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-customerId"] == result[0]["customerId"]
    assert mo.read_jsonfile()["test-customer1Id"] == result[1]["customerId"]
    assert mo.read_jsonfile()["test-originalDisplayName"] == result[0]["originalDisplayName"]
    assert mo.read_jsonfile()["test-user-objectId"]  == result[0]["objectId"]
    assert mo.read_jsonfile()["test-conversationId"] == result[0]["conversation"]["_id"]

def test_get_member_info():
    url = f"{env['test-next-url']}/functions/findOrgMembers"
    payload = {
                "where": {
                    "organization": {
                        "objectId": f"{env['test-organizationId']}"
                     }
                },
                "options": {
                    "includeOwner": "true"
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    x=1
    for temp in res.json():
        if x <= 2 and "invitationWaiting" not in temp and "authorityName" in temp and temp["authorityName"] == "admin"   :
            env[f'test-adm-objectId_{x}'] = temp["objectId"]
            x+=1
        else:
            pass
    mo.write_jsonfile (env)
    assert  mo.read_jsonfile()["test-adm-objectId_1"] == env["test-adm-objectId_1"] 
    assert  mo.read_jsonfile()["test-adm-objectId_2"] == env["test-adm-objectId_2"]
    
def test_set_user_name():
    url = f"{env['parse-url']}/classes/Customer/{env['test-user-objectId']}"
    payload = {
                "displayName": "default name",
                "_method": "PUT",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_ClientVersion": "js1.11.1",
                "_SessionToken": f"{env['sessionToken']}"
               }
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_set_user_info():
    url = f"{env['parse-url']}/classes/Customer/{env['test-user-objectId']}"
    payload = {
                "birthday": {
                    "__type": "Date",
                    "iso": "1984-07-11T07:00:00.538Z"
                },
                "cellPhone": "0988888888",
                "email": "111@aa.bb",
                "gender": "male",
                "language": "zh-TW",
                "location": "default_location_byapi",
                "nation": "R.O.C",
                "customField1": "default_field1_byapi",
                "customField2": "default_field2_byapi",
                "_method": "PUT",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_ClientVersion": "js1.11.1",
                "_SessionToken": f"{env['sessionToken']}"
               }
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_get_accountid_info():
    url = f"{env['parse-url']}/classes/Preference"
    payload = {
                "where": {},
                "limit": 1,
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
               }
    res = req.post(url,json=payload)
    env["test-accountId"] = res.json()["results"][0]["channels"][0]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-accountId"] == res.json()["results"][0]["channels"][0]

def test_create_temp():
    mo.create_template()
    env["test-templateId"] = mo.get_test_templates()[0]["objectId"]
    env["test-templateId-long"] = mo.get_test_templates()[0]["_id"]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-templateId"] == env["test-templateId"]


def test_get_organization_name():
    url = f"{env['parse-url']}/classes/Organization"
    payload = {
                "where": {"members": {
                        "$inQuery": {"where": {"users": {"__type": "Pointer",
                                                         "className": "_User",
                                                         "objectId": f"{env['test-adm-objectId_1']}"}},
                        "className": "Membership"}}},
                "include": "members",
                "keys": "displayName,members",
                "order": "displayName",
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url, json=payload)
    for x in res.json()["results"] :
        if x["objectId"] == f"{env['test-organizationId']}":
            env["test-organization-name"] = x["displayName"]
            mo.write_jsonfile(env)
            break
    assert mo.read_jsonfile()["test-organization-name"] == env["test-organization-name"]