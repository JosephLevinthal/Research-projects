numero_de_habitantes_a=int(input("digite o numero de habitantes da cidade A: "))
numero_de_habitantes_b=int(input("digite o numero de habitantes da cidade B: "))
percentual_do_crescimento_de_habitantes_na_cidade_a=float(input("percentual de crescimento populacional da cidade A: "))
percentual_do_crescimento_de_habitantes_na_cidade_b=float(input("percentual de crescimento populacional da cidade B: "))
laco=0
while(numero_de_habitantes_a<numero_de_habitantes_b):
	pessoas_a=numero_de_habitantes_a*(percentual_do_crescimento_de_habitantes_na_cidade_a/100)
	numero_de_habitantes_a= numero_de_habitantes_a+pessoas_a
	pessoas_b=numero_de_habitantes_b*(percentual_do_crescimento_de_habitantes_na_cidade_b/100)
	numero_de_habitantes_b= numero_de_habitantes_b+pessoas_b
	laco=laco+1
print(laco)