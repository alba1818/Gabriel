from random import choice

frutas = ["uva", "pera", "maça", "laranja"]
sorteio = choice(frutas) #pode por dentro do while q ai sempre vai mudando o sorteio
print(sorteio)
while True:
    escolha_fruta = input("Digite uma fruta: ")
    if escolha_fruta == sorteio:
        print("Você acertou!")
    elif escolha_fruta == "fim":
        break
    else:
        print("Você errou!")
