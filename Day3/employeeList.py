employees = [
["Johan Nason", "johan@gmail.com", 23 ],
["Pat Adams", "pat.adams@gmail.com", 48 ],
["Tasha Vye","tasha24@gmail.com", 26 ]
]


# Age is integere so we need to convert it to String using str(intValue)
# If Boolean also needs to be printed we need to use str(booleanValue)¨

for employee in employees :
    print (employee[0] + " is"  + str(employee[2]) + " years old." +" Email Id:" + str(employee[1]))
