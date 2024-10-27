class Refrigerant:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    # Getters
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def get_quantity(self):
        return self._quantity
    
    # Setters
    def set_name(self, name):
        self._name = name

    def set_quantity(self, quantity):
        self._quantity = quantity

    def set_price(self, price):
        self._price = price