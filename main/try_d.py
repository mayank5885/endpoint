obj1=[
    {
        "filename": "AtlassianJiraAudit_ccpv2/JiraAudit_PollingConfig.json",
        "content": {
            "name": "AtlassianJiraCCPPolling_wrong",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
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
    }
]

for i in obj1:
    print(type(i["filename"]))
    if "pollr" in i["filename"].lower():
        if(type(i["content"])==list):
            print(1)
            if(i["content"][0]["type"] !="Microsoft.SecurityInsights/dataConnectors"):
                check="failed"
                print(check+f"hello {i["content"][0]["type"]}")
            else :
                check="pass"
                print(check+f"hello {i["content"][0]["type"]}")
            
        else:
            print(2)
            if(i["content"]["type"] !="Microsoft.SecurityInsights/dataConnectors"):
                check="failed"
                print(check)
            else :
                check="pass"
                print(check)

