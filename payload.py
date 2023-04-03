import mo
import time

env = mo.read_jsonfile()

def queryTemplate_confirm_card():
    p = {
            "where": {
                "organization": {
                    "__type": "Pointer",
                    "className": "Organization",
                    "objectId": f"{env['test-organizationId']}"
                },
                "version": {
                    "$exists": False
                },
                "templateType": "confirm",
                "vendor": {
                    "$ne": True
                }
            },
            "sort": {
                "updatedAt": -1
            },
            "group": False,
            "limit": 50,
            "_ApplicationId": f"{env['parse-app-id']}",
            "_JavaScriptKey": "javascriptKey",
            "_ClientVersion": "js1.11.1",
            "_SessionToken": f"{env['sessionToken']}"
             }
    return p

def queryTemplate_options_card():
    p = {
              "where": {
              "organization": {
              "__type": "Pointer",
              "className": "Organization",
              "objectId": f"{env['test-organizationId']}"
              },
              "version": {
                          "$exists": False
              },
              "templateType": "card",
              "vendor": {
                         "$ne": True
                    }
                },
              "sort": {
                        "updatedAt": -1
                },
              "group": False,
              "limit": 50,
              "_ApplicationId": f"{env['parse-app-id']}",
              "_JavaScriptKey": "javascriptKey",
              "_ClientVersion": "js1.11.1",
              "_SessionToken": f"{env['sessionToken']}"
               }
    return p

def sand_line_message(type,message,):
    t = str(time.time())
    p = {
                "events": [
                    {
                        "type": type,
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
    return p

def functions_keep(tt): 
    p = {
        "conversation": {
            "className": "Conversation",
            "objectId": f"{env['test-conversationId']}"
        },
        "message": {
            "className": "Message",
            "objectId": tt
        },
        "owner": {
            "className": "_User",
            "objectId": f"{env['test-accountId']}"
        },
        "_ApplicationId": f"{env['parse-app-id']}",
        "_JavaScriptKey": "javascriptKey",
        "_SessionToken": f"{env['sessionToken']}"
         }
    return p

def classes_customer():
    p = {       
        "limit": 1,
        "where": {
            "objectId": f"{env['test-user-objectId']}"
        },
        "include": "customer",
        "_method": "GET",
        "_ApplicationId": f"{env['parse-app-id']}",
        "_JavaScriptKey": "javascriptKey",
        "_SessionToken": f"{env['sessionToken']}"
        }
    return p

def functions_updateCustomFields(cf):
    p = {
        "where": {
            "orgId": f"{env['test-organizationId']}"
        },
        "fields": [
            {
                "type": "text",
                "id": "45dfd088-241c-43e2-a42d-1beb5f4eac88",
                "name": cf,
                "placeholder": "key-in"
            }
        ],
        "_ApplicationId": f"{env['parse-app-id']}",
        "_JavaScriptKey": "javascriptKey",
        "_SessionToken": f"{env['sessionToken']}"
        }
    return p

def functions_assign_for_private():
    p = {
                "inbox": "private",
                "from": {
                    "className": "_User",
                    "objectId": f"{env['test-adm-objectId_2']}"
                },
                "customer": {
                    "className": "Customer",
                    "objectId": f"{env['test-user-objectId']}"
                },
                "organization": {
                    "className": "Organization",
                    "objectId": f"{env['test-organizationId']}"
                },
                "toUser": {
                    "className": "_User",
                    "objectId": f"{env['test-adm-objectId_1']}"
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_ClientVersion": "js1.11.1",
                "_SessionToken": f"{env['sessionToken']}"
                }
    return p

def functions_assign(kw):
    p = {
                "inbox": kw,
                "from": {
                    "className": "_User",
                    "objectId": f"{env['test-adm-objectId_1']}"
                },
                "customer": {
                    "className": "Customer",
                    "objectId": f"{env['test-user-objectId']}"
                },
                "organization": {
                    "className": "Organization",
                    "objectId": f"{env['test-organizationId']}"
                },
                "_ApplicationId": f"{env['parse-app-id']}",
                "_JavaScriptKey": "javascriptKey",
                "_SessionToken": f"{env['sessionToken']}"
                }
    return p