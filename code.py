import json
try:
    with open("users.json","r")as file:
        users=json.load(file)
except FileNotFoundError:
    users=[]
def save_users():
    with open("users.json","w")as file:
        json.dump(users,file)
def add_users():
    print("Add Users...")
    username=input("enter username: ")
    while True:
        try:
            age=int(input("enter age: "))
            break
        except ValueError:
            print("please enter a number!")
    dict1={"username":username,"age":age}
    users.append(dict1)
    save_users()
    print("user added!")
def show_users():
    print("Show Users...")
    if len(users)==0:
        print("there are no users!")
    for number,user in enumerate(users,start=1):
        print(f"{number}. {user["username"]}: {user["age"]} years old")
def search_users():
    print("Search User...")
    search_name=input("search username: ")
    for n in users:
        if n["username"]==search_name:
            print("user found!")
            print(n)
            break
    else:
        print("user not found!")
def delete_users():
    print("Delete User...")
    show_users()
    while True:
        try:
            dy=int(input("enter number of username you want to delete: "))
            if 1<=dy<=len(users):
                break
            print("this number dose not exist!")
        except:
            print("enter number")
    target=dy-1
    users.pop(target)
    save_users()
    print("user deleted!")
def edit_users():
    print("Edit User...")
    show_users()
    while True:
        try:
            edit_user=int(input("enter the number of user you wnat to edit: "))
            if 1<=edit_user<=len(users):
                break
            print("thid number dose not exist!")
        except:
            print("enter number")
    n=users[edit_user-1]
    print("1:Edit name")
    print("2:Edit age")
    print("3:Edit name and age")
    edit_user2=int(input("1 or 2 or 3? "))
    if edit_user2==1:
        while True:
            new_name=input("enter new name: ")
            if new_name.isdigit():
                print("username can not be only number!")
            else:
                n["username"]=new_name
                save_users()
                break
    if edit_user2==2:
        while True:
            try:
                new_age=int(input("enter new age: "))
                break
            except ValueError:
                print("please enter a number!")
        n["age"]=new_age
        save_users()
    if edit_user2==3:
        while True:
            new_name=input("enter new name: ")
            if new_name.isdigit():
                print("username can not be number!")
            else:
                n["username"]=new_name
                save_users()
                break
        while True:
            try:
                new_age=int(input("enter new age: "))
                break
            except ValueError:
                print("please enter a number!")
        n["age"]=new_age
        save_users()
    print("user edited!")
while True:
    print("=====user manager=====")
    print("1:Add Users")
    print("2:Show Users")
    print("3:Search Users")
    print("4:Delete Users")
    print("5:Edit Users")
    print("6:Exit")
    while True:
        try:
            choice=int(input("choose: "))
            if 1<=choice<=6:
                break
            else:
                print("out of range!")
        except ValueError:
            print("please enter number")

    if choice==1:
        add_users()
    elif choice==2:
        show_users()
    elif choice==3:
        search_users()
    elif choice==4:  
        delete_users()
    elif choice==5:
        edit_users()       
    elif choice==6:
        print("Exit...")
        break