estoque = {"jetta": [10, 100000], "golf": [16, 130000], "a3": [12, 160000]}

total = 0

while True:


venda = [[f"{modelo}",3], ["golf", 5], ["a3", 7]]

total = 0
for carro, quantidade in venda:
    preco = estoque[carro][1]
    custo = preco * quantidade
    print(f"{carro}: {quantidade} x {preco} = {custo}")
    estoque[carro][0] -= quantidade
    total += custo

print(f"Custo total: {total}")

for chave, dados in estoque.items():
    print("Carro:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: R$ {dados[1]}")
