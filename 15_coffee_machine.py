MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def report():
    """Показывает, сколько ресурсов в кофемашине."""
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${profit}")


def is_enough(order_ingredients):
    """Проверяет, достаточно ли ингридиентов для создания выбранного напитка."""
    for i in order_ingredients:
        if resources[i] >= order_ingredients[i]:
            return True
        else:
            print(f"Sorry there is not enough {i}.")
            return False


def is_transaction_successful(type_of_coffee):
    """Подсчитывает кол-во вставленных монет, выдает сдачу, если было внесено достаточно денег.
    Добавляет заплаченные за напиток монеты в кофемашину."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    should_pay = MENU[type_of_coffee]["cost"]
    if total < should_pay:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += should_pay
        print(f"Here is ${round(total - should_pay, 2)} in change.")
        return True


def make_coffee(type_of_coffee, ingredients):
    """Вычитает нужное количество ингрединетов из ресурсов кофемашины."""
    for i in resources:
        if i in ingredients:
            resources[i] -= ingredients[i]
    print(f"Here is your {type_of_coffee} ☕️. Enjoy!")


turn_off = False
while not turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        turn_off = True
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        if is_enough(drink["ingredients"]):
            if is_transaction_successful(choice):
                make_coffee(choice, drink["ingredients"])

