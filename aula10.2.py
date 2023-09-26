import random
for i in range(10):
    print(random.randint(1,10))

#outro exemplo
num = random.randint(1,5)

num_sort = random.randint(1,5)
num_escolha = int(input("entre com o número inteiro"
                        " >= 1 e <= 5: "))

if num_escolha == num_sort:
    print("Você acertou!")
else:
    print("Você errou!")


