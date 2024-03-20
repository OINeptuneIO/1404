# project_management.py

from project import Project

def main():
    print("Welcome to Pythonic Project Management")
    file_name = "projects.txt"
    projects = Project.load_projects(file_name)
    print(f"Loaded {len(projects)} projects from {file_name}")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            file_name = input("Enter file name to load projects from: ")
            projects = Project.load_projects(file_name)
            print(f"Loaded {len(projects)} projects from {file_name}")
        elif choice == 's':
            file_name = input("Enter file name to save projects to: ")
            Project.save_projects(file_name, projects)
            print(f"Projects saved to {file_name}")
        elif choice == 'd':
            Project.display_projects(projects)
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yy): ")
            Project.filter_projects_by_date(projects, date)
        elif choice == 'a':
            Project.add_new_project(projects)
        elif choice == 'u':
            Project.update_project(projects)
        elif choice == 'q':
            save_option = input("Would you like to save to projects.txt? ").lower()
            if save_option.startswith('y'):
                Project.save_projects(file_name, projects)
                print("Changes saved.")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
