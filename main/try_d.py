obj1=[
    {
        "filename": "AtlassianJiraAudit_ccpv2/JiraAudit_PollingConfig.json",
        "content": {
            "name": "AtlassianJiraCCPPolling",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors_wrong",
            "location": "{{location}}",
            "kind": "RestApiPoller",
            "properties": {
                "connectorDefinitionName": "JiraAuditCCPDefinition",
                "dataType": "Jira_Audit_v2_CL",
                "dcrConfig": {
                    "dataCollectionEndpoint": "{{dataCollectionEndpoint}}",
                    "dataCollectionRuleImmutableId": "{{dataCollectionRuleImmutableId}}",
                    "streamName": "Custom-Jira_Audit_v2_CL"
                },
                "auth": {
                    "type": "Basic",
                    "UserName": "{{userid}}",
                    "Password": "{{apikey}}"
                },
                "request": {
                    "apiEndpoint": "https://{{jiraorganizationurl}}/rest/api/3/auditing/record",
                    "httpMethod": "GET",
                    "retryCount": 3,
                    "timeoutInSeconds": 60,
                    "queryTimeFormat": "yyyy-MM-ddTHH:mm:ssZ",
                    "headers": {
                        "Accept": "application/json",
                        "User-Agent": "Scuba"
                    },
                    "startTimeAttributeName": "from",
                    "endTimeAttributeName": "to"
                },
                "paging": {
                    "pagingType": "Offset",
                    "offsetParaName": "offset",
                    "pageSizeParaName": "limit",
                    "pageSize": 1000
                },
                "response": {
                    "eventsJsonPaths": [
                        "$.records"
                    ],
                    "format": "json"
                }
            }
        }
    },
    {
        "filename": "GoogleCloudPlatformAudit Logs_ccp/data_connector_poller.json",
        "content": [
            {
                "type": "Microsoft.SecurityInsights/dataConnectors",
                "apiVersion": "2022-10-01-preview",
                "name": "{{workspace}}/Microsoft.SecurityInsights/GCPAuditLogs",
                "kind": "GCP",
                "properties": {
                    "connectorDefinitionName": "GCPAuditLogsDefinition",
                    "dataType": "GCPAuditLogs",
                    "dcrConfig": {
                        "streamName": "SENTINEL_GCP_AUDIT_LOGS"
                    },
                    "auth": {
                        "serviceAccountEmail": "{{GCPServiceAccountEmail}}",
                        "projectNumber": "{{GCPProjectNumber}}",
                        "workloadIdentityProviderId": "{{GCPWorkloadIdentityProviderId}}"
                    },
                    "request": {
                        "projectId": "{{GCPProjectId}}",
                        "subscriptionNames": [
                            "{{GCPSubscriptionName}}"
                        ]
                    }
                }
            }
        ]
    },
    {
        "filename": "file2_JiraAudit_Polling",
        "content": {
            "name": "AtlassianJiraCCPPolling",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors_wrong",
            "location": "{{location}}",
            "kind": "RestApiPoller",
            "properties": {
                "connectorDefinitionName": "JiraAuditCCPDefinition",
                "dataType": "Jira_Audit_v2_CL",
                "dcrConfig": {
                    "dataCollectionEndpoint": "{{dataCollectionEndpoint}}",
                    "dataCollectionRuleImmutableId": "{{dataCollectionRuleImmutableId}}",
                    "streamName": "Custom-Jira_Audit_v2_CL"
                },
                "auth": {
                    "type": "Basic",
                    "UserName": "{{userid}}",
                    "Password": "{{apikey}}"
                },
                "request": {
                    "apiEndpoint": "https://{{jiraorganizationurl}}/rest/api/3/auditing/record",
                    "httpMethod": "GET",
                    "retryCount": 3,
                    "timeoutInSeconds": 60,
                    "queryTimeFormat": "yyyy-MM-ddTHH:mm:ssZ",
                    "headers": {
                        "Accept": "application/json",
                        "User-Agent": "Scuba"
                    },
                    "startTimeAttributeName": "from",
                    "endTimeAttributeName": "to"
                },
                "paging": {
                    "pagingType": "Offset",
                    "offsetParaName": "offset",
                    "pageSizeParaName": "limit",
                    "pageSize": 1000
                },
                "response": {
                    "eventsJsonPaths": [
                        "$.records"
                    ],
                    "format": "json"
                }
            }
        }
    },
        {
        "filename": "file3_JiraAudit_Polling",
        "content": {
            "name": "AtlassianJiraCCPPolling",
            "apiVersion": "2022-12-01-preview",
            "location": "{{location}}",
            "kind": "RestApiPoller",
            "properties": {
                "connectorDefinitionName": "JiraAuditCCPDefinition",
                "dataType": "Jira_Audit_v2_CL",
                "dcrConfig": {
                    "dataCollectionEndpoint": "{{dataCollectionEndpoint}}",
                    "dataCollectionRuleImmutableId": "{{dataCollectionRuleImmutableId}}",
                    "streamName": "Custom-Jira_Audit_v2_CL"
                },
                "paging": {
                    "pagingType": "Offset",
                    "offsetParaName": "offset",
                    "pageSizeParaName": "limit",
                    "pageSize": 1000
                },
                "response": {
                    "eventsJsonPaths": [
                        "$.records"
                    ],
                    "format": "json"
                }
            }
        }
    }    ,{
        "filename": "file4poller.json",
        "content": [
            {
                "type": "Microsoft.SecurityInsights/dataConnectors",
                "apiVersion": "2022-10-01-preview",
                "name": "{{workspace}}/Microsoft.SecurityInsights/GCPAuditLogs",
                "kind": "GCP",
                "properties": {
                    "connectorDefinitionName": "GCPAuditLogsDefinition",
                    "dataType": "GCPAuditLogs",
                    "dcrConfig": {
                        "streamName": "SENTINEL_GCP_AUDIT_LOGS"
                    },
                    "request": {
                        "projectId": "{{GCPProjectId}}",
                        "subscriptionNames": [
                            "{{GCPSubscriptionName}}"
                        ]
                    }
                }
            }
        ]
    }





]

