from numpy import*
m = array(eval(input()))
n = array(eval(input()))
i = j = k = 0
while i<len(m):
	if (m[i] == 33 and n[i] == 22) or (m[i] == 22 and n[i] == 11) or (m[i] == 11 and n[i] == 33):
		j+=1
	if (n[i] == 33 and m[i] == 22) or (n[i] == 22 and m[i] == 11) or (n[i] == 11 and m[i] == 33):
		k+=1
	i+=1

print(len(n))
if j>k:
	print("EUSAPIA")
elif k>j:
	print("BARSANULFO")
else:
	print("EMPATE")