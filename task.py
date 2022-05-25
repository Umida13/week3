
# check list

# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i

#     return res

# print(factorial(3))
# print(factorial(5))




#GUES NUMBER
# from itertools import count
# import numbers
# import random 
# def some():
#     gues = 0
#     count = 0
#     number = random.randint(1, 11)
#     while gues != number:
#         print(number)
#         gues = int(input("enter number: "))
#         count += 1 # count = count + 1 

#         if gues > number:
#             print("загаданное число меньше")
#         elif gues < number:
#             print("загаданное число больше")
        
#     again = input(f'Угадали! кол-во попыток = {count}\nХотите заново?')
#     if again.lower() == 'yes':
#             some()
#     else:
#             print('ok, bye')
# some()


# from collections import defaultdict

# def check_pali(our_string):
#     our_string = our_string.lower()
#     counts = defaultdict(int)
#     for letter in our_string:
#         if ord(letter) >= 97 and ord(letter) <= 122:
#             counts[letter] += 1 
#     # print(counts)
#     middle = ""
#     for letter in counts:
#         if middle and counts[letter] % 2 == 1:
#             return False
#         elif counts[letter] % 2 == 1:
#             middle = letter
#     return True
# print(check_pali('радар'))





# a = ['1', '2', '3', '4', '5']
# a = map(int, a)
# print(a)

# name = "Makers"
# def outer_func():
#     name = "Hello"
#     def inner_func():
#         name = "World"
#         print(name)

#     inner_func()
#     print(name)
# outer_func()



from itertools import count
import numbers
import random 
def some():
   
    number = random.randint(1, 20)
    while True:
        number = int(input("Enter number: "))
        if number == random.randint(1, 5):
            print("ghbdtn")
        elif number == 0:
            print("Не волнуйся, если не работает. Если бы все всегда работало, у тебя бы не было работы")
        else:
            print("пока")
some()