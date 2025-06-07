data=[
    {
        "filename": "AtlassianJiraAudit_ccpv2/JiraAudit_DataConnectorDefinition.json",
        "content": {
            "name": "JiraAuditCCPDefinition",
            "apiVersion": "2022-09-01-preview",
            "type": "Microsoft.SecurityInsights/Wrong",
            "location": "{{location}}",
            "kind": "Customizable",
            "availability": {
                "isPreview": False
            },
            "properties": {
                "connectorUiConfig": {
                    "title": "Atlassian Jira Audit (using REST API)",
                    "id": "JiraAuditCCPDefinition",
                    "publisher": "Microsoft",
                    "descriptionMarkdown": "The [Atlassian Jira](https://www.atlassian.com/software/jira) Audit data connector provides the capability to ingest [Jira Audit Records](https://support.atlassian.com/jira-cloud-administration/docs/audit-activities-in-jira-applications/) events into Microsoft Sentinel through the REST API. Refer to [API documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-audit-records/) for more information. The connector provides ability to get events which helps to examine potential security risks, analyze your team's use of collaboration, diagnose configuration problems and more.",
                    "graphQueriesTableName": "Jira_Audit_v2_CL",
                    "graphQueries": [
                        {
                            "metricName": "Total data received",
                            "legend": "Jira Audit Events",
                            "baseQuery": "{{graphQueriesTableName}}"
                        }
                    ],
                    "sampleQueries": [
                        {
                            "description": "All Atlassian Jira audit logs",
                            "query": "{{graphQueriesTableName}}\n| sort by TimeGenerated desc"
                        },
                        {
                            "description": "Total Events",
                            "query": "{{graphQueriesTableName}}\n | summarize count() by OriginalEventUid"
                        }
                    ],
                    "dataTypes": [
                        {
                            "name": "{{graphQueriesTableName}}",
                            "lastDataReceivedQuery": "{{graphQueriesTableName}}|summarize Time = max  (TimeGenerated)\n|where isnotempty(Time)"
                        }
                    ],
                    "connectivityCriteria": [
                        {
                            "type": "HasDataConnectors"
                        }
                    ],
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
                            }
                        ],
                        "customs": [
                            {
                                "name": "Atlassian Jira API access",
                                "description": "Permission of [Administer Jira](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#authentication) is required to get access to the Jira Audit logs API. See [Jira API documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-audit-records/#api-group-audit-records) to learn more about the audit API."
                            }
                        ]
                    },
                    "instructionSteps": [
                        {
                            "description": "To enable the Atlassian Jira connector for Microsoft Sentinel, click to add an organization, fill the form with the Jira environment credentials and click to Connect. \n Follow [these steps](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) to create an API token.\n ",
                            "instructions": [
                                {
                                    "type": "DataConnectorsGrid",
                                    "parameters": {
                                        "mapping": [
                                            {
                                                "columnName": "Atlassian Jira organization URL",
                                                "columnValue": "properties.request.apiEndpoint"
                                            }
                                        ],
                                        "menuItems": [
                                            "DeleteConnector"
                                        ]
                                    }
                                },
                                {
                                    "type": "ContextPane",
                                    "parameters": {
                                        "isPrimary": True,
                                        "label": "Add organization",
                                        "title": "Add organization",
                                        "subtitle": "Add Atlassian Jira organization",
                                        "contextPaneType": "DataConnectorsContextPane",
                                        "instructionSteps": [
                                            {
                                                "instructions": [
                                                    {
                                                        "type": "Textbox",
                                                        "parameters": {
                                                            "label": "Atlassian Jira organization URL",
                                                            "placeholder": "Atlassian Jira organization URL",
                                                            "type": "string",
                                                            "name": "jiraorganizationurl"
                                                        }
                                                    },
                                                    {
                                                        "type": "Textbox",
                                                        "parameters": {
                                                            "label": "User Name",
                                                            "placeholder": "User Name (e.g., user@example.com)",
                                                            "type": "securestring",
                                                            "name": "userid"
                                                        }
                                                    },
                                                    {
                                                        "type": "Textbox",
                                                        "parameters": {
                                                            "label": "API Key",
                                                            "placeholder": "API Key",
                                                            "type": "password",
                                                            "name": "apikey"
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    },
    {
        "filename": "GoogleCloudPlatformAudit Logs_ccp/data_connector_definition.json",
        "content": {
            "type": "Microsoft.SecurityInsights/dataConnectorDefinitions",
            "name": "{{workspace}}/Microsoft.SecurityInsights/GCPAuditLogsDefinition",
            "kind": "Customizable",
            "properties": {
                "connectorUiConfig": {
                    "id": "GCPAuditLogsDefinition",
                    "title": "GCP Pub/Sub Audit Logs",
                    "publisher": "Microsoft",
                    "descriptionMarkdown": "The Google Cloud Platform (GCP) audit logs, ingested from Microsoft Sentinel's connector, enables you to capture three types of audit logs: admin activity logs, data access logs, and access transparency logs. Google cloud audit logs record a trail that practitioners can use to monitor access and detect potential threats across Google Cloud Platform (GCP) resources.",
                    "graphQueriesTableName": "GCPAuditLogs",
                    "graphQueries": [
                        {
                            "metricName": "Total events received",
                            "legend": "GCP Audit Logs",
                            "baseQuery": "{{graphQueriesTableName}}"
                        }
                    ],
                    "sampleQueries": [
                        {
                            "description": "Get Sample of GCP Audit Logs",
                            "query": "{{graphQueriesTableName}}\n | take 10"
                        }
                    ],
                    "dataTypes": [
                        {
                            "name": "{{graphQueriesTableName}}",
                            "lastDataReceivedQuery": "{{graphQueriesTableName}}\n | where TimeGenerated > ago(12h) | summarize Time = max(TimeGenerated)\n | where isnotempty(Time)"
                        }
                    ],
                    "connectivityCriteria": [
                        {
                            "type": "HasDataConnectors"
                        }
                    ],
                    "availability": {
                        "status": 1,
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
                                    "read": True,
                                    "write": True,
                                    "delete": True,
                                    "action": False
                                }
                            }
                        ]
                    },
                    "instructionSteps": [
                        {
                            "instructions": [
                                {
                                    "type": "MarkdownControlEnvBased",
                                    "parameters": {
                                        "prodScript": "#### 1. Set up your GCP environment \n You must have the following GCP resources defined and configured: topic, subscription for the topic, workload identity pool, workload identity provider and service account with permissions to get and consume from subscription. \n Terraform provides API for the IAM that creates the resources. [Link to Terraform scripts](https://github.com/Azure/Azure-Sentinel/tree/master/DataConnectors/GCP/Terraform/sentinel_resources_creation).",
                                        "govScript": "#### 1. Set up your GCP environment \n You must have the following GCP resources defined and configured: topic, subscription for the topic, workload identity pool, workload identity provider and service account with permissions to get and consume from subscription. \n Terraform provides API for the IAM that creates the resources. [Link to Gov Terraform scripts](https://github.com/Azure/Azure-Sentinel/tree/master/DataConnectors/GCP/Terraform/sentinel_resources_creation_gov)."
                                    }
                                },
                                {
                                    "type": "CopyableLabel",
                                    "parameters": {
                                        "label": "Tenant ID: A unique identifier that is used as an input in the Terraform configuration within a GCP environment.",
                                        "fillWith": [
                                            "TenantId"
                                        ],
                                        "name": "TenantId",
                                        "disabled": True
                                    }
                                },
                                {
                                    "type": "Markdown",
                                    "parameters": {
                                        "content": "#### 2. Connect new collectors \n To enable GCP Audit Logs for Microsoft Sentinel, click the Add new collector button, fill the required information in the context pane and click on Connect."
                                    }
                                },
                                {
                                    "type": "GCPGrid",
                                    "parameters": {}
                                },
                                {
                                    "type": "GCPContextPane",
                                    "parameters": {}
                                }
                            ]
                        }
                    ]
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

for i in data:
            if "definition" in i["filename"].lower():
                if(type(i["content"])==list):
                    if(i["content"][0]["type"]["properties"]["connectorUiConfig"]):
                            print("fail 1")
                else:
                    if(i["content"]["type"] !="Microsoft.SecurityInsights/dataConnectorsDefinitions"):
                        print("fail 2")
            
print("last pass")