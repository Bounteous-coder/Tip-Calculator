print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == 'S' or size == 'Small':
    bill += 15
    if pepperoni == 'Y':
        bill += 2

elif size == 'M' or size == 'Medium':
    bill += 20
    if pepperoni == 'Y':
        bill += 3

elif size == 'L' or size == 'Large':
    bill += 25
    if pepperoni == 'Y':
        bill += 3

else:
    print("Wrong input")
    exit()

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is ${bill}")