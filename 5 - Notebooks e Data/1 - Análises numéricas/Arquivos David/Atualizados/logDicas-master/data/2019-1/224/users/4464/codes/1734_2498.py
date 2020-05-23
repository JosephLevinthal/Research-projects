HabA = int(input("Digite o numero de habitantes Cidade A: "))
HabB = int(input("Digite o numero de habitantes Cidade B: "))
percA = float(input("digite percentual de crescimento da cidade A: "))
percB= float(input("digite percentual de crescimento da cidade B: "))

anos = 0
A = HabA
B = HabB

while (A < B):
	if (HabA < HabB):
		A = A +((A*percA)/100)
		B = B+((B*percB)/100)
		anos = anos + 1
	
print(anos)
	
