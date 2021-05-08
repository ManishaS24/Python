class Employee:
    
    def __init__(self, first_name, last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@' + 'company.com'
    

    
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee('Manisha', 'Sinha', 60000)

import datetime
my_date = datetime.date(2021, 6, 8)

#print(Employee.__dict__)

print(Employee.is_weekday(my_date))

