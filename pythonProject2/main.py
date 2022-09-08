print("***************************")
print(" Welcome to employees page ")
print("***************************\n\n")
print("1-Add a employee.\n")
print("2-List the employees.\n")
print("3-Delete the list.\n")
print("4-Delete a employee\n")
choose=int(input("Choose the number that you want: "))
print("\n\n")
if choose==1:
    employee = input("Enter the employee's name: ")
    with open("employeeslist.txt", "a") as f:
        f.write(employee)
        f.write("\n")
    answer=0
    while answer!=1:
        answer = input("Do you want to add more?(Y)or(N) ")
        if answer == "y" or answer=="Y":
            with open("employeeslist.txt", "a") as f:
                new_employee=input("Enter the employee's name: ")
                f.write(new_employee)
                f.write("\n")
        elif answer=="n" or answer=="N":
            print("Adding employee succesfully completed")
            answer=1
        else:
            print("Wrong answer.Try again!")
elif choose==2:
     with open("employeeslist.txt", "r") as f:
        employees = f.read()
        if employees=="":
            print("Firstly add a employee")
        else:
            print(employees)
elif choose==3:
     with open("employeeslist.txt", "w") as f:
         f.write("")
elif choose==4:
    with open("employeeslist.txt", "r") as f:
        employees = f.read()
        print(employees)
    if employees=="":
        print("Firstly add a employee")
    else:
        x = int(input("On which line is the employee that you want? "))
        with open("employeeslist.txt", "r") as f:
            info = f.readlines()
            info.pop(x - 1)
        with open("employeeslist.txt", "w") as f:
            for i in range(0, len(info)):
                f.write(info[i].strip())
                f.write("\n")




