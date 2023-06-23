#my_list = [1,2,3,4]
#def square(my_list):
 #   lst = []
  #  for i in my_list:
   #     lst.append(i ** 2)
   # print (lst)

my_list=[1,2,3,4]
def my_func(my_list):
    lst = []
    for i in my_list:
        lst.append(i * i)
    return lst
print(my_func(my_list))