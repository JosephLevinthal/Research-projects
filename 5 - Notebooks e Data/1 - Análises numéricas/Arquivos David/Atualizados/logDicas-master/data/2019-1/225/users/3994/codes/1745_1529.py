gi=int(input("Qtd. guerreiros na infantaria: "))
gc=int(input("Qtd. guerreiros na cavalaria: "))
pi=float(input("Percentual na infantaria: "))
pc=float(input("Percentual na cavalaria: "))
t=0
c=0
while(t<50000):
	g=(gi*pi)/100
	gi=gi+g
	k=(gc*pc)/100
	gc=gc+k
	t=t+1
print(t)

