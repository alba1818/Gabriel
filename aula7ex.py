
#Tabela de um supermercado

tabela = {'tomate': 1.5, 'alface': 0.75, 'feijão': 8.0, 'arroz': 15.0, 'uva': 7.0}
while True:
    produto = input("\nDigite o nome do produto ou fim para encerrar: ")
    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço: R${tabela[produto]:.2f}")
    else:
        print("Produto não encontrado")
