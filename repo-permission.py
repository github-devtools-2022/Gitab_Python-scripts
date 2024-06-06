import requests
import csv

# Variable of Token
TOKEN = "glpat-Zp-xYYawdziVYmAuCyDC"

# csv file path
CSV_FILE = "HTB-project_0521.csv"

# URL for GitLab API
BASE_URL = "https://gitlab.intern.has-to-be.com/api/v4/projects"

# Declare the project ids in a list
project_ids = ('431', '430', '428', '427', '426', '425', '424', '422', '421', '414', '413', '411', '409', '408', '407', '406', '405', '404', '403', '402', '401', '400', '399', '398', '397', '395', '390', '389', '388', '387', '386', '385', '384', '383', '382', '381', '379', '378', '377', '376', '375', '374', '373', '372', '371', '370', '369', '368', '367', '366', '365', '364', '363', '362', '359', '358', '357', '356', '353', '352', '351', '349', '348', '347', '346', '345', '344', '343', '340', '339', '338', '337', '336', '335', '334', '333', '332', '331', '330', '329', '328', '327', '326', '325', '322', '321', '320', '319', '318', '317', '316', '315', '314', '313', '312', '311', '310', '309', '308', '307', '306', '305', '304', '302', '301', '300', '299', '298', '297', '296', '295', '294', '293', '292', '291', '290', '289', '288', '287', '286', '285', '284', '282', '281', '280', '279', '278', '277', '276', '275', '274', '272', '271', '270', '269', '268', '266', '265', '264', '263', '261', '260', '259', '257', '256', '255', '254', '253', '251', '250', '249', '248', '246', '245', '244', '243', '241', '240', '239', '238', '237', '236', '235', '234', '233', '232', '230', '229', '223', '222', '220', '219', '218', '217', '215', '214', '213', '212', '211', '210', '207', '206', '205', '204', '203', '202', '201', '200', '199', '198', '197', '196', '195', '194', '193', '192', '191', '190', '189', '188', '187', '186', '185', '184', '183', '182', '181', '180', '179', '178', '177', '176', '175', '174', '173', '171', '170', '169', '168', '167', '166', '164', '163', '162', '160', '159', '158', '157', '156', '155', '154', '153', '152', '151', '150', '149', '148', '147', '146', '144', '143', '142', '141', '140', '139', '138', '136', '135', '134', '132', '131', '130', '129', '128', '127', '126', '125', '123', '122', '121', '119', '118', '117', '116', '115', '114', '113', '110', '109', '108', '107', '104', '103', '102', '100', '99', '98', '97', '96', '93', '91', '90', '89', '85', '84', '83', '82', '80', '79', '77', '76', '75', '74', '73', '71', '70', '69', '68', '67', '66', '64', '63', '62', '61', '60', '59', '58', '57', '56', '55', '54', '53', '52', '51', '50', '49', '48', '47', '46', '45', '44', '42', '41', '40', '39', '38', '37', '36', '35', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '2', '1' )


