print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
if tip == 10 or tip == 12 or tip == 15:
    pay = (bill / people) + (bill / people) * (tip / 100)
    print(f"Each person should pay: ${round(pay, 2)}")
else:
    raise ValueError("Wrong tip!")



