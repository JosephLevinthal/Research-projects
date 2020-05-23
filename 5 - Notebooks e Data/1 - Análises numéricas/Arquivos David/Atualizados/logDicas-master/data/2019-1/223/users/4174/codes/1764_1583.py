from numpy import*
n = input("numero:")
i = 0 
j = 3
p = "."
t = ""
while(i < len(n)):
	if(i < (len(n)-4)):
		t = t + n[i:j] + p
	else:
		t = t + n[i:j]
	i = i + 3
	j = j + 3
print(t)