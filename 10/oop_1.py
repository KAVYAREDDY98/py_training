#class, methods,class varialbles, instance variable = attributes being stored and used in init method)

class Employee():

	raise_amt = 1.05
	num_emps = 0
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay
		
		Employee.num_emps += 1

	def fullname(self):
		return(f'{self.first} {self.last}')	

	def apply_raise(self):
		self.pay = int(int(self.pay) * self.raise_amt)

	def total_emps(self):
		ret

emp_1 = Employee('John', 'K', 50000)
emp_2 = Employee('Jane', 'M', 60000)
#print(emp_1.first)
#print(emp_2.email)

#print(emp_1.fullname())
#print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.raise_amt)
print(Employee.raise_amt)