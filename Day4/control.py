
# Create a list of employees
employees = [
["Johan Nason", "johan@gmail.com", 23, True ],
["Pat Adams", "pat.adams@gmail.com", 48, False ],
["Tasha Vye","tasha24@gmail.com", 26 , True]
]

# Enter from the user to get a or b
userinput = input("Show all employees(a) OR only best Employees(b):- ")

if userinput == "a":
    for employee in employees :
        if(str(employee[3])=="False"):
            print ("NORMAL:"+employee[0] + " is "  + str(employee[2]) + " years old." +" Email Id:" + str(employee[1]))
elif  userinput == "b":
    for employee in employees :
        if(str(employee[3])=="True"):
            print ("BEST:"+employee[0] + " is "  + str(employee[2]) + " years old." +" Email Id:" + str(employee[1]))
else:
        print("Invalid Option!")