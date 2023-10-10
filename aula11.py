#arquivo = open("aula_texto.txt", "w")
#arquivo.write("Primeira aula de arquivo de texto")
#arquivo.close

#with open("aula_texto.txt", "w") as arquivo:
    #arquivo.write("Eu gosto de fruta")

#arquivo = open("aula_texto.txt", "r")
#print(arquivo.read())
#arquivo.close()

#with open("aula_texto.txt", "r") as arquivo:
    #print(arquivo.read())

#  with open("aula_texto.txt", "a") as arquivo:
#     arquivo.write("\nAmanha fara sol.")

with open("meses.txt", "w") as meses:
    meses.write("01 - Janeiro\n")
    meses.write("02 - Fevereiro\n")
    meses.write("03 - Março\n")
    meses.write("04 - Abril\n")
    meses.write("05 - Maio\n")
    meses.write("06 - Junho\n")
    meses.write("07 - Julho\n")
    meses.write("08 - Agosto\n")
    meses.write("09 - Setembro\n")
    meses.write("10 - Outubro\n")
    meses.write("11 - Novembro\n")
    meses.write("12 - Dezembro\n")

with open("meses.txt", "r") as meses:
    linhas = meses.readlines()
    del linhas[0]

with open("meses.txt", "w") as meses:
    for linha in linhas:
        meses.write(linha)

with open("meses.txt", "r") as meses:
    linhas = meses.readlines()
    print(linhas)
    print(linhas[0])

