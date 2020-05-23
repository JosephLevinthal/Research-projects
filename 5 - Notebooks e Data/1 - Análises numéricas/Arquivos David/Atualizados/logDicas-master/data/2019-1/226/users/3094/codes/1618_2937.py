numero_de_mols = float(input("numero_de_mols: "))
volume = float(input("volume: "))
temperatura = float(input("temperatura: 1"))
pressao = (numero_de_mols * 0.082057 * (temperatura + 273.1)) / volume
print(pressao)