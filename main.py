# import DB
# DB.DATA_BASE 

# def add_data_base(**kwargs):
#     DATA_BASE[ID]= kwargs
#     increment()



# from DB import DATA_BASE, ID, increment
# print(DATA_BASE)

# email = input("enter email: ")
# name = input("enter name: ")
# phone = input("enter phone: ")

# try:
#     if not phone.startswith("+996"):
#         raise ValueError("number starts with +996")
# except ValueError as error:
#         print(error)
# else:
#     DATA_BASE = ["email"]
#     DATA_BASE = ["name"]
#     DATA_BASE = ["phone"]

# print(DATA_BASE)


from DB import DATA_BASE


# def increment():
#     global ID
#     ID += 1

# while True:
#     answer = input("enter answer")
#     if answer == "":
#         break
#     email = input("enter email: ")
#     name = input("enter name: ")
#     phone = input("enter phone: ")

#     try:
#         if not phone.startswith("+996"):
#             raise ValueError("number starts with +996")
#     except ValueError as error:
#             print(error)
#     else:
#         info_user = {}
#         info_user["email"] = email
#         info_user["name"] = name
#         info_user["phone"] = phone

#     print(DATA_BASE)



 
from DB import DATA_BASE, ID


# def increment():
#     global ID
#     ID += 1
    

# def generate_user(*args, **kwargs):
#     email = kwargs.get("email")
#     name = kwargs.get("name")
#     phone = kwargs.get("phone")
#     return {"email": email, "name": name, "phone": phone}

# while True:
#     answer = input("enter answer: ")
#     if answer == "":
#         break
#     email = input("enter email: ")
#     name = input("enter name: ")
#     phone = input("enter phone: ")
#     try:
#         if not phone.startswith("+996"):
#             raise ValueError("Номер должен начинаться только на +996")
#     except ValueError as error:
#         print(error)
#     else:
#         info = generate_user(name=name, email=email, phone=phone)
       
#         add_data_base(**info)





# print(DATA_BASE)




from DB import DATA_BASE, ID


# def increment():
#     global ID
#     ID += 1

# while True:
#     answer = input("enter answer: ")
#     if answer == "":
#         break
#     email = input("enter email: ")
#     name = input("enter name: ")
#     phone = input("enter phone: ")
#     try:
#         if not phone.startswith("+996"):
#             raise ValueError("Номер должен начинаться только на +996")
#     except ValueError as error:
#         print(error)
#     else:
#         info_user = dict()
#         info_user["email"] = email
#         info_user["name"] = name
#         info_user["phone"] = phone
#         print(ID)
#         DATA_BASE[ID] = info_user
#         increment()

# print(DATA_BASE)