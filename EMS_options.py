from Employee_Class import Employee
from datetime import datetime
import csv

employees_list = []

# Read or find any employee:
def read_employees():
    option = input("""Select option:
    1: See all employees
    2: Find employees by ID
    3: Find employees by department""")
    match option:
        case "1":
            for employee in employees_list: print(employee)
        case "2":
            emp_id = input("Enter employee id: ")
            for employee in employees_list:
                if str(employee.emp_id) == emp_id:
                    print(employee)
                    break
                else:print(f"No employee with id {emp_id} found.")
        case "3":
            department = input("Enter Department")
            dept = [str(employee) for employee in employees_list if employee.department == department]
            
            for employee in dept:
                print(employee)
        case _: print("Not a valid input")




# Add new employees to the Employees list:
def add_employees():
    try:
        # Input Employee name
        name = input("Enter the employee name in the format 'first, last': ")
        
        #Splitting
        first, last = name.split(", ")
        
        # Capitalizing
        first_name = first.capitalize()
        last_name = last.capitalize()
    except ValueError:
        print("you did not include a ',' ")

    while True:
        try:
            # Input Employee salary
            salary = int(input("Enter employee salary: "))
        except ValueError:
            print("Salary must be an integer")
        else: break
    
    while True: 
        try: 
            # Input the hiring date
            doe_string = input("enter the date of employment (day/month/year): ")
            date_hired = datetime.strptime(doe_string, "%d/%m/%Y")
        except ValueError:
            print("Date must be in the format day/month/full year (00/00/0000)")
        else: break
    
    while True:
        try:
            #Input Department
            department = input("Enter department name: ")
        except TypeError:
            print("You entered a non-numberical value.")
        else: break
    employee = Employee(first_name, last_name, salary, date_hired, department)
    employees_list.append(employee)





# Update the department element of the Employees list
def update_employees():
    emp_id = input("Enter employee id: ")
    for e in employees_list:
        if e.emp_id == emp_id:
            employees_list == e
            break
        else:
            print("Employee not found")
            return
    try:
        # Input Employee name
        name = input("Enter the employee name in the format 'first, last': ")
        
        #Splitting
        first, last = name.split(", ")
        
        # Capitalizing
        first_name = first.capitalize()
        last_name = last.capitalize()
    except ValueError:
        print("you did not include a ',' ")
    
    while True:
        try:
            # Input Employee salary
            salary = int(input("Enter employee salary: "))
        except ValueError:
            print("Salary must be an integer")
        else: break
    
    while True: 
        try: 
            doe_string = input("enter the date of employment (day/month/year): ")
            date_hired = datetime.strptime(doe_string, "%d/%m/%Y")
        except ValueError:
            print("Date must be in the format day/month/full year (00/00/0000)")
        else: break
        try:
            department = input("Enter department name: ")
        except:
            print("You entered a non numberical character")
    
    employees_list.first_name = first_name
    employees_list.last_name = last_name
    employees_list.salary = salary
    employees_list.date_hired = date_hired
    employees_list.department = department





# Delete employees from the list
def remove_employees():
    emp_id = input("Enter employee id: ")
    employees = [employee for employee in employees if employee.emp_id != emp_id]





# Option panel:
if __name__ == "__main__":
    while True:
        print("""Welcome to the Employee Management System! Please enter an option: 
        1: See Employees
        2: Add Employees
        3: Update an Employee
        4: Remove an Employee
        5: exit""")

        option = input("option: ")

        match option:
            case "1": read_employees()
            case "2": add_employees()
            case "3": update_employees()
            case "4": remove_employees()
            case "5": 
                with open("employee.csv",'wr') as file:
                    csvreader = csv.reader(file)
                    for Employee in csvreader:
                        Employee.append(add_employees)
                break
            case _: print("Not a valid input.")


    