import requests
import csv

# Define your repositories
repositories = ['nos', 'java', 'MapCache', 'golang']   //Add the repo names to list repo team & teammembers permision
# Your GitHub Personal Access Token
token = 'YOUR_TOKRN'
# The base URL for GitHub API
base_url = 'https://api.github.com'
# Your GitHub organization name
org_name = '<YOUR_ORG>'

# Prepare the header for authentication
headers = {'Authorization': f'token {token}'}

# Function to fetch teams for a repository
def fetch_teams(repo):
    url = f'{base_url}/repos/{org_name}/{repo}/teams'
    response = requests.get(url, headers=headers)
    print(f'Fetching teams for repository: {repo}')
    if response.status_code == 200:
        print(f'Successfully fetched teams for {repo}')
    else:
        print(f'Failed to fetch teams for {repo}, status code: {response.status_code}')
    return response.json()

# Function to fetch team members and their roles with pagination support
def fetch_team_members_and_roles(team_slug):
    members_with_roles = []
    page = 1

    while True:
        members_url = f'{base_url}/orgs/{org_name}/teams/{team_slug}/members?page={page}'
        members_response = requests.get(members_url, headers=headers)
        print(f'Fetching members for team: {team_slug}, page: {page}')
        
        if members_response.status_code == 200:
            members = members_response.json()
            if not members:
                break

            print(f'Successfully fetched members for team {team_slug}, page {page}')
            for member in members:
                membership_url = f'{base_url}/orgs/{org_name}/teams/{team_slug}/memberships/{member["login"]}'
                membership_response = requests.get(membership_url, headers=headers)
                print(f'Fetching role for member: {member["login"]} in team {team_slug}')
                if membership_response.status_code == 200:
                    print(f'Successfully fetched role for member {member["login"]} in team {team_slug}')
                else:
                    print(f'Failed to fetch role for member {member["login"]} in team {team_slug}, status code: {membership_response.status_code}')
                membership_info = membership_response.json()

                # Append member info along with role to the list
                members_with_roles.append({
                    'login': member['login'],
                    'role': membership_info.get('role', 'N/A')
                })

            page += 1
        else:
            print(f'Failed to fetch members for team {team_slug}, status code: {members_response.status_code}')
            break

    return members_with_roles

# Prepare data for CSV
data_for_csv = []

for repo in repositories:
    teams = fetch_teams(repo)
    for team in teams:
        team_slug = team['slug']
        members_with_roles = fetch_team_members_and_roles(team_slug)
        for member in members_with_roles:
            data_for_csv.append([repo, team['name'], member['login'], member['role']])
            print(f'Added data for member {member["login"]} in team {team["name"]} for repository {repo}')

# Export to CSV
csv_file_name = 'nos_teams_members_roles.csv'
with open(csv_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Repository', 'Team Name', 'Member Username', 'Role'])
    writer.writerows(data_for_csv)
    print(f'Exported data to {csv_file_name}')

print('Script execution completed')
