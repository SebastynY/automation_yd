URL = 'https://api.direct.yandex.com/json/v5/reports'
TOKEN = ''
LOGIN = ''
BODY = {
    "params": {
        "SelectionCriteria": {
        },
        "FieldNames": [
            "Date",
            "CampaignName",
            "CampaignId",
            "Clicks",
            "Cost",
            "Ctr",
            "Impressions",
        ],
        "ReportName": "Yesterday Costs Report",
        "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
        "DateRangeType": "LAST_WEEK",
        "Format": "TSV",
        "IncludeVAT": "YES",
        "IncludeDiscount": "NO"
    }
}
HEADER = {"Authorization": "Bearer " + TOKEN,
          "Client-Login": LOGIN,
          "Accept-Language": "en",
          "skipReportHeader": "true",
          "returnMoneyInMicros": "false",
          "skipReportSummary": "true"
          }
FORM_DATETIME = '%Y-%m-%d-%Hh%Mm%Ss'
