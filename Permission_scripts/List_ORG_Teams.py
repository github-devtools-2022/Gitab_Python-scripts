# get the list of github org teams
import requests
import csv

BASE_URL = "https://api.github.com"
TOKEN = "<YOUR_TOKEN>"
owner = "<YOUR_ORG>"
HEADERS = {
    "Accept": "application/vnd.github+json" ,
    "Authorization": f"Bearer {TOKEN}" ,
    "X-GitHub-Api-Version": "2022-11-28"  ,
}

def get_org_teams(owner):
    teams = []
    page = 1
    while True:
        url = f"{BASE_URL}/orgs/{owner}/teams?page={page}&per_page=100"  # Adjust per_page as needed
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # This will stop the loop if an error occurs
        page_teams = response.json()
        if not page_teams:  # If the page is empty, stop the loop
            break
        teams.extend(page_teams)
        page += 1
    return teams

# add pagenation 


def write_teams_to_csv(teams):
    with open("chpt-emutesteams.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "description", "privacy", "url", "permission"])
        for team in teams:
            writer.writerow([team["id"], team["name"], team["description"], team["privacy"], team["url"], team["permission"]])

teams = get_org_teams(owner)
write_teams_to_csv(teams)
print(f"Exported {len(teams)} teams to teams.csv")
