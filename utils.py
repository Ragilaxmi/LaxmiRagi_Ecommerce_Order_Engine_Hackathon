def apply_coupon(total):
    if total > 1000:
        total *= 0.9

    code = input("Enter coupon code (or press Enter): ")

    if code == "SAVE10":
        total *= 0.9
    elif code == "FLAT200":
        total -= 200

    return total
