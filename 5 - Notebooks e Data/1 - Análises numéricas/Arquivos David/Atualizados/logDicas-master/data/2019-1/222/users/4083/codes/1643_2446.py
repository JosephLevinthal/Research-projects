senha = int(input("digite a senha: "))
c1 = (senha%1000)
c2 = c1//100
c3 = ((c1)-(c2*100))//10
c4 = (c1%10)

p = (senha - c1)//1000
p1 = p//100
p2 = ((p)- (p1*100))//10
p3 = p%10
pt = p1 + p3 + c3
ct = p2 + c2 + c4

if  (ct%pt == 0):
	  print("acesso liberado")
		
else:
	 print("senha invalida")





