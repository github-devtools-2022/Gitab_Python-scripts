import requests
import csv

# Function to read CSV file and return team names, user names, and roles
def read_csv(file_path):
    teams_and_users = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            team_name, user_name, role = row
            teams_and_users.append((team_name.strip(), user_name.strip(), role.strip()))
    return teams_and_users

# Function to add members to organization teams
def add_members_to_teams(teams_and_users, org_name, token):
    base_url = f"https://api.github.com/orgs/{org_name}/teams"

    for team, user, role in teams_and_users:
        url = f"{base_url}/{team}/memberships/{user}"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        payload = {"role": role}
        response = requests.put(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            print(f"Successfully added {user} to {team} team as a {role}.")
        else:
            print(f"Failed to add {user} to {team} team. Status code: {response.status_code}, Response: {response.json()}")

# Main function
def main():
    file_path = 'teamsuser2.csv'  # Path to CSV file containing team names, user names, and roles
    org_name = '<YOUR_ORG>'  # Organization name
    token = '<YOUR_TOKEN>'  # Personal access token
    
    teams_and_users = read_csv(file_path)
    add_members_to_teams(teams_and_users, org_name, token)

if __name__ == "__main__":
    main()
