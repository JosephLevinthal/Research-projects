from numpy import*
n = input("digite um numero multiplo de tres ou tres: ")
i = 0
k = 3
msg = ""
while(i< len(n)):
	if( i == len(n)-3):
		msg = msg +n[i:k]
		i = i + 3
		k = k + 3
	else:
		msg = msg + n[i:k] + "."
		i = i + 3
		k = k + 3
print(msg)