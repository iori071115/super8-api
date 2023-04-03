import mo 
import json
import requests as req

env = mo.read_jsonfile()

def test_invite_new_managers():
    url = f"{env['parse-url']}/functions/invite"
    payload = {
                "className": "Organization",
                "objectId": f"{env['test-organizationId']}",
                "emails": [
                    "auto_test@no8.io"
                ],
                "authority": "admin",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    
    res = req.post(url,json=payload)
    assert res.status_code == 200
    
def test_confirm_invited_managers():
    url = f"{env['test-next-url']}/functions/findOrgMembers"
    payload = {
                "where": {
                    "organization": {
                        "objectId": f"{env['test-organizationId']}"
                    }
                },
                "options": {
                    "includeOwner": True
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    
    res = req.post(url,json=payload)
    for temp in res.json():
        if  "invitationWaiting" in temp and temp["username"] == "auto_test@no8.io" :
            break
        else:
            pass
    assert temp["username"] == "auto_test@no8.io"
    assert temp["authorityName"] == "admin"

def test_delete_invited_managers():
    url = f"{env['parse-url']}/functions/evict"
    payload = {
                "className": "Organization",
                "objectId": f"{env['test-organizationId']}",
                "emails": [
                    "auto_test@no8.io"
                ],
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_confirm_that_the_invited_managers_has_been_removed():
    url = f"{env['test-next-url']}/functions/findOrgMembers"
    payload = {
                "where": {
                    "organization": {
                        "objectId": f"{env['test-organizationId']}"
                    }
                },
                "options": {
                    "includeOwner": True
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    
    res = req.post(url,json=payload)
    for temp in res.json():
        if  "invitationWaiting" in temp and temp["username"] != "auto_test@no8.io" :
            pass
        else:
            break
    assert res.status_code == 200

def test_get_account_info():
    url = f"{env['parse-url']}/classes/_User/{env['test-accountId']}"
    payload = {
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
               }
    res = req.post(url,json=payload)
    env["test-FirstName"] = res.json()["firstName"]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-FirstName"] == res.json()["firstName"]

def test_modify_account_info():
    url = f"{env['parse-url']}/classes/_User/{env['test-accountId']}"
    payload = {
                "firstName": "修改帳戶名稱 by API",
                "language": "zh",
                "_method": "PUT",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_confirm_modifyed_account_info():
    url = f"{env['parse-url']}/classes/_User/{env['test-accountId']}"
    payload = {
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
               }
    res = req.post(url,json=payload)
    assert res.json()["firstName"] == "修改帳戶名稱 by API"

def test_recovery_account_name():
    url = f"{env['parse-url']}/classes/_User/{env['test-accountId']}"
    payload = {
                "firstName": f"{env['test-FirstName']}",
                "language": "zh",
                "_method": "PUT",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    res = req.post(url,json=payload)
    assert res.status_code == 200

def test_confirm_recoveryed_account_info():
    url = f"{env['parse-url']}/classes/_User/{env['test-accountId']}"
    payload = {
                "_method": "GET",
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
               }
    res = req.post(url,json=payload)
    assert res.json()["firstName"] == env["test-FirstName"]