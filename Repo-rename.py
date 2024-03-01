import csv
import requests
 
def update_repository(old_name, new_name):
    url = f"https://api.github.com/repos/devtools-probot-sandbox/{old_name}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    data = {
        "name": new_name,
        "private": True
    }
 
    response = requests.patch(url, headers=headers, json=data)
    return response
 
# Read old and new repository names from CSV
with open('Book2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        old_name = row['old_name']
        new_name = row['new_name']
        response = update_repository(old_name, new_name)
        print(f"Updating repository {old_name} to {new_name}: {response.status_code}")