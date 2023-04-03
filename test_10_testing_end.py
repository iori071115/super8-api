import mo 
import json
import requests as req

env = mo.read_jsonfile()
    
def test_delete_test_templates():
    for x in mo.get_test_templates():
        tempid = x["_id"]
        url = f"{env['parse-url']}/functions/removeTemplate"
        payload = {
                    "templateId": tempid,
                    "organization": {"__type": "Pointer",
                                    "className": "Organization",
                                    "objectId": f"{env['test-organizationId']}"},
                    "_ApplicationId": f"{env['parse-app-id']}",
                    "_JavaScriptKey": "javascriptKey",
                    "_SessionToken": f"{env['sessionToken']}"
                    }
        res = req.post(url,json=payload)
        
def test_delete_file():
    for x in mo.get_test_file():
        fileid = x["objectId"]
        url = f"{env['parse-url']}/classes/File/{fileid}"
        payload = {
                    "_method": "DELETE",
                    "_ApplicationId": f"{env['parse-app-id']}",
                    "_JavaScriptKey": "javascriptKey",
                    "_SessionToken": f"{env['sessionToken']}"
                    }
        res = req.post(url,json=payload)

def test_delete_MA():
    url = f"{env['test-next-url']}/automation/{env['test-MA_Id']}"
    header = {"_SessionToken": f"{env['sessionToken']}"}
    res = req.delete(url,headers=header)
    assert res.json()["procedureId"] == env['test-MA_Id']

def test_delete_customergroup():
    for x in mo.get_customergroup():
        if x["name"] == "test customer group" :
            y = x["objectId"]
            url = f"{env['parse-url']}/classes/CustomerGroup/{y}"
            payload = {
                        "_method": "PUT",
                        "expired": True,
                        "_ApplicationId": f"{env['parse-app-id']}",
                        "_JavaScriptKey": "javascriptKey",
                        "_SessionToken": f"{env['sessionToken']}"
                        }
            res = req.post(url,json=payload)
        else:
            pass