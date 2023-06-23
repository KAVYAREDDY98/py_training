class Employee():

	raise_amt = 1.05

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay
		
	def fullname(self):
		return(f'{self.first} {self.last}')	

	def apply_raise(self):
		self.pay = int(int(self.pay) * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amt):
		cls.raise_amt = amt

	def from_str(cls, emp_str):
		first, last, pay = emp_1_str.split('-')	
		return cls(first, last, pay)

emp_1 = Employee('John', 'K', 50000)
emp_2 = Employee('Jane', 'M', 60000)

Employee.set_raise_amt(1.09)
print(emp_1.raise_amt)

emp_1_str = 'John-K-50000'


new_emp_1 = Employee.from_str(emp_1_str)