# Write headers to the CSV file
with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["project_id", "description", "name", "name_with_namespace", "Project_name", "Project_Fullpath",
                         "created_at", "default_branch", "ssh_url_to_repo", "http_url_to_repo", "web_url",
                         "readme_url", "forks_count", "avatar_url", "star_count", "last_activity_at",
                         "namespace_id", "namespace_name", "namespace_path", "namespace_kind", "namespace_full_path",
                         "namespace_parent_id", "namespace_avatar_url", "namespace_web_url", "repository_storage",
                         "container_registry_image_prefix", "links_self", "links_issues", "links_merge_requests",
                         "links_repo_branches", "links_labels", "links_events", "links_members",
                         "_links_cluster_agents", "code_suggestions", "packages_enabled", "empty_repo", "archived",
                         "visibility", "resolve_outdated_diff_discussions", "issues_enabled", "merge_requests_enabled",
                         "wiki_enabled", "jobs_enabled", "snippets_enabled", "container_registry_enabled",
                         "service_desk_enabled", "can_create_merge_request_in", "issues_access_level",
                         "repository_access_level", "merge_requests_access_level", "forking_access_level",
                         "wiki_access_level", "builds_access_level", "snippets_access_level", "pages_access_level",
                         "analytics_access_level", "container_registry_access_level",
                         "security_and_compliance_access_level", "releases_access_level", "environments_access_level",
                         "feature_flags_access_level", "infrastructure_access_level", "monitor_access_level",
                         "model_experiments_access_level", "model_registry_access_level", "emails_disabled",
                         "emails_enabled", "shared_runners_enabled", "lfs_enabled", "creator_id", "import_url",
                         "import_type", "import_status", "open_issues_count", "description_html", "updated_at",
                         "ci_default_git_depth", "ci_forward_deployment_enabled", "ci_forward_deployment_rollback_allowed",
                         "ci_job_token_scope_enabled", "ci_separated_caches",
                         "ci_allow_fork_pipelines_to_run_in_parent_project", "build_git_strategy",
                         "keep_latest_artifact", "restrict_user_defined_variables", "runners_token",
                         "runner_token_expiration_interval", "group_runners_enabled", "auto_cancel_pending_pipelines",
                         "build_timeout", "auto_devops_enabled", "auto_devops_deploy_strategy", "ci_config_path",
                         "public_jobs", "only_allow_merge_if_pipeline_succeeds", "allow_merge_on_skipped_pipeline",
                         "request_access_enabled", "only_allow_merge_if_all_discussions_are_resolved",
                         "remove_source_branch_after_merge", "printing_merge_request_link_enabled", "merge_method",
                         "squash_option", "enforce_auth_checks_on_uploads", "suggestion_commit_message",
                         "merge_commit_template", "squash_commit_template", "issue_branch_template",
                         "statistics_commit_count", "statistics_storage_size", "statistics_repository_size",
                         "statistics_wiki_size", "statistics_lfs_objects_size", "statistics_job_artifacts_size",
                         "statistics_pipeline_artifacts_size", "statistics_packages_size", "statistics_snippets_size",
                         "statistics_uploads_size", "autoclose_referenced_issues", "permissions_project_access",
                         "permissions_group_access"])

    # Loop through the project ids
    for project_id in project_ids:
        # Run the API call
        response = requests.get(f"{BASE_URL}/{project_id}?statistics=true",
                                headers={"PRIVATE-TOKEN": TOKEN})

        # Check if the request was successful
        if response.status_code == 200:
            project_info = response.json()

            # Check if 'issues' key exists in '_links' dictionary
            if "issues" in project_info["_links"]:
                issues_link = project_info["_links"]["issues"]
            else:
                issues_link = None

            # Write data to the CSV file
            csv_writer.writerow([
                project_info["id"], project_info["description"], project_info["name"],
                project_info["name_with_namespace"], project_info["path"], project_info["path_with_namespace"],
                project_info["created_at"], project_info.get("default_branch", ""), project_info["ssh_url_to_repo"],
                project_info["http_url_to_repo"], project_info["web_url"], project_info.get("readme_url", ""),
                project_info.get("forks_count", ""), project_info["avatar_url"], project_info["star_count"],
                project_info["last_activity_at"], project_info["namespace"]["id"], project_info["namespace"]["name"],
                project_info["namespace"]["path"], project_info["namespace"]["kind"],
                project_info["namespace"]["full_path"], project_info["namespace"]["parent_id"],
                project_info["namespace"]["avatar_url"], project_info["namespace"]["web_url"],
                project_info["repository_storage"], project_info["container_registry_image_prefix"],
                project_info["_links"]["self"], issues_link, project_info["_links"].get("merge_requests", ""),
                project_info["_links"]["repo_branches"], project_info["_links"]["labels"],
                project_info["_links"]["events"], project_info["_links"]["members"],
                project_info["_links"]["cluster_agents"], project_info.get("code_suggestions", ""),
                project_info["packages_enabled"], project_info["empty_repo"], project_info["archived"],
                project_info["visibility"], project_info["resolve_outdated_diff_discussions"],
                project_info["issues_enabled"], project_info["merge_requests_enabled"],
                project_info["wiki_enabled"], project_info["jobs_enabled"], project_info["snippets_enabled"],
                project_info["container_registry_enabled"], project_info["service_desk_enabled"],
                project_info["can_create_merge_request_in"], project_info["issues_access_level"],
                project_info["repository_access_level"], project_info["merge_requests_access_level"],
                project_info["forking_access_level"], project_info["wiki_access_level"],
                project_info["builds_access_level"], project_info["snippets_access_level"],
                project_info["pages_access_level"], project_info["analytics_access_level"],
                project_info["container_registry_access_level"],
                project_info["security_and_compliance_access_level"], project_info["releases_access_level"],
                project_info["environments_access_level"], project_info["feature_flags_access_level"],
                project_info["infrastructure_access_level"], project_info["monitor_access_level"],
                project_info["model_experiments_access_level"], project_info["model_registry_access_level"],
                project_info["emails_disabled"], project_info["emails_enabled"],
                project_info["shared_runners_enabled"], project_info["lfs_enabled"], project_info["creator_id"],
                project_info["import_url"], project_info["import_type"], project_info["import_status"],
                project_info.get("open_issues_count", ""), project_info["description_html"], project_info["updated_at"],
                project_info["ci_default_git_depth"], project_info["ci_forward_deployment_enabled"],
                project_info["ci_forward_deployment_rollback_allowed"], project_info["ci_job_token_scope_enabled"],
                project_info["ci_separated_caches"],
                project_info["ci_allow_fork_pipelines_to_run_in_parent_project"],
                project_info["build_git_strategy"], project_info["keep_latest_artifact"],
                project_info["restrict_user_defined_variables"], project_info["runners_token"],
                project_info["runner_token_expiration_interval"], project_info["group_runners_enabled"],
                project_info["auto_cancel_pending_pipelines"], project_info["build_timeout"],
                project_info["auto_devops_enabled"], project_info["auto_devops_deploy_strategy"],
                project_info.get("ci_config_path", ""), project_info["public_jobs"],
                project_info["only_allow_merge_if_pipeline_succeeds"],
                project_info["allow_merge_on_skipped_pipeline"], project_info["request_access_enabled"],
                project_info["only_allow_merge_if_all_discussions_are_resolved"],
                project_info["remove_source_branch_after_merge"],
                project_info["printing_merge_request_link_enabled"], project_info["merge_method"],
                project_info["squash_option"], project_info["enforce_auth_checks_on_uploads"],
                project_info["suggestion_commit_message"], project_info["merge_commit_template"],
                project_info["squash_commit_template"], project_info["issue_branch_template"],
                project_info["statistics"]["commit_count"], project_info["statistics"]["storage_size"],
                project_info["statistics"]["repository_size"], project_info["statistics"]["wiki_size"],
                project_info["statistics"]["lfs_objects_size"], project_info["statistics"]["job_artifacts_size"],
                project_info["statistics"]["pipeline_artifacts_size"], project_info["statistics"]["packages_size"],
                project_info["statistics"]["snippets_size"], project_info["statistics"]["uploads_size"],
                project_info["autoclose_referenced_issues"], project_info["permissions"]["project_access"],
                project_info["permissions"]["group_access"]
            ])
        else:
            print(f"Error in the API call of id {project_id}")

print("CSV file has been created successfully.")
