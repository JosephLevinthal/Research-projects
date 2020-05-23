#Número de habitantes de uma cidade A
n_hab_a = int(input('Digite o numero de habitantes da Cidade A:   '))

#Número de habitantes de uma cidade B
n_hab_b = int(input('Digite o numero de habitantes da Cidade B:   '))

#Percentual de crescimento populacional da cidade A
taxa_a = float(input('taxa de crescimento da Cidade B:  '))

#Percentual de crescimento populacional da cidade B
taxa_b = float(input('taxa de crescimento da Cidade B:  '))

percentual_a = taxa_a / 100
percentual_b = taxa_b / 100
t=0

# A população da cidade A é menor que a população da cidade B

while(n_hab_a < n_hab_b):
	acrescimo_a = n_hab_a * percentual_a 
	acrescimo_b = n_hab_b * percentual_b
	n_hab_a = n_hab_a + acrescimo_a
	n_hab_b = n_hab_b + acrescimo_b
	
	t=t+1

print(t)
