from refrigerant import Refrigerant

class Terminal:
    def __init__(self, machine):
        self.machine = machine

    def validate_input(self, text, type):
        while True:
            try:
                value = type(input(text))
                return value
            except ValueError:
                print("Valor inválido. Tente novamente.")

    def validate_option(self, text, type, options):
        while True:
            try:
                value = type(input(text))
                if value in options:
                    return value
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Valor inválido. Tente novamente.")

    def main_menu(self):
        print("\nBem vindo ao Menu Principal!\n")

        print(f"Crédito: R$ {self.machine.get_credit():.2f}\n")

        print("1 - Inserir crédito")
        print("2 - Comprar Refrigerante")
        print("3 - Abastecer máquina")
        print("4 - sair")

        option = self.validate_option(f"\nEscolha uma opção: ", int, [1, 2, 3, 4])
        return option
    
    def purchase_menu(self):
        print("\nEscolha o refrigerante que deseja comprar:\n")

        self.show_refrigerants()

        option = self.validate_option("\nEscolha uma opção: ", int, [1, 2, 3, 4])
        return option

    def show_refrigerants(self):
        print("\nRefrigerantes disponíveis:\n")
        option = 0
        for refrigerant in self.machine.get_refrigerants():
            option += 1
            print(f"{option} - {refrigerant.get_name()} à R$ {refrigerant.get_price():.2f} - {refrigerant.get_quantity()} unidades")
        print(f"{option + 1} - Voltar")

