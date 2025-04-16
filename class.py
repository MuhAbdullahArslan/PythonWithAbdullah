# Task Title: Employee Management System with Attendance & Payroll

from datetime import datetime

class Person:

    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
    
    def get_age(self):
        dob = datetime.strptime(self.dob,"%Y-%m-%d")

        today = datetime.today()
        age = today.year - dob.year

         
        return age 
    
class Employee(Person):
    def __init__(self,name,dob,employee_id,department,salary):
        super().__init__(name,dob)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
    
    def __str__(self):
        return f"""
    -:Employee Information:-
    
    name = {self.name}
    age = {super().get_age()}
    DOB(Date_of_Birth) = {self.dob}
    Id = {self.employee_id}
    Department = {self.department}
    """

# 3. Class: Attendance

# Method: mark_attendance(date) – accepts a date (datetime.date) and stores it in a list.

# Method: get_attendance_count() – returns total attendance days using len().
class Attendance:
    
    def __init__(self):
        self.attendance_date = []
    
    def mark_attendance(self,date: datetime.date):
        
        if date not in self.attendance_date:
            self.attendance_date.append(date)
        
    def get_attendance_count(self):
        return len(self.attendance_date)
            
# 4. Class: Payroll

# Method: calculate_pay() – calculates pay based on attendance (assume 1000 per day attended).
            
class Payroll(Attendance):
    def calculate_pay(self):
        payroll_based_on_atte = self.get_attendance_count() * 1000
        return payroll_based_on_atte

# 5. Final Class: HRSystem (inherits from Employee, Attendance, and Payroll)
class HRSystem(Employee,Payroll):
    
# Method: generate_report() – prints:
    def generate_report(self):
        print(f"""
              Employee name : {self.name}
              Age : {self.get_age()}
              Department : {self.department}
              Total attendance : {self.get_attendance_count()}
              Final Salary : {self.calculate_pay()}""")


em1 = HRSystem("Abdullah","2004-09-16",21406,"Electrical ",45000)
em1.attendance_date('2024-09-16')

print(em1)