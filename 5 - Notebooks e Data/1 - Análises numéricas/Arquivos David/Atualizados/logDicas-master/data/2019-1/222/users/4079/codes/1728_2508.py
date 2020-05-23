num=int(input("numero de aproximidades: "))

cont= 1

ap= 3

while(cont < num):
	may= (cont*2) * (cont*2+1) * (cont*2+2)
	
	ap= ap + (-1)**(cont+1)*4 / may
	
	cont= cont + 1
	print(round(ap,8))