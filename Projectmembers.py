import csv
import requests

TOKEN = "glpat-nJX9i3StVsZY7nFnX5sg"  # Replace with your actual private token

# Specify the CSV file path
CSV_FILE = "VIR-project-user227.csv"

# List of project IDs
PROJECT_IDS = [
171,170,169,168,167,165,163,161,160,158,157,155,154,153,152,150,148,145,142,141,140,139,138,137,136,135,133,130,129,128,127,123,122,120,119,118,115,114,113,109,108,105,104,103,100,94,93,92,90,89,88,86,85,84,82,81,80,79,78,77,76,75,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,54,53,52,51,50,49,48,47,46,45,44,42,41,39,38,37,36,35,32,30,29,28,27,26,25,24,23,22,21,20,19,17,14,13,12,11,10,9,8,7,5,4,3,1
]


def fetch_project_info(project_id):
    url = f"https://git.viriciti.com/api/v4/projects/{project_id}"
    headers = {"PRIVATE-TOKEN": TOKEN}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
    
    print("runing the {project_id}")


def fetch_members(project_id):
    url = f"https://git.viriciti.com/api/v4/projects/{project_id}/members/all"
    headers = {"PRIVATE-TOKEN": TOKEN}
    members = []
    page = 1
    per_page = 100
    while True:
        params = {"page": page, "per_page": per_page}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        members_data = response.json()
        members.extend(members_data)
        if not members_data:
            break
        page += 1
    return members


def main(): 
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            [
                "id", "path", "path_with_namespace", "namespacekind", "web_url",
                "last_activity_at", "empty_repo", "archived", "visibility",
                "member_id", "username", "name", "access_level"
            ]
        )

        for project_id in PROJECT_IDS:
            try:
                project_info = fetch_project_info(project_id)
                project_id = project_info["id"]
                path = project_info["path"]
                path_with_namespace = project_info["path_with_namespace"]
                namespacekind = project_info["namespace"]["kind"]
                web_url = project_info["web_url"]
                last_activity_at = project_info["last_activity_at"]
                empty_repo = project_info["empty_repo"]
                archived = project_info["archived"]
                visibility = project_info["visibility"]
            except Exception as e:
                print(f"Error fetching project information for project {project_id}: {e}")
                continue

            for member in fetch_members(project_id):
                try:
                    member_id = member["id"]
                    username = member["username"]
                    name = member["name"]
                    access_level = member["access_level"]
                  
                except Exception as e:
                    print(f"Error processing member data for project {project_id}: {e}")
                    continue

                csv_writer.writerow([
                    project_id, path, path_with_namespace, namespacekind, web_url,
                    last_activity_at, empty_repo, archived, visibility,
                    member_id, username, name, access_level, 
                ])


if __name__ == "__main__":
    main()
