import csv
import requests

# Replace with your Jira site and credentials
JIRA_URL = "https://yourdomain.atlassian.net"
API_TOKEN = "your-api-token"
EMAIL = "your-email@example.com"
PROJECT_KEY = "PROJ"

headers = {
    "Authorization": f"Basic {EMAIL}:{API_TOKEN}",
    "Content-Type": "application/json"
}

def import_csv_to_jira(csv_path):
    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            payload = {
                "fields": {
                    "project": {"key": PROJECT_KEY},
                    "summary": row["Summary"],
                    "description": row["Description"],
                    "issuetype": {"name": row["Issue Type"]}
                }
            }
            response = requests.post(f"{JIRA_URL}/rest/api/3/issue", headers=headers, json=payload)
            if response.status_code == 201:
                print(f"✅ Created issue: {row['Summary']}")
            else:
                print(f"❌ Failed to create issue: {row['Summary']} - {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    import_csv_to_jira("Jira_Import_YYYYMMDD_HHMMSS.csv")
