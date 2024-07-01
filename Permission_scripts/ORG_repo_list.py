import csv
import requests

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "<YOUR_TOKEN",
    "X-GitHub-Api-Version": "2022-11-28"
}

url = "https://api.github.com/orgs/<YOUR_ORG>/repos"
repos = []

# Function to fetch repositories by handling pagination
def fetch_repositories(url):
    page = 1
    while True:
        response = requests.get(url, headers=headers, params={"page": page})
        data = response.json()
        if not data:  # If no data is found, break the loop
            break
        repos.extend(data)
        page += 1

# Fetch repositories
fetch_repositories(url)

# Define CSV file and headers
csv_file = "<FILE_NAME>.csv"     
csv_headers = [
    "id", "node_id", "name", "full_name", "private", "html_url", "description", "fork",
    "url", "archive_url", "assignees_url", "blobs_url", "branches_url", "collaborators_url",
    "comments_url", "commits_url", "compare_url", "contents_url", "contributors_url",
    "deployments_url", "downloads_url", "events_url", "forks_url", "git_commits_url",
    "git_refs_url", "git_tags_url", "git_url", "issue_comment_url", "issue_events_url",
    "issues_url", "keys_url", "labels_url", "languages_url", "merges_url", "milestones_url",
    "notifications_url", "pulls_url", "releases_url", "ssh_url", "stargazers_url",
    "statuses_url", "subscribers_url", "subscription_url", "tags_url", "teams_url",
    "trees_url", "clone_url", "mirror_url", "hooks_url", "svn_url", "homepage",
    "language", "forks_count", "stargazers_count", "watchers_count", "size", "default_branch",
    "open_issues_count", "is_template", "has_issues", "has_projects", "has_wiki", "has_pages",
    "has_downloads", "has_discussions", "archived", "disabled", "visibility", "pushed_at",
    "created_at", "updated_at", "permissions_admin", "permissions_push", "permissions_pull",
    "security_advanced_security_status", "security_secret_scanning_status",
    "security_secret_scanning_push_protection_status"
]

# Write data to CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=csv_headers)
    writer.writeheader()
    for repo in repos:
        advanced_security_status = repo["security_and_analysis"].get("advanced_security", {}).get("status")
        secret_scanning_status = repo["security_and_analysis"]["secret_scanning"]["status"]
        secret_scanning_push_protection_status = repo["security_and_analysis"]["secret_scanning_push_protection"]["status"]

        repo_data = {
            "id": repo["id"],
            "node_id": repo["node_id"],
            "name": repo["name"],
            "full_name": repo["full_name"],
            "private": repo["private"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "fork": repo["fork"],
            "url": repo["url"],
            "archive_url": repo["archive_url"],
            "assignees_url": repo["assignees_url"],
            "blobs_url": repo["blobs_url"],
            "branches_url": repo["branches_url"],
            "collaborators_url": repo["collaborators_url"],
            "comments_url": repo["comments_url"],
            "commits_url": repo["commits_url"],
            "compare_url": repo["compare_url"],
            "contents_url": repo["contents_url"],
            "contributors_url": repo["contributors_url"],
            "deployments_url": repo["deployments_url"],
            "downloads_url": repo["downloads_url"],
            "events_url": repo["events_url"],
            "forks_url": repo["forks_url"],
            "git_commits_url": repo["git_commits_url"],
            "git_refs_url": repo["git_refs_url"],
            "git_tags_url": repo["git_tags_url"],
            "git_url": repo["git_url"],
            "issue_comment_url": repo["issue_comment_url"],
            "issue_events_url": repo["issue_events_url"],
            "issues_url": repo["issues_url"],
            "keys_url": repo["keys_url"],
            "labels_url": repo["labels_url"],
            "languages_url": repo["languages_url"],
            "merges_url": repo["merges_url"],
            "milestones_url": repo["milestones_url"],
            "notifications_url": repo["notifications_url"],
            "pulls_url": repo["pulls_url"],
            "releases_url": repo["releases_url"],
            "ssh_url": repo["ssh_url"],
            "stargazers_url": repo["stargazers_url"],
            "statuses_url": repo["statuses_url"],
            "subscribers_url": repo["subscribers_url"],
            "subscription_url": repo["subscription_url"],
            "tags_url": repo["tags_url"],
            "teams_url": repo["teams_url"],
            "trees_url": repo["trees_url"],
            "clone_url": repo["clone_url"],
            "mirror_url": repo["mirror_url"],
            "hooks_url": repo["hooks_url"],
            "svn_url": repo["svn_url"],
            "homepage": repo["homepage"],
            "language": repo["language"],
            "forks_count": repo["forks_count"],
            "stargazers_count": repo["stargazers_count"],
            "watchers_count": repo["watchers_count"],
            "size": repo["size"],
            "default_branch": repo["default_branch"],
            "open_issues_count": repo["open_issues_count"],
            "is_template": repo["is_template"],
            "has_issues": repo["has_issues"],
            "has_projects": repo["has_projects"],
            "has_wiki": repo["has_wiki"],
            "has_pages": repo["has_pages"],
            "has_downloads": repo["has_downloads"],
            "has_discussions": repo["has_discussions"],
            "archived": repo["archived"],
            "disabled": repo["disabled"],
            "visibility": repo["visibility"],
            "pushed_at": repo["pushed_at"],
            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"],
            "permissions_admin": repo["permissions"]["admin"],
            "permissions_push": repo["permissions"]["push"],
            "permissions_pull": repo["permissions"]["pull"],
            "security_advanced_security_status": advanced_security_status,
            "security_secret_scanning_status": secret_scanning_status,
            "security_secret_scanning_push_protection_status": secret_scanning_push_protection_status
        }
        writer.writerow(repo_data)

print("Data has been written to", csv_file)
