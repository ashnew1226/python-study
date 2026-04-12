class Employee:
    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Getter methods
    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_salary(self, salary):
        self.salary = salary

    # Instance method
    def display_details(self):
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary}")

e differently – use the add() method on the field to add a record to the relation. This example adds the Author inst
# Main execution
if __name__ == "__main__":
    emp = Employee("Geek", 10000.0)
    emp.display_details()

    
