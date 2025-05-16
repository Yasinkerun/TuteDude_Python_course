num = int(input("Enter a number: "))

if num % 2 == 0 and num != 0:
    print(f"{num} is Even")

elif num == 0:
    print(f"{num} is Zero")

else:
    print(f"{num} is Odd")