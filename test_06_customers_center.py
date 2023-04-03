import mo 
import payload as pl
import json
import time
import requests as req

env = mo.read_jsonfile()

def test_export_customergroup():
    url = f"{env['parse-url']}/functions/task.export"
    payload = {
                "i18n": {"locale": "zh-TW",
                         "fileName": "ChrisHsu_20230331024701",
                         "fields": {
                         "displayName": "顯示名稱",
                         "originalDisplayName": "原始名稱平台",
                         "joinedAt": "加入時間",
                         "friendship": "客戶狀態",
                         "tags": "標籤",
                         "elandTag": "Eland標籤",
                         "tagtooTag": "Tagtoo標籤",
                         "email": "電子信箱",
                         "cellPhone": "電話/手機",
                         "gender": "性別",
                         "birthday": "生日",
                         "nation": "國家",
                         "location": "位置（現居城市）",
                         "about": "關於",
                         "objectId": "Super 8 用戶 ID",
                         "customerId": "平台 ID",
                         "customField1": "自訂1",
                         "customField2": "自訂2",
                         "customField3": "自訂3",
                         "hiddenField1": "隱藏1",
                         "hiddenField2": "隱藏2",
                         "platform": "平台"},
                         "sheets": {"main": "ChrisHsu_20230331024701"},
                         "content": {"default": {"null": "無"},
                                     "platform": {"all": "所有平台",
                                                  "facebook": "Messenger",
                                                  "line": "LINE",
                                                  "instagram": "Instagram",
                                                  "whatsapp": "WhatsApp"},
                                     "friendship": {"unfollow": "已封鎖",
                                                    "follow": "有效會員"},
                                     "gender": {"male": "男",
                                                "female": "女",
                                                "other": "其他"}}},
                "groupId": f"{env['test-groupId']}",
                "query": {"orgId": f"{env['test-organizationId']}"},
                "_ApplicationId": "number8",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": "r:c94c734f5fa351e2343962129c9777c3"
                }
    res = req.post(url,json=payload)
    assert res.status_code == 200