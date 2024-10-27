from refrigerant import Refrigerant

class Machine:
    def __init__(self):
        self._credit = 0
        self._refrigerants = [
            Refrigerant("Coca-Cola", 5.50, 50),
            Refrigerant("Fanta", 5.00, 50),
            Refrigerant("Sprite", 4.00, 50)
        ]

    # Getters
    def get_credit(self):
        return self._credit
    
    def get_refrigerants(self):
        return self._refrigerants
    
    # Setters
    def set_credit(self, credit):
        self._credit = credit

    def set_refrigerants(self, refrigerants):
        self._refrigerants = refrigerants

    def reduce_credit(self, amount):
        self._credit -= amount
        
    # Método para realizar a compra
    def buy_refrigerant(self, option, quantity):
        refrigerant = self._refrigerants[option - 1]
        total_price = refrigerant.get_price() * quantity

        if self._credit < total_price:
            print("\nCrédito insuficiente.")
            print(f"Seu troco: R$ {self.get_credit():.2f}")
            self.set_credit(0)
            return False

        if refrigerant.get_quantity() < quantity:
            print("\nQuantidade indisponível.")
            print(f"Seu troco: R$ {self.get_credit():.2f}")
            self.set_credit(0)
            return False

        # Atualiza o crédito e a quantidade do refrigerante
        self.reduce_credit(total_price)
        refrigerant.set_quantity(refrigerant.get_quantity() - quantity)

        print("\nCompra realizada com sucesso!")
        print(f"Você comprou {quantity} unidade(s) de {refrigerant.get_name()} por R$ {total_price:.2f}.")
        print(f"Seu troco: R$ {self.get_credit():.2f}")

        self.set_credit(0)

        return True
