phNo = input("0796929699")
length = len(phNo)
if length == 12 \
    and phNo[3] == "-" \
    and phNo[7] == "-" \
    and phNo[:3].isdigit() \
    and phNo[4:7].isdigit() \
    and phNo[8:].isdigit() :
    print("Valid Phone Number")
else :
    print("Invalid Phone Number")