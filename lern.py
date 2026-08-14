class Project:
    def __init__(self, client_name, project_type, price, is_completed):
        self.client_name = client_name
        self.project_type = project_type
        self.price = price
        self.is_completed = is_completed

    def get_size_category(self):
        if self.price < 50:
            return "Small"
        elif self.price < 200:
            return "Medium"
        else:
            return "Large"

    def get_status(self):
        if self.is_completed:
            return "Completed"
        else:
            return "In Progress"


def save_project(project):
    with open("projects.txt", "a") as file:
        file.write(f"{project.client_name},{project.project_type},{project.price},{project.is_completed}\n")


def load_projects():
    projects = []
    with open("projects.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            client_name = parts[0]
            project_type = parts[1]
            price = float(parts[2])
            is_completed = parts[3] == "True"
            project = Project(client_name, project_type, price, is_completed)
            projects.append(project)
    return projects


while True:
    print("\n--- Design Projects Tracker ---")
    print("1. Add new project")
    print("2. View all projects")
    print("3. View in-progress projects only")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        client_name = input("Enter client name: ")
        project_type = input("Enter project type: ")

        try:
            price = float(input("Enter project price: "))
        except ValueError:
            print("Invalid input.")
            continue

        completed_answer = input("Is the project completed? (y/n): ")
        is_completed = completed_answer.lower() == 'y'

        new_project = Project(client_name, project_type, price, is_completed)
        save_project(new_project)
        print("Project added successfully!")

    elif choice == "2":
        all_projects = load_projects()
        print("\n--- All Projects ---")
        for project in all_projects:
            print(f"{project.client_name} - {project.project_type} - {project.get_size_category()} - {project.get_status()}")

    elif choice == "3":
        all_projects = load_projects()
        in_progress = [p for p in all_projects if not p.is_completed]
        print("\n--- In Progress Projects ---")
        for project in in_progress:
            print(f"{project.client_name} - {project.project_type} - {project.get_size_category()}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")