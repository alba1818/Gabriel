import random
#EXCERCICIo


num_sort = random.randint(1,5)
chance = 0
while chance < 3:
    num_escolha = int(input("entre com o número inteiro"
                        " >= 1 e <= 5: "))
    if num_escolha == num_sort:
        print("Você acertou!")
    else:
        print("Você errou!")
    chance += 1
