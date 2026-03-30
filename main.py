from product import add_product, view_products
from cart import add_to_cart, view_cart, remove_from_cart
from order import place_order, view_orders, cancel_order
from utils import apply_coupon

def main():
    user = input("Enter username: ")

    while True:
        print("\n===== E-Commerce CLI =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Add to Cart")
        print("4. Remove from Cart")
        print("5. View Cart")
        print("6. Apply Coupon")
        print("7. Place Order")
        print("8. Cancel Order")
        print("9. View Orders")
        print("10. Low Stock Alert")
        print("11. Return Product")
        print("12. Simulate Concurrent Users")
        print("13. View Logs")
        print("14. Trigger Failure Mode")
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
            print("Coupon feature coming soon...")

        elif choice == "7":
            place_order(user)

        elif choice == "8":
            cancel_order()

        elif choice == "9":
            view_orders()

        elif choice == "10":
            print("Low stock alert feature coming soon...")

        elif choice == "11":
            print("Return product feature coming soon...")

        elif choice == "12":
            print("Concurrency simulation coming soon...")

        elif choice == "13":
            print("Logs feature coming soon...")

        elif choice == "14":
            print("Failure mode triggered (demo)...")

        elif choice == "0":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
