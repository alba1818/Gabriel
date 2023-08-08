#Aula sobre dicionário

carros = {"Jeep Renegade": ['R$90.000,00', 2018],
          "Jeep Compass": 150000,
          "Troller": 80000}

print(carros)
print(carros["Troller"])
print(carros["Jeep Renegade"])

carros["Jeep Compass"]= 145000
print(carros)

carros["Jeep Renegade"][1] = 2016
print(carros)

del carros["Troller"]
print(carros)

carros["Audi A3"] = ['R$150.000,00', 2018, 'motor 2.0']
print(carros)

print("Audi A3" in carros)

