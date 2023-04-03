import mo 
import payload as pl
import json
import time
import requests as req

env = mo.read_jsonfile()

def test_create_MA():
    url = f"{env['test-next-url']}/automation"
    header = {"_SessionToken": f"{env['sessionToken']}"}
    payload = {
                "orgId": f"{env['test-organizationId']}",
                "name": "自動旅程",
                "enabled": True,
                "fbTag": "NO_TAG",
                "platform": "line",
                "startTime": "2023-03-31 00:00",
                "endTime": "2023-04-14 23:59",
                "limits": {},
                           "oos": {"enabled": False,
                           "hour": 22,
                           "minute": 0,
                           "duration": 43200},
                "nodes": [{"id": "0dM7YAZrEr",
                           "type": "start",
                           "position": {"x": 78.00021158831736,"y": 0}
                            },{"id": "XirySkexPx",
                               "type": "trigger",
                               "data": {"type": "join"},
                               "selectable": True,
                               "position": {"x": 0.0008054755235554847,
                                            "y": 131}},
                            {"id": "uuKF84OrDL",
                             "type": "end",
                             "position": {"x": 86.0007165865076,
                                          "y": 323}}],
                "edges": [{
                           "id": "SbCk2oqGcl",
                           "source": "0dM7YAZrEr",
                           "target": "XirySkexPx",
                           "type": "smoothstep"},
                            {"id": "JqtMMSAmru",
                             "source": "XirySkexPx",
                             "target": "uuKF84OrDL",
                             "type": "add"}]
                }
    res = req.post(url,json=payload,headers=header)
    env["test-MA_Id"] = res.json()["procedureId"]
    mo.write_jsonfile(env)
    assert mo.read_jsonfile()["test-MA_Id"] == res.json()["procedureId"]

def test_edit_MA():
    url = f"{env['test-next-url']}/automation/{env['test-MA_Id']}"
    header = {"_SessionToken": f"{env['sessionToken']}"}
    payload = {
                "orgId":f"{env['test-organizationId']}",
                "enabled":True,
                "name":"test MA for API automation",
                "fbTag":"NO_TAG",
                "platform":"line",
                "startTime":mo.set_time(2),
                "endTime":mo.set_time(3),
                "limits":{},
                          "oos":{"enabled":False,
                                 "hour":22,
                                 "minute":0,
                                 "duration":43200},
                                "nodes":[{"id":"0dM7YAZrEr",
                                          "type":"start",
                                          "position":{"x":78.0004331536103,
                                                      "y":0},
                                          "targetPosition":"top",
                                          "sourcePosition":"bottom",
                                          "width":84,
                                          "height":31},
                                          {"id":"XirySkexPx",
                                           "type":"trigger",
                                           "data":{"type":"api"},
                                          "selectable":True,
                                          "position":{"x":0.0006770969643226576,
                                                      "y":131},
                                          "targetPosition":"top",
                                          "sourcePosition":"bottom",
                                          "width":240,
                                          "height":92},
                                          {"type":"message",
                                                  "data":{"name":"訊息 1",
                                                  "waitTime":"",
                                                  "skipOOS":False,
                                                  "messages":[{"contentType":"text/plain",
                                                               "data":{"content":"s8 api觸發~~"},
                                                                       "index":0}]},
                                                  "position":{"x":0.000572529711360765,
                                                              "y":323},
                                                "id":"Ev1DTOW9di",
                                                "targetPosition":"top",
                                                "sourcePosition":"bottom",
                                                "width":240,
                                                "height":160},
                                                {"id":"uuKF84OrDL",
                                                "type":"end",
                                                "position":{"x":86.00094962904457,
                                                            "y":583},
                                                "targetPosition":"top",
                                                "sourcePosition":"bottom",
                                                "width":68,
                                                "height":24}],
                                    "edges":[{"id":"SbCk2oqGcl",
                                              "source":"0dM7YAZrEr",
                                              "target":"XirySkexPx",
                                              "type":"smoothstep"},
                                             {"id":"JqtMMSAmru",
                                              "source":"XirySkexPx",
                                              "target":"Ev1DTOW9di",
                                              "type":"add"},
                                             {"type":"add",
                                              "id":"kYp7hOFcdu",
                                              "source":"Ev1DTOW9di",
                                              "target":"uuKF84OrDL"}]
                 }
    res = req.put(url,json=payload,headers=header)
    assert res.status_code == 200
