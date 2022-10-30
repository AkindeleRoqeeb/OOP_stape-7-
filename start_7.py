import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        ############### run validation to the recieve argument ######################
        assert price >= 0, f"price {price} is not greater or equal zero"

        ##################### OR ###############
        assert quantity >= 0, f"quality {quantity} is not greater or equal zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    ############## Asign to self object ############################
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('item2.txt', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"item('{self.name}', {self.price}, {self.quantity})"

Item.instantiate_from_csv()
print(Item.all)