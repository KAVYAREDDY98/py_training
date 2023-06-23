'''diff btw list(can be mutable/replace) and tuple''' 
'''list representation [] or list()'''
#list_1 = ["Hi", "Hello"]
##list_2 = list_1

##print(list_2)
#list_1.pop()
#print(list_1)
#list_1.remove('Hi')
#print(list_1)
#del list_1[0]
#print (list_1)

##list_1[0] = "Bye"  
#print(list_2)
#print(list_1)

'''Tuple is immutable''' 
'''tuple represenation () or tuple()'''

#tuple_1 = ("Hi", "Hello")
#tuple_2 = tuple_1
#print(tuple_2)

#tuple_1[0] = 'Bye'
#print(tuple_2)



'''Sets(membership test) (gives unique values, unordered, merges and returns unique values), Represenattion-{} or set()'''

'''
message = ["Hi", "Hello", "Bye", "Hello"]
print(message)

msg = {"Hi", "Hello", "Bye","Hello"}
print(msg)

msg_1 = {"Hi", "Hello", "Bye","Hello"}
msg_2 = {"Goodbye", "Bro", "Bye","Hello"}

print(msg_1.difference(msg_2))
print(msg_2.difference(msg_1))

print(msg_1.union(msg_2))
print(msg_2.union(msg_1))

'''
#emp_1= ['John', 'K' , '27', ['Python', 'Java']]
'''Dictionaries - {key:value} pair'''
'''
emp_1 = {'name':'John', 'age':'27', 'prog_lang': ['Python', 'Java']}

print(emp_1.items())
print(emp_1.keys())
print(emp_1.values())

print(emp_1['age'])
#print(emp_1['email']) #error
print(emp_1.get('name'))
print(emp_1.get('email','not found!'))


emp_1.update({'name':'kavya','email':'k@company'})
print(emp_1)

del emp_1['email']
print(emp_1)

emp_1.pop('age')
print(emp_1)

'''
emp_1 = {'name':'John', 'age':'27', 'prog_lang': ['Python', 'Java']}
'''
#keys
for i in emp_1:
	print(i)


#select keys
for i in emp_1.keys():
	print(i)

#select values
for i in emp_1.values():
	print(i)

#select keys or values
for k,v in emp_1.items():
	print(k)
	print(v)

#items both k and v
for i in emp_1.items():
	print(i)

#customize
for k in emp_1.items():
	print(f'This is keys: {k} - This is values: {v}')

'''

#Conditions
'''
==
!=
>
<
>=
<=

if False:
	print('it is true')
else:
	print('it is false')
'''
'''
prog_lang ='Java'
if prog_lang == 'Python':
	print("It is Python")
elif prog_lang == 'Scala': 
	print("It is Scala")
else:
	print('Not Match')
'''

'''
AND
OR
NOT
'''

lunch = 'ok'
homework = 'not ok'
if lunch and homework:
	print('You can play')
else:
	print('You cannot play')

if not homework:
	print('You can play')
else:
	print('You cannot play')