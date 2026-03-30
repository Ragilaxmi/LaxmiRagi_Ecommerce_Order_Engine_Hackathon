from cart import carts
from product import products
from payment import process_payment

orders = {}
order_id_counter = 1

def place_order(user):
    global order_id_counter

    if user not in carts or not carts[user]:
        print("Cart empty")
        return

    cart = carts[user]
    total = 0

    for pid, qty in cart.items():
        total += products[pid]["price"] * qty

    print("Total amount:", total)

    success = process_payment()

    if not success:
        print("Payment failed! Rolling back...")
        for pid, qty in cart.items():
            products[pid]["stock"] += qty
        carts[user] = {}
        return

    order_id = order_id_counter
    order_id_counter += 1

    orders[order_id] = {
        "user": user,
        "items": cart.copy(),
        "total": total,
        "status": "PLACED"
    }

    carts[user] = {}

    print("Order placed successfully! Order ID:", order_id)

def view_orders():
    for oid, details in orders.items():
        print(oid, details)

def cancel_order():
    oid = int(input("Enter Order ID: "))

    if oid not in orders:
        print("Order not found")
        return

    if orders[oid]["status"] == "CANCELLED":
        print("Already cancelled")
        return

    orders[oid]["status"] = "CANCELLED"

    for pid, qty in orders[oid]["items"].items():
        products[pid]["stock"] += qty

    print("Order cancelled")
