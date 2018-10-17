def make_pizza( size,*toppings):
    print("\nMaking a "+str(size)+"-pizza with following toppings:")
    for topping in toppings:
        print("-"+topping)
