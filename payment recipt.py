class PaymentReceipt:
    def __init__(self, receipt_number, date, customer_name, items, total_amount, payment_method):
        self.receipt_number = receipt_number
        self.date = date
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.payment_method = payment_method

    def generate_receipt(self):
        receipt = f"""
**Payment Receipt**

**Receipt Number:** {self.receipt_number}
**Date:** {self.date}

**Customer Name:** {self.customer_name}

**Items Purchased:**
"""
        for item in self.items:
            receipt += f"  - {item['name']}: ${item['price']} x {item['quantity']} = ${item['total']:.2f}\n"
        receipt += f"""
**Total Amount:** ${self.total_amount:.2f}

**Payment Method:** {self.payment_method}

**Thank you for your payment!**
"""
        return receipt

# Example usage:
items = [
    {'name': 'Apple iPhone', 'price': 999.99, 'quantity': 1, 'total': 999.99},
    {'name': 'Samsung TV', 'price': 1299.99, 'quantity': 1, 'total': 1299.99},
    {'name': 'Boat Headphones', 'price': 99.99, 'quantity': 2, 'total': 199.98}
]

receipt = PaymentReceipt(
    receipt_number='001',
    date='2024-07-23',
    customer_name='Manasa',
    items=items,
    total_amount=sum(item['total'] for item in items),
    payment_method='Credit Card'
)

print(receipt.generate_receipt())