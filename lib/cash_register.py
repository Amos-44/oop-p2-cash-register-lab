#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):

        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):

        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):

        if self.total == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        if self.total.is_integer():
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):

        if not self.previous_transactions:
            self.total = 0
            self.items = []
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        removed = 0
        new_items = []

        for i in self.items:
            if i == last["item"] and removed < last["quantity"]:
                removed += 1
                continue
            new_items.append(i)

        self.items = new_items

        if self.total == 0:
            self.total = 0.0