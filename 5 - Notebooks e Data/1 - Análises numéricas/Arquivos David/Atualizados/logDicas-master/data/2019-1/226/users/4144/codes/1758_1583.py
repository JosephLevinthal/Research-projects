a = input("digite os numeros: ")
i = 0
k = 3
men = ""
while(i<len(a)):
	if(i==len(a)-3):
		men = men + a[i:k]
		i = i +3
		k = k +3
	else:
		men = men + a[i:k] + "."
		i = i+3
		k = k+3
print(men)