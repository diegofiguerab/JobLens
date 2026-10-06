import json

# Goal of this project version:
# Build a basic Python job tracker that can add, view, update and delete job applications.

'''
JOBLENS

1. Add application
2. View applications
3. Update applications
4. Delete application
5. Search applications
6. Exit

'''


job_1 = {
    "company": "Amazon",
    "position": "Software Engineer Intern",
    "status": "Applied",
    "url": ""
}

job_2 = {
    "company": "Google",
    "position": "Data Scientist Intern",
    "status": "Interested",
    "url": ""
}

job_3 = {
    "company": "Amazon",
    "position": "Machine Learning Engineer Intern",
    "status": "Interested",
    "url": ""
}

jobs = [job_1, job_2, job_3]

# 2. Functions

def view_jobs():
    print("\n~ JobLens Applications ~\n")
    print(f"{'#':<3}{'Company':<18}  {'Position':<41} {'Status':<15}")
    print("-" * 75)

    for number, job in enumerate(jobs, start=1):
        print(f"{number}. {job['company']:<18}  {job['position']:<40}  {job['status']:<15}")

    print("-" * 75)

def add_job():
    company = input("Enter the name of the company: ")
    position = input("Enter the position: ")
    status = input("Enter status of application: ")
    url = input("URL of the application website: ")

    new_job = {
        "company": company,
        "position": position,
        "status": status,
        "url": url
    }

    jobs.append(new_job)
    save_jobs()
    print(f"{new_job} added to list!")


def update_job():
    app_number = int(input("Enter the application number: "))
    job = jobs[app_number - 1]

    new_status = input("How's the application going so far?: ")

    job["status"] = new_status
    save_jobs()
    print("Done!")



def delete_job():
    ask = int(input("Which application do u want to delete?: "))
    job = jobs[ask - 1]

    jobs.remove(job)
    save_jobs()
    print("removed!")

def search_jobs():
    search = input("What do u want to search for?: ")

    for job in jobs:
        if search in job["company"]:
            print(f"\n{job['company']} - {job['position']} - {job['status']}")

def save_jobs():
    with open("jobs.json", "w") as file:
        json.dump(jobs, file)

def load_jobs():
    try:
        with open("jobs.json", "r") as file:
            jobs = json.load(file)
            return jobs
        
    except FileNotFoundError:
        return []

jobs = load_jobs()

if not jobs:
    jobs = [job_1, job_2, job_3]
    save_jobs()

# Menu

while True:
    print("""
~~~ JobLens ~~~
~ Bring your job hunt into focus ~

1. Add Application
2. View Applications
3. Update Application
4. Delete Application
5. Search Applications
6. Exit
""")
    
    choice = int(input("What would you like today?: "))

    if choice == 1:
        add_job()

    elif choice == 2:
        view_jobs()

    elif choice == 3:
        update_job()

    elif choice == 4:
        delete_job()

    elif choice == 5:
        search_jobs()
# Exit Choice
    elif choice == 6:
        break  

    else:
        print("Invalid Choice, Try Again")



