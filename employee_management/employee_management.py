# FILE: employee_management.py

class EmployeeManagement:
    """
    Employee Management System

    This module uses lists, sets, tuples, and dictionaries to manage employee data. 
    It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

    Data Structures:

    1. Lists: To store collections of employees and departments.
    2. Tuples: To store immutable employee details.
    3. Sets: To manage unique skills and departments.
    4. Dictionaries: To map employee IDs to their details and manage department assignments.
    """

    def __init__(self):
        # List of employees with details (ID, name, age, department, skills)
        self.employees = [
            (1, "Alice", 30, "HR", {"Recruitment", "Training"}),
            (2, "Bob", 25, "IT", {"Python", "Networking"}),
            (3, "Charlie", 28, "Finance", {"Accounting", "Excel"}),
            (4, "Diana", 35, "IT", {"Java", "Security"}),
            (5, "Eve", 40, "HR", {"Recruitment", "Employee Relations"})
        ]

        # List of departments
        self.departments = ["HR", "IT", "Finance", "Marketing"]

        # Set of unique skills
        self.skills = set()

        # Adding skills from employees
        for employee in self.employees:
            self.skills.update(employee[4])

        # Dictionary to map employee IDs to their details
        self.employee_catalog = {emp[0]: emp for emp in self.employees}

        # Dictionary to manage department assignments
        self.department_assignments = {dept: [] for dept in self.departments}

        # Assign employees to departments
        for employee in self.employees:
            self.department_assignments[employee[3]].append(employee[0])

    # List-Related Methods
    def find_employee_index(self, emp_id):
        """Finds the index of an employee in the list."""
        for index, employee in enumerate(self.employees):
            if employee[0] == emp_id:
                return index
        return -1

    def sort_employees_by_age(self):
        """Sorts employees by age."""
        return sorted(self.employees, key=lambda emp: emp[2])

    def reverse_departments(self):
        """Reverses the list of departments."""
        return self.departments[::-1]

    def append_department(self, department):
        """Appends a new department to the list."""
        if department not in self.departments:
            self.departments.append(department)
            self.department_assignments[department] = []
            print(f"Department '{department}' added.")
        else:
            print(f"Department '{department}' already exists.")

    def remove_department(self, department):
        """Removes a department from the list."""
        if department in self.departments:
            self.departments.remove(department)
            del self.department_assignments[department]
            print(f"Department '{department}' removed.")
        else:
            print(f"Department '{department}' not found.")

    # Tuple-Related Methods
    def find_max_min_age(self):
        """Finds the maximum and minimum age of employees."""
        ages = [emp[2] for emp in self.employees]
        return max(ages), min(ages)

    # Set-Related Methods
    def add_skill(self, skill):
        """Adds a new skill."""
        self.skills.add(skill)
        print(f"Skill '{skill}' added.")

    def remove_skill(self, skill):
        """Removes a skill."""
        self.skills.discard(skill)
        print(f"Skill '{skill}' removed.")

    def list_all_skills(self):
        """Lists all skills."""
        return self.skills

    def count_skill_occurrences(self, skill):
        """Counts the occurrences of a specific skill."""
        return sum(1 for emp in self.employees if skill in emp[4])

    def find_common_skills(self, other_skills):
        """Finds common skills between two sets."""
        return self.skills.intersection(other_skills)

    def find_unique_skills(self):
        """Finds unique skills in the company."""
        return self.skills.difference({"Python", "Java"})

    def clear_skills(self):
        """Clears all skills."""
        self.skills.clear()
        print("All skills cleared.")

    # Dictionary-Related Methods
    def add_employee(self, emp_id, name, age, department, skills_set):
        """Adds a new employee."""
        if emp_id not in self.employee_catalog:
            self.employee_catalog[emp_id] = (emp_id, name, age, department, skills_set)
            self.department_assignments[department].append(emp_id)
            self.skills.update(skills_set)
            print(f"Employee '{name}' added.")
        else:
            print(f"Employee ID '{emp_id}' already exists.")

    def remove_employee(self, emp_id):
        """Removes an employee."""
        if emp_id in self.employee_catalog:
            emp_details = self.employee_catalog.pop(emp_id)
            self.department_assignments[emp_details[3]].remove(emp_id)
            print(f"Employee '{emp_details[1]}' removed.")
        else:
            print(f"Employee ID '{emp_id}' not found.")

    def get_employee_details(self, emp_id):
        """Gets employee details."""
        return self.employee_catalog.get(emp_id, "Employee not found.")

    def list_employees_by_department(self, department):
        """Lists all employees in a department."""
        return [emp_id for emp_id in self.department_assignments.get(department, [])]

    def count_employees_by_department(self, department):
        """Counts employees in a department."""
        return len(self.department_assignments.get(department, []))

    def update_employee_details(self, emp_id, new_details):
        """Updates employee details."""
        if emp_id in self.employee_catalog:
            old_department = self.employee_catalog[emp_id][3]
            new_department = new_details[3]
            if old_department != new_department:
                self.department_assignments[old_department].remove(emp_id)
                self.department_assignments[new_department].append(emp_id)
            self.employee_catalog[emp_id] = new_details
            print(f"Updated details for employee ID '{emp_id}'.")
        else:
            print(f"Employee ID '{emp_id}' not found.")

    def merge_employee_catalogs(self, other_catalog):
        """Merges two employee catalogs."""
        for emp_id, details in other_catalog.items():
            if emp_id not in self.employee_catalog:
                self.employee_catalog[emp_id] = details
                self.department_assignments[details[3]].append(emp_id)
                self.skills.update(details[4])
        print("Employee catalogs merged.")

    def get_all_employee_ids(self):
        """Gets all employee IDs."""
        return list(self.employee_catalog.keys())

    def clear_employee_catalog(self):
        """Clears the employee catalog."""
        self.employee_catalog.clear()
        for dept in self.department_assignments:
            self.department_assignments[dept] = []
        print("Employee catalog cleared.")

