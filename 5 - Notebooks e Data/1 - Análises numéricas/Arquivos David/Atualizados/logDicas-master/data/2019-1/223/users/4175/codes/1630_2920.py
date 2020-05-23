g = float(input("quantos kg possui seu prato: "))
b = int(input("quantas bebidas voce pegou: "))
s = int(input("quantas sobremesas voce pegou: "))

kg = g/1000

sf = 26.90
sc = 3.50
sb = 3

sft = sf*kg
sct = sc*b
sbt = sb*s

T = sft + sct + sbt
print(round(T,2))