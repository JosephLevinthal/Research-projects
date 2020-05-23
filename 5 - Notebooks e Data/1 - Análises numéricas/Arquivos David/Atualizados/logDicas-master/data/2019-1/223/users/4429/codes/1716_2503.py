num=int(input("digite um numero: "))
contadora=1
apr=4

while(contadora<num):
	denominador=(contadora+2)
	apr=apr+(-1)**(contadora)*4/denominador
	
	contadora=contadora+1
	
print(round(apr, 8))