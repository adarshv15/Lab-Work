"""Retail point-of-sale system.
Supports checkout, promotions, and receipt logging.
"""

import secrets

PRICE_LIST = {
    "pen": 10,
    "notebook": 45,
    "bag": 799,
    "bottle": 150,
}

sales_total = 0.0
receipt_lines = []


def process_checkout(cart_items, tax_rate=0.05, receipts=None):
    """Calculate a checkout total, validate inputs, and record the receipt."""
    global sales_total

    if receipts is None:
        receipts = []

    if not isinstance(tax_rate, (int, float)) or isinstance(tax_rate, bool):
        raise ValueError("Tax rate must be a number.")

    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    subtotal = 0.0

    for item, quantity in cart_items:
        if item not in PRICE_LIST:
            raise ValueError(f"Unknown item: {item}")

        if (
            not isinstance(quantity, int)
            or isinstance(quantity, bool)
            or quantity <= 0
        ):
            raise ValueError("Quantity must be a positive integer.")

        subtotal += PRICE_LIST[item] * quantity

    total = round(subtotal * (1 + tax_rate), 2)
    receipts.append(total)
    sales_total += total

    receipt_number = secrets.randbelow(9000) + 1000
    receipt_lines.append(
        f"Receipt #{receipt_number} total={total:.2f}"
    )

    return total


def apply_promo_code(code_str):
    """Apply a supported promotion to the current sales total."""
    if code_str == "10OFF":
        return round(max(0, sales_total - 50), 2)

    if code_str == "10PERCENT":
        return round(sales_total * 0.90, 2)

    raise ValueError("Invalid promo code.")


def update_stock(item, qty):
    """Validate a stock update request for a known item."""
    if item not in PRICE_LIST:
        raise ValueError(f"Unknown item: {item}")

    if not isinstance(qty, int) or isinstance(qty, bool) or qty <= 0:
        raise ValueError("Stock quantity must be a positive integer.")

    print(f"Stock update requested for {item}: {qty} units.")


def save_receipt_log(file="pos_log.txt"):
    """Append recorded receipts to a UTF-8 encoded log file."""
    with open(file, "a", encoding="utf-8") as receipt_file:
        for line in receipt_lines:
            receipt_file.write(line + "\n")


def print_sales():
    """Display the running sales total."""
    print(f"Sales so far: {sales_total:.2f}")


def main():
    """Run sample checkouts and demonstrate promotion handling."""
    global sales_total

    sales_total = 0.0
    receipt_lines.clear()

    bills = [
        [("pen", 3), ("notebook", 2)],
        [("bag", 1), ("bottle", 1)],
        [("bottle", 4)],
        [("pen", 2)],
    ]

    for index, cart in enumerate(bills, start=1):
        try:
            print(f"Bill {index}: {process_checkout(cart)}")
        except ValueError as error:
            print(f"Bill {index} error: {error}")

    try:
        update_stock("bottle", 5)
    except ValueError as error:
        print(f"Stock error: {error}")

    print("After promo:", apply_promo_code("10PERCENT"))

    code = input(
        "Enter promo code (10PERCENT or 10OFF): "
    ).strip().upper()

    if not code:
        code = "10OFF"

    try:
        print("After your promo:", apply_promo_code(code))
    except ValueError as error:
        print("Promo error:", error)

    try:
        save_receipt_log()
        print("Receipt log saved.")
    except OSError as error:
        print(f"Could not save receipt log: {error}")

    print_sales()


if __name__ == "__main__":
    main()
