print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = 1 + int(input("How much tip would you like to give? 10, 12 or 15? ")) / 100
people = int(input("How many people to split the bill? "))

calculate = (bill * tip)  / people

print(f"Each person should pay: ${round(calculate, 2)}")