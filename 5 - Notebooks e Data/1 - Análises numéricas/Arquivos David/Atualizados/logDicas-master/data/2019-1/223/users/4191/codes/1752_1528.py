dano=int(input("Dano dos guerreiros: "))
pv=int(input("Pontos de vida do troll: "))
cura=int(input("Cura do troll: "))

cont=0
pv1=pv

while(pv1>0):
	pv1=pv1+cura-dano*5
	cont=cont+1
print(cont)	