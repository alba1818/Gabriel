#Funções

def soma(a,b):
    print(a+b)

soma(5,8)

def ehpar(x):
    return x % 2 == 0

print(ehpar(2))
print(ehpar(5))

def ehimpar(h):
    return h % 2 > 0

print(ehimpar(7))

def par_ou_impar(x):
    if ehpar(x):
        return "par"
    else:
        return "impar"

print(par_ou_impar(7))
print(par_ou_impar(19))
print(par_ou_impar(6))

def maior_num(a,b):
    if a > b:
        return a
    else:
        return b

print(maior_num(9,10))

lista_mun = [8,9]
print(max(lista_mun))

def maior_num(a,b):
    lista = [a,b]
    return max(lista)

print(maior_num(14,19))

def valida_num(numero, minimo, maximo):
    return numero >= minimo and numero <= maximo

print(valida_num(5,5, 10))
print(valida_num(1,5, 10))

def barra():
    return "*" * 40
print(barra())

def barra_op(n=40, caractere= "*"):
    return n * caractere

print(barra_op())
print(barra_op(80, "."))


