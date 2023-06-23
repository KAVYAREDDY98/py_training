# 2 functs with return
'''
def hello_func():
	return 'Hello'

def hi_func():
	return("Hi world!")

print(hello_func())
print(hi_func())
'''
#functions with aurguments
'''
def emp_info(*args, **kwargs):
	
	print(args)
	print(kwargs)

emp_info('python', 'Java', car = '2020', make = 'ford')
'''
'''
prog_lang = ['python', 'Java', 'Scala']

for i in prog_lang:
	if i =='Java':
		print(i)
		break
	print(i)
'''
'''# approach to define function

list_1 = ['Python', 'Java', 'Scala']

def find_index(where,which):
	for i,v in enumerate(where):
		if v == which:
			print(i,v)
			#print(f"The index of {v} is {i}")
find_index(list_1, 'Scala')
'''
'''

#function is defined in other file
#importing every function
#import module as mo


list_1 = ['Python', 'Java', 'Scala']

module.find_index(list_1, 'Scala')
print(module.message)

#for importing specific function
# from module import find_index , message

list_1 = ['Python', 'Java', 'Scala']

find_index(list_1, 'Scala')
print(message)

#for importinf all but for accessing no need to specify

find_index(list_1, 'Scala')
print(message)

'''

#import packages

import calendar
#print(calendar.__file__)

print(dir(calendar))
print(help(calendar.isleap))