x = str(input("Mais de oito mil:"))

n = ""
i = 0 
j = 3
c = 0
while(i != len(x)):
	a = x[i:j]
	n = n+a+'.'
	i = i + 3
	j = j + 3
	c = c + 3
print(n[:-1])