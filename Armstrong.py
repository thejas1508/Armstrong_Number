Storage = 0
anumber = int(input("Enter the Number:"))
temp = anumber
while temp > 0:
    Remainder = temp % 10
    Storage = Storage + Remainder**3
    temp = temp // 10
if anumber == Storage:
     print(anumber,"is an Armstrong Number")
else:
     print(anumber,"is not an Armstrong Number")
