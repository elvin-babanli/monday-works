def pizza_orders():
    price = 0

size = input("Add a size: small / large / extra-large:  ")
if size == "small":
    price =10
elif size == "large":
    price = 15
elif size == "extra-large":
    price = 20

peperoni = input("Do you wanna add peperoni? (yes / no): ")
if peperoni == "yes":
    price = price + 2

chesse = input("Do you wanna add cheese? (yes / no): ")
if chesse == "yes":
    price = price + 1

tip = price * 0.1

final = price + tip
print("Your final bill is: $",final)

pizza_orders()