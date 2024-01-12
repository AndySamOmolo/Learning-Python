n = input("Enter a number: ")
a = n[0]
b = n[1]

if int(n) % 2 == 0:
    print(str(n) + " is divisible by 2")

elif (int(a) + int(b)) % 3 == 0:
    print(str(n) + " is divisible by 3")

else:
    print(str(n) + " is not divisible by 2")

