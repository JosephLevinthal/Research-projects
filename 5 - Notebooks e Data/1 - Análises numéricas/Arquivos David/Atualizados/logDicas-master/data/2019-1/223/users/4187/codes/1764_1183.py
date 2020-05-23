from numpy import* 
vet = array(eval(input("vet:")))
i = 0
tamanho = size(vet)
Numeros_Posit = 0
while(i < tamanho):
	if(vet[i] > 0):
		Numeros_Posit =  Numeros_Posit + 1
	i = i + 1
novo_vet = zeros(Numeros_Posit, dtype=int)
i = 0
i2 = 0
while(i < size(vet)):
	if(vet[i] > 0):
		novo_vet[i2] = vet[i]
		i2 = i2 + 1
	i = i+ 1
print(novo_vet)
		
		