na=int(input("cidade a: "))
nb=int(input("cidade b: "))
pa=float(input("percentual a: "))/100
pb=float(input("percentual b: "))/100
t=0
while(na<=nb):
	na=na+(na*pa)
	nb=nb+(nb*pb)
	t=t+1
print(t)
	