print("Welcome to the tip calculator!")
total = float(input("What was the bill's total?"))
tip = int(input("How much tip % would you like to give? 10, 12, or 15"))
people = int(input("How many people want to split the bill?"))
bill = (tip / 100) * total + total
bill_per_person =  bill / people
print(bill)
print(f'Each person should pay {bill_per_person}')