errorMessage=""
flag=True
temp={}
for i in obj1:
    title=i["filename"]
    if "poll" in title.lower():
            errorMessage+= "\n \n"+ title+ "- \n \n"
            if(type(i["content"])==list):
                temp=i["content"][0]
            else:
                temp=i["content"]

            if "type" in temp:
                if(temp["type"] !="Microsoft.SecurityInsights/dataConnectors"):
                        ele=temp["type"]
                        errorMessage+="File has element type - "+ele+" it should be  Microsoft.SecurityInsights/dataConnectors \n"
                        flag=False
            else:
                errorMessage+="File doesn't have element-type \n"
                flag=False 

            if "kind" in temp:
                if(temp["kind"]=="RestApiPoller"):

                    if "auth" in temp["properties"]:
                        pass
                    else:
                        errorMessage+="File doesn't have element- properties.auth \n"
                        flag=False 

                    if "request" in temp["properties"]:
                        pass
                    else:
                        errorMessage+="File doesn't have element- properties.request \n"
                        flag=False   

                    if "response" in temp["properties"]:
                        pass
                    else:
                        errorMessage+="File doesn't have element- properties.response \n"
                        flag=False                                            
                
                elif(temp["kind"]=="GCP"):

                    if "auth" in temp["properties"]:
                        pass
                    else:
                        errorMessage+="File doesn't have element- properties.auth \n"
                        flag=False 

                    if "request" in temp["properties"]:
                        pass
                    else:
                        errorMessage+="File doesn't have element- properties.request \n"
                        flag=False  

            else:
                errorMessage+="File doesn't have element-kind \n"
                flag=False 



if(flag):
    print("all clear")
else:
    print(errorMessage)





