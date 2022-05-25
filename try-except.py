''' try-except - это обработка исключений
ошибки - SyntaxError IdentationError TabError
'''
# exceptions: 
'''
ZeroDivisionError
NameError
TypeError
KeyError
ImportError
ValueError
IndexError

'''
# ValueError -> BaseExeption прородитель всех исключкний

# try:
#     a: int = int(input("enter: "))
#     print(a)
# except:
#     print("some error!")


# if 2 > 5:
#     print('test')
# else:
#     print('tests')

# try:
#     a = int(input("enter a: "))
#     b = int(input("enter b: "))
#     print(a/b)
# # except Exception as name:
# #     print(name)
# except:
#     import sys 
#     print(f'error {sys.exc_info()[0]}')


# try:
#     a = int(input("enter a: "))
#     b = int(input("enter b: "))
#     print(a/b)
# except ZeroDivisionError:
#     print('error!')

# try:
# list_ = [1, 2, 3, 4, 5]   #l ist(range(1, 6))
# print(list_[2])   # 3
# print(list_[25])


# list_ = [1, 2, 3, 4, 5] 
# try: 
# print(list_[25])
# except IndexError:
#     print('no index!')


# try:
#     n1 = int(input("enter:"))
#     n2 = input("enter")
#     print(n1 + n2)
# except TypeError:
#     print("type error")
# except ValueError:
#     print("ошибка значения n1")



# try:
#     n1 = int(input('enter n1: '))
#     n2 = input('enter n2: ')
#     print(n1 / n2)
# except(ZeroDivisionError, ValueError, TypeError):
#     print("Error! ZeroDivisionError, TypeError or ValueError")



# dict_ = {'a': 5, "b": 'c', "D": 20}
# try:
#     key = input("enter key: ")
#     res = dict_[key]
# except KeyError:
#     print("нет такого ключа!")
# else:
#     dict_[key] = res * 2   # dict_ = {k: v * 2 for k, v in dict_.items()}
# print(dict_)



# try:
#     res = a * 2
#     print(res)
# except NameError:
#         print('variable a not found')
#         a = 5
#         res = a * 2
# finally:
#     print(res)


# try:
#     age = int(input("enter: "))
#     if age < 6:
#         raise TypeError("вам нельзя!!!")
# except ValueError:
#     print("age not str!!!")
# except TypeError as name:
#     print(name)

# age = int(input("enter: "))
# if age < 6:
#     raise ValueError("age < 6")




# try:
#     name = input("enter name: ")
#     age = int(input("enter age: "))
# except ValueError:
#     print("age not str")
# else:
#     print(f'hello {name} you are: {age} years old!')
# finally:
#     print("goodbye!")





# email = input('enter email: ')
# try: 
#     if not '@' in email and not '.' in email:
#         raise ValueError("invalid email")
# except ValueError as name:
#     print(name)
# else:
#     print(email)

import email


ID = 0




# data_user = dict()
# i = 0
# email = input('enter email: ')
# password = input('enter pass: ')
# password_confirm = input('enter password_confirm: ')
# try: 
#     if not '@' in email or not '.' in email:
#         raise ValueError("invalid email")
#     if password != password_confirm:
#         raise ValueError("пароли не совпадают!")
# except ValueError as name:
#     print(name)
# else:
#     data_user[f"id: {1}"] = {"email": email, "password": password}
#     i += (data_user)


# pas = "password"
# more_info = {}



# info_users= {
#     "id": ID,
#     "email": None,
#     pas: None,
#     "is_active": False,
#     "activate_key": None,
#     "more_info": None
# }
# email = input("enter email: ")
# password = input("enter pass:word ")
# password_confirm = input("enter password2: ")

# try:
#     if email.endswith("@gmail.com"):
#         raise ValueError(" only @gmail.com")
#     if len(password) < 8:
#         raise ValueError("паоль не может быть меньше 8 символов")
#     if password != password_confirm:
#         raise ValueError("пароль не совпадает")
# except ValueError as name:
#     print(name)
# else:
#     info_users['email'] = email
#     info_users[pas] = password
#     info_users["activate_key"] = email.upper()[::-1] + password[-3:]
# finally:
#     print(info_users)



# CLASS WORK

# dict_ = {1: "umida13", 2: "john123", 3: "python19"}
# dict_ = {value: key for key, value in dict_.items()}
# try:
#   username = input("Введите юзернейм: ")
#   ID = dict_[username]
#   print(ID)
# except KeyError:
#   print('Введенного юзера нет в базе данных')
# else:
#   print(f'Добро пожаловать, {username}')
# finally:
#   print('Спасибо!')


# inp1 = input()
# list1 = inp1.







#  pas = "password"
# more_info = {}



# info_users= {
#     "id": ID,
#     "email": None,
#     pas: None,
#     "is_active": False,
#     "activate_key": None,
#     "more_info": None
# }


# for i in range(2):
#     email = input("enter email: ")
#     password = input("enter pass:word ")
#     password_confirm = input("enter password2: ")

# try:
#     if email.endswith("@gmail.com"):
#         raise ValueError(" only @gmail.com")
#     if len(password) < 8:
#         raise ValueError("паоль не может быть меньше 8 символов")
#     if password != password_confirm:
#         raise ValueError("пароль не совпадает")
# except ValueError as name:
#     print(name)
# else:
#     data = {
#         "email": email,
#         "password": password,
#         "activate_key": email.upper()[::-1]+ password[-3:]
#     }
#     info_user[ID] = data
#     ID += 1
# finally:
#     print(info_users)






