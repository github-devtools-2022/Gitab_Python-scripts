import requests
import csv

TOKEN = 'glpat-nJX9i3StVsZY7nFnX5sg'

CSV_FILE = 'Viri_Instense_users227.csv'

Baseurl = "https://git.viriciti.com/api/v4/users"


with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "username",	"name", "state", "locked", "avatar_url", "web_url", "created_at", "bio", "location", "public_email", "skype", "linkedin", "twitter", "discord", "website_url", "organization", "job_title", "pronouns", "bot", "work_information", "followers", "following", "is_followed", "local_time", "last_sign_in_at", "confirmed_at", "last_activity_on", "email", "theme_id", "color_scheme_id", "projects_limit", "current_sign_in_at", "can_create_group", "can_create_project", "two_factor_enabled", "external", "private_profile", "commit_email", "is_admin", "note", "namespace_id", "created_by_id", "created_by_username", "created_by_name", "created_by_state", "created_by_locked", "created_by_avatar_url", "created_by_web_url", "email_reset_offered_at"])

    page = 1
    while True:
        response = requests.get(f"{Baseurl}?statistics=true&page={page}",
                          headers={"PRIVATE-TOKEN": TOKEN})
        
        if response.status_code != 200:
            print(response.json())
            break

        users = response.json()
        for user in users:
            writer.writerow([user.get(key, "") for key in ["id", "username", "name", "state", "locked", "avatar_url", "web_url", "created_at", "bio", "location", "public_email", "skype", "linkedin", "twitter", "discord", "website_url", "organization", "job_title", "pronouns", "bot", "work_information", "followers", "following", "is_followed", "local_time", "last_sign_in_at", "confirmed_at", "last_activity_on", "email", "theme_id", "color_scheme_id", "projects_limit", "current_sign_in_at", "can_create_group", "can_create_project", "two_factor_enabled", "external", "private_profile", "commit_email", "is_admin", "note", "namespace_id", "created_by_id", "created_by_username", "created_by_name", "created_by_state", "created_by_locked", "created_by_avatar_url", "created_by_web_url", "email_reset_offered_at"]])

        if 'next' not in response.links:
            break
        page += 1
