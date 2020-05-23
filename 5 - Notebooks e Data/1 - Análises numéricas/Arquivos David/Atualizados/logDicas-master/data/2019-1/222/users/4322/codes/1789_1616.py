from numpy import*
gelo = 2
fogo = 3
choque = 4
conjuracao = 8
ilusao = 10
i = 0
dano_do_mago = dano_da_magia * nivel_do_mago
magia = array(eval(input("Qual o tipo de magia? ").upper()))
nivel = array(eval(input("Qual o tipo de nivel? "))
while(size(magia) > i):
	print(sum(magia[i] * nivel[i]))
	i = i + 1