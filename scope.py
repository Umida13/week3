'''
область видмиости в Python - в общем для контекста как глобальная и локальная область видимости
built-ins встроеные обьекты
global - лобальное пространство имен, то к чему есть доступ
enclosed - замкнутое пространство
local - локальное пространство
''' 







# name = "Python19"    # глобвльная прерменная
# def say_hi():
#     name = "test"  # локаьная переменая
#     print(f'hello {name}')
# def say_bye():
#     name = "test1"  # локаьная переменая
#     print(f'good bye {name}')

# say_hi()
# say_bye()




# name = "Python"   #global

# def func1():
#     name = 'Nursultan'  #local
#     test1 = 'test'
#     # print(name)
#     print(locals())
# func1()
# # print(name)
# print(globals())   # функция которая возвращает Словарь где обьявленф все глобальные обьекты
# globals()["Room"] = 15




# def func1():
#     name = "test"
#     locals()["age"] = 21
#     print(locals())

# func1() 






# ID = 0
# print(ID)
# def increment_id(id = None):    #  increment_id увеличение на 1 позициюю 
#     # id += 1
#     # return id 
#     global ID
#     ID += 1
#     # print(ID)

# def decrement_id():
#     global ID
#     ID -= 1


# # increment_id(ID)
# # increment_id(ID)
# # increment_id(ID)

# decrement_id(ID)
# decrement_id(ID)
# decrement_id(ID)
# print(ID) 





# def func1():
#     name = "Aigerim"  # encolosed
#     def func2():
#         nonlocal name
#         name = "Elina"   #local
#         print(name)
#     func2()
#     print(name)
# func1()



# name = "Test1"
# def func1():
#     global name
#     name = "Test2"
#     print(name)
#     name = "Test2"
#     def func2():
#         global name
#         name = "Test3"
#         print(name)
#         def func3():
#             global name
#             name = "Test4"
#             print(name)
#         func3()
#     func2()
# func1()
# print(name) 






# def func1():
#     name = "aktan"  # encloced
#     def func2():
#         nonlocal name
#         name = name.capitalize()   # local
#         # print(name)
#         globals()["last_name"] = "Testov"
#     func2()
#     # print(name)
# func1()
# print(globals())  



