import math as m

inicial_HP = int(input("Pontos de vida inicial?"))
D1 = int(input("Qual o valor sorteado no primeiro dado?"))
D2 = int(input("Qual o valor sorteado do segundo dado?"))
dano = m.sqrt(5*D1)+(m.pi**(D2/3))
atual_HP = inicial_HP - dano
print(int(atual_HP+1))