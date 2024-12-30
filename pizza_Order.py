size = input("Enter your pizza size according to S/M/L?")
bill = 0

if size == "S" or size == "s":
    bill+=100
    print("Small pizza's price is 100rs.")
elif size == "m" or size == 'M':
    bill += 200
    print("Medium pizza's price is 200rs.")
elif size == 'L' or size =='l':
    bill += 300
    print("Large pizza's size is 300rs.")

add_pepperoni = input("Do you want pepperoni(Y/N)?")

if add_pepperoni == "Y" or add_pepperoni == 'y':
    if size == "S" or size == 's':
        bill+=30
    else:
        bill+=50

extra_cheese = input("Do youu want extra cheese?(Y/N)")

if extra_cheese == 'Y' or extra_cheese == 'y':
    bill+=20

print(f"Your final bill is {bill}")