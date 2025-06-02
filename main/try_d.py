obj1=[
    {
        "filename": "AtlassianJiraAudit_ccpv2/JiraAudit_PollingConfig.json",
        "content": {
            "name": "AtlassianJiraCCPPolling",
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
        "filename": "ErmesBrowserSecurityEvents_ccp/data_connector_definition.json",
        "content": {
            "type": "Microsoft.SecurityInsights/dataConnectorDefinitions",
            "apiVersion": "2022-09-01-preview",
            "name": "ErmesBrowserSecurityEvents",
            "location": "{{location}}",
            "kind": "Customizable",
            "properties": {
                "connectorUiConfig": {
                    "id": "ErmesBrowserSecurityEvents",
                    "title": "Ermes Browser Security Events",
                    "publisher": "Ermes Cyber Security S.p.A.",
                    "descriptionMarkdown": "Ermes Browser Security Events",
                    "graphQueriesTableName": "ErmesBrowserSecurityEvents_CL",
                    "graphQueries": [
                        {
                            "metricName": "Total events received",
                            "legend": "Ermes Events",
                            "baseQuery": "{{graphQueriesTableName}}"
                        }
                    ],
                    "sampleQueries": [
                        {
                            "description": "Get Sample of Ermes Events",
                            "query": "{{graphQueriesTableName}}\n | take 10"
                        }
                    ],
                    "dataTypes": [
                        {
                            "name": "{{graphQueriesTableName}}",
                            "lastDataReceivedQuery": "{{graphQueriesTableName}}\n | where TimeGenerated > ago(12h) | where name_s == \"no data test\" | summarize Time = max(TimeGenerated)\n | where isnotempty(Time)"
                        }
                    ],
                    "connectivityCriteria": [
                        {
                            "type": "HasDataConnectors"
                        }
                    ],
                    "availability": {
                        "isPreview": False
                    },
                    "permissions": {
                        "resourceProvider": [
                            {
                                "provider": "Microsoft.OperationalInsights/workspaces",
                                "permissionsDisplayText": "Read and Write permissions are required.",
                                "providerDisplayName": "Workspace",
                                "scope": "Workspace",
                                "requiredPermissions": {
                                    "write": True,
                                    "read": True,
                                    "delete": True
                                }
                            },
                            {
                                "provider": "Microsoft.OperationalInsights/workspaces/sharedKeys",
                                "permissionsDisplayText": "Read permissions to shared keys for the workspace are required. [See the documentation to learn more about workspace keys](https://docs.microsoft.com/azure/azure-monitor/platform/agent-windows#obtain-workspace-id-and-key)",
                                "providerDisplayName": "Keys",
                                "scope": "Workspace",
                                "requiredPermissions": {
                                    "action": True
                                }
                            }
                        ],
                        "customs": [
                            {
                                "name": "Ermes Client Id and Client Secret",
                                "description": "Enable API access in Ermes. Please contact [Ermes Cyber Security](https://www.ermes.company) support for more information."
                            }
                        ]
                    },
                    "instructionSteps": [
                        {
                            "description": "Connect using OAuth2 credentials",
                            "instructions": [
                                {
                                    "type": "OAuthForm",
                                    "parameters": {
                                        "clientIdLabel": "Client ID",
                                        "clientSecretLabel": "Client Secret",
                                        "connectButtonLabel": "Connect",
                                        "disconnectButtonLabel": "Disconnect"
                                    }
                                }
                            ],
                            "title": "Connect Ermes Browser Security Events to Microsoft Sentinel"
                        }
                    ]
                }
            }
        }
    }
]


# def check_polling(nameFile):
#     j=0
#     checkName=Polling
#     for i in nameFile:



for i in obj1:
    if(i["content"]["type"] !="Microsoft.SecurityInsights/dataConnectors"):
        check="failed"
        break
    else :
        check="pass"

print(check)