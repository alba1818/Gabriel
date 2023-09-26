while True:
    try:
        numero = int(input("Digite um número inteiro (0 sai): "))
        if numero == 0:
            break
    except Exception:
        print("Número inválido!")




