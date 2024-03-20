# project.py

import os

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    @staticmethod
    def load_projects(file_name):
        projects = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                next(file)  # skip header
                for line in file:
                    data = line.strip().split('\t')
                    name, start_date, priority, cost_estimate, completion_percentage = data
                    project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                    projects.append(project)
        return projects

    @staticmethod
    def save_projects(file_name, projects):
        with open(file_name, 'w') as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

    @staticmethod
    def display_projects(projects):
        incomplete_projects = [project for project in projects if project.completion_percentage < 100]
        completed_projects = [project for project in projects if project.completion_percentage == 100]

        incomplete_projects.sort(key=lambda x: x.priority)
        completed_projects.sort(key=lambda x: x.priority)

        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"  {project}")

        print("Completed projects:")
        for project in completed_projects:
            print(f"  {project}")

    @staticmethod
    def filter_projects_by_date(projects, date):
        filtered_projects = [project for project in projects if project.start_date > date]
        filtered_projects.sort(key=lambda x: x.start_date)
        Project.display_projects(filtered_projects)

    @staticmethod
    def add_new_project(projects):
        print("Let's add a new project")
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yy): ")
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))
        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)

    @staticmethod
    def update_project(projects):
        print("Select a project to update:")
        for index, project in enumerate(projects):
            print(f"{index} {project}")

        choice = int(input("Project choice: "))
        project = projects[choice]

        new_completion_percentage = input(f"New Percentage: ")
        if new_completion_percentage:
            project.completion_percentage = int(new_completion_percentage)

        new_priority = input(f"New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
