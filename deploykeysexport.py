# Declaring the import packages
import requests
import csv

#Declaring variables


url_2 = "https://git.viriciti.com/api/v4/projects/{Projet_id}/deploy_keys"

TOKEN = "glpat-nJX9i3StVsZY7nFnX5sg"

CSV_FILE ="MY.csv"

Project_id=[ 89,146,192,263,267,270 ]

with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
    CSVWRITE =  csv.writer(file)
    CSVWRITE.writerow(["project_id","path","path_with_namespace","namespace_kind","id","title","key","finger_print","fingerprint_sha256","created_at","expires_at"])


page=1
while True:
    for project_id in Project_id:
      print(f"Getting deploy keys for project {project_id}...")
      response = requests.get(f"https://git.viriciti.com/api/v4/projects/{project_id}?statistics=true",
                            headers={"PRIVATE-TOKEN": TOKEN})
      print(f"{response}")

    if response.status_code != 200:
        print(f"Failed to get deploy keys for project {Project_id}.")
        break
    
    for project_id in Project_id:
      print(f"Getting deploy keys for project {project_id}...")
    response2 = requests.get(f"{url_2}",
                            headers={"PRIVATE-TOKEN": TOKEN})
    print(f"{response2}")
  #check if the request was empty


    deploykeys=response.json()&response2.json()
    print(f"{deploykeys}")
    for deploy in deploykeys:
        
        CSVWRITE.writerow([deploy.get(key, "") for key in ["project_id","path","path_with_namespace","namespace_kind","id","title","key","finger_print","fingerprint_sha256","created_at","expires_at"]])
      


 
        



    






