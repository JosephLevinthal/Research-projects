k=int(input("numero de entrada: "))
w=0
for i in range(k):
	print(( k * ("*")) + ( 2 * w * ("o")) + (k *("*")) )
	k=k-1
	w=w+1