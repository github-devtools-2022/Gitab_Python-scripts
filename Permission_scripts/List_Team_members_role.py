import csv
import requests

# Replace with your GitHub token and organization name
GITHUB_TOKEN = '<YOUR_TOKEN>'
ORG_NAME = '<YOUR_ORG>'
CSV_FILE = f'ORG_team_members.csv'

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'X-GitHub-Api-Version': '2022-11-28'
}

def get_paginated_results(url, headers):
    results = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            results.extend(response.json())
            # Check if there is a next page
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                url = None
        else:
            raise Exception(f"Error fetching data: {response.status_code} {response.text}")
    return results

def get_teams(org_name):
    url = f'https://api.github.com/orgs/{org_name}/teams'
    return get_paginated_results(url, headers)

def get_team_members(org_name, team_slug):
    url = f'https://api.github.com/orgs/{org_name}/teams/{team_slug}/members'
    return get_paginated_results(url, headers)

def get_team_member_membership(org_name, team_slug, username):
    url = f'https://api.github.com/orgs/{org_name}/teams/{team_slug}/memberships/{username}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching team member membership: {response.status_code} {response.text}")

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Team Name', 'Username', 'Role'])
        for row in data:
            writer.writerow(row)

def main():
    try:
        data = []
        print("Fetching teams in the organization...")
        # Get all teams in the organization
        teams = get_teams(ORG_NAME)
        print(f"Found {len(teams)} teams.")

        for team in teams:
            team_slug = team['slug']
            team_name = team['name']
            print(f"Fetching members for team '{team_name}' (slug: {team_slug})...")
            # Get members of the current team
            members = get_team_members(ORG_NAME, team_slug)
            print(f"Found {len(members)} members in team '{team_name}'.")

            for member in members:
                username = member['login']
                print(f"Fetching membership details for user '{username}' in team '{team_name}'...")
                membership = get_team_member_membership(ORG_NAME, team_slug, username)
                role = membership['role']
                data.append([team_name, username, role])
                print(f"User '{username}' has role '{role}' in team '{team_name}'.")

        # Save to CSV
        print("Saving data to CSV file...")
        save_to_csv(data, CSV_FILE)
        print(f"Team members have been saved to {CSV_FILE}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
