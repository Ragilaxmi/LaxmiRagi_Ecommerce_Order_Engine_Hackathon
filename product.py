products = {}

def add_product():
    pid = input("Enter Product ID: ")
    if pid in products:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock: "))

    products[pid] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully!")

def view_products():
    if not products:
        print("No products available")
        return

    for pid, details in products.items():
        print(pid, details)
