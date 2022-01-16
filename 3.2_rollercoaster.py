print("Hello, I'm the roller coaster ticket machine. Please follow the instructions.")
height = int(input("What is your height in cm? "))
if height < 120:
    print("You can't ride. :(")
else:
    print("You can ride.")
    age = int(input("What's your age? "))
    if age < 12:
        price = 5
    elif age < 18:
        price = 7
    else:
        price = 12
    print(f"Your ticket costs ${price}")
    photo = input("Do you want a photo? Y or N: ")
    if photo == "Y":
        price += 3
    elif photo == "N":
        price = price
    else:
        raise ValueError("Please, enter Y or N.")
    print(f"The total bill is ${price}")



