from numpy import*
a = array(eval(input("vetor 1: ")))
b = array(eval(input("vetor 2: ")))
n = size(a)
print(n)
t = 0
a1 = 0
b1 = 0
while t<n:
	if (a[t]- b[t] == 11) or (a[t]-b[t]== -22):
		a1 = a1 + 1
	elif (b[t] - a[t]==11) or (b[t]-a[t]== -22):
		b1 = b1 + 1
	t = t + 1
if (a1>b1):
	print("EUSAPIA")
elif (b1>a1):
	print("BARSANULFO")
elif (b1 == a1):
	print("EMPATE")