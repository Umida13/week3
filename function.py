'''''
Function - это блок кода который принимает аргументы и возвращает результат
a = 5
b = 6
c  = a+b 
Функция придерживается принципа DRY
def - это ключевое слово для обьявления функцию
'''

# def func1():   #  обьявления функции
#     print("hi i func1")  #тело функции
# func1()         # вызов функции



# def func(num1, num2):     #параметры функции 
#     print(num1, num2) 
# func("test", 5)     #5, 5 = аргументы функции (параметры бывают позиционные так и именлванные)



# def func(word1, word2):
#     print(word1, word2)
# func("string",1.0)
# # передача именновах аргументов

# def sum_first:
#     print(6+11
#     sum_first)



# def sum_objects(num1m, num2):
#     print((num1 num2)* num3)
# sum_objects(10, 20)
# sum_objects(20,50)
# sum_objects(1, 5)






# def func(word):
#   print(word.upper())
#   return word.upper()

# func("Aitemir")

# names = ["daria"], ["aibike", "adilet", "erbol"]
# def ccapitalize_name(iterable_object):
#     new_names = list()
#     for name in iterable_object:
#         new_names.append(name.capitalize())
#         return new_names
#         print(capitali_ename.capitalize())
   

# def func(num1, num2, *args):
#     print(num1, num2)
#     print("args: ", args)
#     print(args[0])
#     print(args[1])
#     for i in args:
#         print(i)
# func(5, 5, 1, "test")






# def sum_iterable(*args):
#     print(args)
#     return sum(args)

# result = sum_iterable(1, 2, 3, 4, 5, 6, 7, 8)
# print(result)




# def func(name, age, **kwargs):
#     print(name, age)
#     print(kwargs)

# func(name="Python", age=19, room=9)




# def func(name, age, **kwargs):
#     print(name, age)
#     print(kwargs)
#     print(kwargs["room"])    # kwargs.get(room)

# func(name="Python", age=19, room=9)




# ages = [12, 34, 34, 1, -3, 21]

# def check_age(ages):
#     for age in ages:
#         if age > 18:
#             print(age)

# check_age(ages)



# ages = [12, 34, 34, 1, -3, 21]

# def check_age(ages, *args, **kwargs):
#     for age in ages:
#         if age > 18:
#             print(age)
#             print(args[0]) + kwargs["world"]

# check_age(ages, "hello", world="world")






# students = 0: {
#     "name": "Aitemir",
#     "age": 30,
#     "adress": "test",
#     "phone": "+996700010205"
# },
# 1: {
#     "name": "Kalya",
#     "age": 25,
#     "adress": "test",
#     "phone": "+996500110205"
# }


# def info(*args, **kwargs):
#     print(args)
#     print(kwargs.get("students"))
# info(students=students)







# students = 0: {
#     "name": "Aitemir",
#     "age": 30,
#     "adress": "test",
#     "phone": "+996700010205"
# },
# 1: {
#     "name": "Kalya",
#     "age": 25,
#     "adress": "test",
#     "phone": "+996500110205"
# }


# def info(*args, **kwargs):
#     students = kwargs.get("students")
#     for k, v in students.items():
#         for k1, v1 in v.items



# def is_email(email: str) -> bool:
#     if email.endswith("@gmail.com"):
#         return True
#     return False


# email_list = ["atemir@mail.ru", "almaz@gmail.com", "isa@yandex.ru"]

# email_list_gmail = list()

# for email in email_list:
#     if is_email(email):
#         email_list_gmail.append(email)
#     print(email_list_gmail)




# def check_bad_wors(words):

# lists_bad_words = ["war", "fuck", "fight", "fire", "gun", "drugs"]

# user1 = input("enter words: ").split()
# try:
#     for word in user1:
#         if word in lists_bad_words:
#             raise ValueError(" You are blocked!")
# except ValueError as error:
#     print(error)
     

# print("good")



# def check_bad_wors(words):

#     lists_bad_words = ["war", "fuck", "fight", "fire", "gun", "drugs"]

# user1 = input("enter words: ").split()
# for word in user1:
#         if word in lists_bad_words:
#             raise ValueError(" You are blocked!")


# user1=input("enter word: ").split()
# try:
#     check_bad_wors(user1)
# except ValueError as error:
#     print(error)

# user2=input("enter word: ").split()
# try:
#     check_bad_wors(user2)
# except ValueError as error:
#     print(error)

     







# TASK

# dict_ = {1: "5", 2: "9", 3: "test"}
# def dictionary(dict_):
#     for k, v in dict_.items():
#         print(dict_[k])
# dictionary(dict_)




# num = 6
# def check(num):
#     if num % 2 == 0:
#         print("It is even number")
#     else:
#         print("It is odd number")
# check(num)
  





# def func(arg1, arg2 = '1'):
#     print(arg1, arg2)
# func(arg2 = '1', arg1 = '2')


# def func(a = 5, b = 6, **args):
#     print(arg)
# func(a = 1, b = 2, c = 3)


#TASKS


# Создайте функцию sum_digits()
# которая принимает целое число и возвращает 
# сумму всех его цифр.

# Пример:
# print(sum_digits(105)) 
# Вывод:
# 6 

# def  sum_digits(num):
#     result = 0
#     for i in str(num):
#         result += int(i)
#     return result
# print(sum_digits(105))

# def  sum_digits(a):
#     first = a // 100
#     second = a // 10 / 10
#     third = a // 10
#     return first + second + third
# print(sum_digits(105))





# def multiply(a, b):
#     return a * b

# print(multiply(5, 6)) 




import numbers
import types


# def get_type(a, b):
#     get_type = types
#     print(types.split(a, b))
#     return type(a)
#     return type(b)

# print(get_type(5, 's'))

# def divide(a, b):
#     return a // b
# print(divide(5, 10)) 



