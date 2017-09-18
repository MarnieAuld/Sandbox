"""
Write a program which asked a user for SIZE and NUMBER OF TOPPINGS and return the final price.
"""

SMALL_KEBAB = 7.50
LARGE_KEBAB = 10
TOPPING_PRICE = 0.50
NUMBER_OF_FREE_TOPPINGS = 2


def main():
    kebab_price = get_kebab_size() + get_number_of_toppings()
    print("Kebab price = {:.2f}".format(kebab_price))


def get_kebab_size():
    user_kebab_size = input("What size kebab do you require? SMALL or LARGE").upper()
    valid_input = False
    while not valid_input:
        if user_kebab_size == "SMALL":
            valid_input = True
            kebab_size = SMALL_KEBAB
        elif user_kebab_size == "LARGE":
            valid_input = True
            kebab_size = LARGE_KEBAB
        else:
            valid_input = False
    return kebab_size


def get_number_of_toppings():
    try:
        number_of_toppings = int(input("How many toppings do you require?"))
        if number_of_toppings <= NUMBER_OF_FREE_TOPPINGS:
            topping_charge = 0
        else:
            topping_charge = TOPPING_PRICE * (number_of_toppings - NUMBER_OF_FREE_TOPPINGS)
    except ValueError:
        print("Invalid input; please enter a valid number")
    return topping_charge


main()
