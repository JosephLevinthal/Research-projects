string = input("s: ")
vogal = ['a','e','i','o','u']
qtd = [0,0,0,0,0]

for i in string:
	if i == 'a':
		qtd[0]+=1
	if i == 'e':
		qtd[1]+=1
	if i == 'i':
		qtd[2]+=1
	if i == 'o':
		qtd[3]+=1
	if i == 'u':
		qtd[4]+=1

for i in range(len(vogal)):
	print(vogal[i]+":", qtd[i])