# PROGRAM REQUIREMENTS
# 1. Print report
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make Coffee

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    global profit
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    desc = f"\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}"
    return desc


def resource_cal(drink):
    ingredients = MENU[drink]["ingredients"]
    isEnough = True
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry there is no enough {i}")
            isEnough = False
        else:
            if i == "water":
                resources["water"] -= ingredients["water"]
            elif i == "milk":
                resources["milk"] -= ingredients["milk"]
            else:
                resources["coffee"] -= ingredients["coffee"]

    return isEnough


def price_calc(drink):
    price = MENU[drink]["cost"]
    # penny - 0.01
    # dime - 0.10
    # nickel - 0.05
    # quarter - 0.25
    print("ENTER COINS")
    quarter = int(input("How many quarters: "))
    nickel = int(input("How many nickel: "))
    dime = int(input("How many dime: "))
    penny = int(input("How many pennies: "))

    # calculating inputted coins
    handed_money = round((quarter * 0.25) + (nickel * 0.05) + (dime * 0.10) + (penny * 0.01), 2)

    # check if there's enough money to buy
    while handed_money < price:
        print(f"\nThe cost is ${price} and you only paid ${handed_money}???")
        quarter = int(input("How many quarters: "))
        nickel = int(input("How many nickel: "))
        dime = int(input("How many dime: "))
        penny = int(input("How many pennies: "))
        handed_money = round((quarter * 0.25) + (nickel * 0.05) + (dime * 0.10) + (penny * 0.01), 2)

    if resource_cal(drink):
        print(f"You handed in ${handed_money}. Cost of {drink} is ${price}")
        if handed_money != price:
            change = round(handed_money - price, 2)
            print(f"Here's your change: ${change}")

        print(f"Thank you for ordering... Enjoy your {drink}!")
        # add money profit
        global profit
        profit += price

    else:
        print(f"Refunding your ${handed_money}...")  # should refund all the money offered, not only the price


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        print(report())
    elif order == 'off':
        print("Turning off the machine...")
        break
    elif order == "espresso":
        price_calc(order)

    elif order == "latte":
        price_calc(order)

    elif order == "cappuccino":
        price_calc(order)
    else:
        print("Invalid order")

    choice = input("\nDo you want to order again? Y/N:  \n").lower()
    if choice == 'n':
        break


# just to check profit
print(f"Profit is: {profit}")
