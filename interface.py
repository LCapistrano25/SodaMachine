from machine import Machine
from terminal import Terminal

capacity = 50

class Interface:
    def __init__(self):
        self.machine = Machine()
        self.terminal = Terminal(self.machine)
        
    def handle_main_menu(self):
        while True:
            option = self.terminal.main_menu()
            if option == 1:
                self.insert_credit()
            elif option == 2:
                if self.machine.get_credit() == 0:
                    print("\nCrédito insuficiente. Por favor, insira crédito.")
                    continue

                result = self.select_refrigerant()

                if result == False:
                    continue

                break

            elif option == 3:
                self.refuel_machine()

            elif option == 4:
                print(f"\nSeu troco: R$ {self.machine.get_credit():.2f}")
                print("Obrigado por utilizar a máquina de refrigerantes!\n")
                break
            else:
                break
    
    def select_refrigerant(self):
        refrigerant_option = self.terminal.purchase_menu()

        if refrigerant_option == 4:
            return False # Voltar ao menu principal

        quantity = self.terminal.validate_input(
            f"Quantas unidades você deseja comprar? Você tem R${self.machine.get_credit():.2f} de crédito: ", int)

        if quantity <= 0:
            print("Quantidade inválida.")
            return False

        # Tentar realizar a compra
        self.machine.buy_refrigerant(refrigerant_option, quantity)
        return True
    
    def insert_credit(self):
        credit = self.terminal.validate_input("\nDigite o valor do crédito: ", float)
        if credit <= 0:
            print("Valor inválido.")
            return
        
        credit_total = round(credit + self.machine.get_credit(), 2)

        self.machine.set_credit(credit_total)
        print(f"Crédito adicionado: R$ {credit_total:.2f}")

    def refuel_machine(self):
        refrigerants = self.machine.get_refrigerants()
        for refrigerant in refrigerants:
            refrigerant.set_quantity(capacity)
        print("\nMáquina abastecida com sucesso.")


if __name__ == "__main__":
    interface = Interface()
    interface.handle_main_menu()