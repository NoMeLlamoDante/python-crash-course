def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following topping")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16,'peperoni')
make_pizza(12,'mushrooms', 'green pepers', 'extra cheese')