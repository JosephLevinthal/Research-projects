A=int(input("a"))
B=int(input("b"))
pa=float(input("pa"))
pb=float(input("pb"))

ta=A
tb=B
ano=0

while(ta<tb):
	ta=ta+ta*(pa/100)
	tb=tb+tb*(pb/100)
	ano=ano+1
	
print(ano)
   	
	
