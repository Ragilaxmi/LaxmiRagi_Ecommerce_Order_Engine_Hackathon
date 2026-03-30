from product import products

carts = {}

def add_to_cart(user):
    pid = input("Enter Product ID: ")
    qty = int(input("Enter Quantity: "))

    if pid not in products:
        print("Product not found")
        return

    if products[pid]["stock"] < qty:
        print("Not enough stock")
        return

    carts.setdefault(user, {})
    carts[user][pid] = carts[user].get(pid, 0) + qty

    products[pid]["stock"] -= qty
    print("Added to cart")

def view_cart(user):
    if user not in carts or not carts[user]:
        print("Cart empty")
        return

    total = 0
    for pid, qty in carts[user].items():
        price = products[pid]["price"]
        total += price * qty
        print(pid, qty)

    print("Total:", total)

def remove_from_cart(user):
    pid = input("Enter Product ID: ")

    if pid in carts.get(user, {}):
        qty = carts[user][pid]
        products[pid]["stock"] += qty
        del carts[user][pid]
        print("Removed from cart")