# Example usage
if __name__ == "__main__":
    emp_mgmt = EmployeeManagement()

    print("Employee Catalog:")
    for emp_id, details in emp_mgmt.employee_catalog.items():
        print(f"{emp_id}: {details}")

    print("\nDepartments Available:")
    print(emp_mgmt.departments)

    print("\nSkills Available:")
    print(emp_mgmt.skills)

    print("\nDepartment Assignments:")
    for dept, emp_ids in emp_mgmt.department_assignments.items():
        print(f"{dept}: {emp_ids}")

    # Add and remove employees
    emp_mgmt.add_employee(6, "Frank", 29, "Marketing", {"SEO", "Content Writing"})
    emp_mgmt.remove_employee(3)

    print("\nEmployee Catalog After Changes:")
    for emp_id, details in emp_mgmt.employee_catalog.items():
        print(f"{emp_id}: {details}")

    # Get employee details
    print("\nEmployee Details for ID 2:")
    print(emp_mgmt.get_employee_details(2))

    # List employees by department
    print("\nEmployees in IT Department:")
    print(emp_mgmt.list_employees_by_department("IT"))

    # Count employees by department
    print("\nCount of Employees in HR Department:")
    print(emp_mgmt.count_employees_by_department("HR"))

    # Find employee index
    print("\nIndex of Employee ID 2:")
    print(emp_mgmt.find_employee_index(2))

    # Add and remove skills
    emp_mgmt.add_skill("Project Management")
    emp_mgmt.remove_skill("Networking")

    # List all skills
    print("\nAll Skills:")
    print(emp_mgmt.list_all_skills())

    # Sort employees by age
    print("\nEmployees Sorted by Age:")
    for emp in emp_mgmt.sort_employees_by_age():
        print(emp)

    # Reverse the list of departments
    print("\nReversed List of Departments:")
    print(emp_mgmt.reverse_departments())

    # Find the maximum and minimum age of employees
    max_age, min_age = emp_mgmt.find_max_min_age()
    print(f"\nMaximum Age: {max_age}, Minimum Age: {min_age}")

    # Count the occurrences of a specific skill
    print(f"\nOccurrences of 'Python': {emp_mgmt.count_skill_occurrences('Python')}")

    # Find common skills between two sets
    other_skills = {"Python", "SEO", "Data Analysis"}
    print(f"\nCommon Skills: {emp_mgmt.find_common_skills(other_skills)}")

    # Find unique skills in the company
    print(f"\nUnique Skills: {emp_mgmt.find_unique_skills()}")

    # Update employee details
    emp_mgmt.update_employee_details(2, (2, "Bob", 26, "Finance", {"Python", "Accounting"}))
    print(f"\nUpdated Employee Details for ID 2: {emp_mgmt.get_employee_details(2)}")

    # Merge two employee catalogs
    other_catalog = {
        7: (7, "Grace", 32, "IT", {"Python", "Machine Learning"}),
        8: (8, "Hank", 45, "HR", {"Recruitment", "Training"})
    }
    emp_mgmt.merge_employee_catalogs(other_catalog)
    print("\nMerged Employee Catalog:")
    for emp_id, details in emp_mgmt.employee_catalog.items():
        print(f"{emp_id}: {details}")

    # Append a new department to the list
    emp_mgmt.append_department("Legal")
    print("\nUpdated List of Departments:")
    print(emp_mgmt.departments)

    # Remove a department from the list
    emp_mgmt.remove_department("Marketing")
    print("\nUpdated List of Departments After Removal:")
    print(emp_mgmt.departments)

    # Clear all skills
    emp_mgmt.clear_skills()
    print("\nSkills After Clearing:")
    print(emp_mgmt.skills)

    # Get all employee IDs
    print("\nAll Employee IDs:")
    print(emp_mgmt.get_all_employee_ids())

    # Clear the employee catalog
    emp_mgmt.clear_employee_catalog()
    print("\nEmployee Catalog After Clearing:")
    print(emp_mgmt.employee_catalog)