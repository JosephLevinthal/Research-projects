mols = int(input("Numero de mols: "))
vol = float(input("Volume: "))
temp = float(input("Temperatura: "))

kelvin = temp + 273.1
R = 0.082057

p = (mols*R*kelvin)/vol
print(p)