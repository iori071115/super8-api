import mo 
import json
import requests as req

env = mo.read_jsonfile()
header = {
          "X-Parse-Application-Id": f"{env['parse-app-id']}",
              "X-Parse-Session-Token": f"{env['sessionToken']}",
              "X-Parse-Javascript-Key": f"{env['parse-javascript-key']}",
              "origin": "https://console.no8.io"
          }

def test_creat_superlink():
    url = f"{env['parse-url']}/link/api/v1/organizations/{env['test-organizationId']}/campaigns"
    payload = {
                "name": "AutoTest",
                "triggerTarget": "all",
                "platform": "line",
                "channels": [
                    {
                        "position": 1,
                        "name": "渠道 1",
                        "tags": [],
                        "isSyncReport": False
                    }
                ]
                }
    res = req.post(url,json=payload,headers=header)
    env["test-campId"] = res.json()["id"]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-campId"] == res.json()["id"]

def test_delete_superlink():
    url = f"{env['parse-url']}/link/api/v1/organizations/{env['test-organizationId']}/campaigns/{env['test-campId']}"
    res = req.delete(url,headers=header)
    assert res.status_code == 200
    

def test_confirm_superlink_was_deleted():
    url = f"{env['parse-url']}/link/api/v1/organizations/{env['test-organizationId']}/campaigns/"
    param = {"Authorization":f"Bearer {env['sessionToken']}","page": 1,"pageSize": 20}
    res = req.get(url,params=param,headers=header)
    assert res.json()["rows"][0]["id"] != env['test-campId']