
employee_file = open("employees.txt","r")

print(employee_file.readable())

print(employee_file.read())

print(employee_file.readline())

print(employee_file.readlines())

print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)


employee_file = open("employees.txt","a")

employee_file.write("\nToby - Human Resources")

employee_file = open("employees1.txt","w")

employee_file.write("\nToby - Human Resources")


employee_file.close()