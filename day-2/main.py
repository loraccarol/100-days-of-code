print("Welcome to the tip calculator!")

bill = input("What was the total bill? $ ")
tip = input("How much tip you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")


with_tip = float(bill) + float(tip) / 100 * float(bill)
pay = with_tip / int(people)

print(f"Each person should pay: ${round(pay, 2)}")