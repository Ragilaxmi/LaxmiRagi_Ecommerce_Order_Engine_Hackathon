from product import add_product, view_products
from cart import add_to_cart, view_cart, remove_from_cart
from order import place_order, view_orders, cancel_order

def main():
    user = input("Enter username: ")

    while True:
        print("\n1. Add Product")
        print("2. View Products")
        print("3. Add to Cart")
        print("4. Remove from Cart")
        print("5. View Cart")
        print("6. Place Order")
        print("7. Cancel Order")
        print("8. View Orders")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            add_to_cart(user)
        elif choice == "4":
            remove_from_cart(user)
        elif choice == "5":
            view_cart(user)
        elif choice == "6":
            place_order(user)
        elif choice == "7":
            cancel_order()
        elif choice == "8":
            view_orders()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
