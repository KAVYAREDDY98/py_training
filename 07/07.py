#decorators<--  closures<-- first class functions

#def square(x):
#	return(x*x)
#print(square(4))

#result = square(4)
#print(result)

#result= square
#print(result.__name__)
#print(return(4))


#def outer_func(message):
#	message = 'Hi'

#	def inner_func():
#		print(message)

#	return inner_func

#hi_func = outer_func('Hi')
#hi_func()

#hello_func = outer_func('Hello')
#hello_func()

#[1,2,3,4] -->>> [1,4,9,16]

#def square(i):
#	return i*i

#def cube(i):
#	return i*i*i


#my_list=[1,2,3,4]
#your_list= [3,6,8,1]

#def my_func(args,func):
#	result = []
#	for i in args:
#		result.append(func(i))

#	return result

#print(my_func(my_list,square))
#print(my_func(your_list,square))

#print(my_func(my_list,cube))
#print(my_func(your_list,cube))

def dec_func(orig_func):
	def wrapper_func():
		return orig_func()
	return wrapper_func

def disp_func():
	print('This is a display function')

dec_disp = dec_func(disp_func)
dec_disp()

def Bye_func():
	print('This is a Bye function')
	print('Hello everyone!')

def Hello_func():
	print('This is a Hello function')
	print('Hello everyone!')

disp_func()
Bye_func()
Hello_func()