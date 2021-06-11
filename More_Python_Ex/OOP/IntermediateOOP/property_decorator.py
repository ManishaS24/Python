class Employee:
    amount_raise = 1.04

   
    def __init__(self, first_name, last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        # self.email = first_name + '.' + last_name + '@' + 'company.com'
    
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first_name, self.last_name)
    
    @property
    def fullname(self):
        return '{} {} '.format(self.first_name, self.last_name)
    
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split()
        self.first_name = first_name
        self.last_name = last_name
      
    @fullname.deleter
    def fullname(self):
        print('Name Deleted!')
        self.first_name = None
        self.last_name = None


emp_1 = Employee('Amit', 'Mishra', 76000)

# emp_1.first_name = 'Lucky'

emp_1.fullname = 'Priya Gooj'

print(emp_1.first_name)
print(emp_1.email)
# print(emp_1.fullname())
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)

