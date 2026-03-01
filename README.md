# Máquina de Refrigerantes (Soda Machine)

Este é um projeto simples de simulação de uma máquina de refrigerantes desenvolvido em Python. Ele permite que os usuários insiram créditos, escolham refrigerantes para comprar e até mesmo reabasteçam a máquina.

## 🚀 Funcionalidades

- **Inserir Crédito**: Adicione saldo à máquina para realizar compras.
- **Comprar Refrigerante**: Escolha entre Coca-Cola, Fanta ou Sprite. O sistema verifica se há saldo suficiente e se o produto está em estoque.
- **Sistema de Troco**: Ao finalizar a compra ou sair, a máquina devolve o saldo restante como troco.
- **Abastecer Máquina**: Opção para repor o estoque de todos os refrigerantes para a capacidade máxima.
- **Interface de Terminal**: Menus interativos e fáceis de usar diretamente no console.

## 🛠️ Estrutura do Projeto

O projeto é dividido em quatro módulos principais:

- **[refrigerant.py](refrigerant.py)**: Define a classe `Refrigerant`, representando um produto com nome, preço e quantidade.
- **[machine.py](machine.py)**: Contém a classe `Machine`, responsável pela lógica de negócios, gerenciamento de crédito e estoque.
- **[terminal.py](terminal.py)**: Gerencia a interface de texto, exibição de menus e validação de entradas do usuário.
- **[interface.py](interface.py)**: O ponto de entrada do sistema que coordena a interação entre a máquina e o terminal.

## 💻 Como Executar

Para iniciar a simulação, certifique-se de ter o Python instalado em sua máquina e execute o arquivo principal:

```bash
python interface.py
```

## 📝 Exemplo de Uso

1. Ao iniciar, escolha a opção `1` para inserir crédito.
2. Digite o valor desejado (ex: `10.00`).
3. Escolha a opção `2` para comprar um refrigerante.
4. Selecione o refrigerante e a quantidade.
5. A máquina processará a compra e informará seu troco.
