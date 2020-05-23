x=int(input("Digite um numero: "))
h=0
t=1
for i in range(1,x+1):
	h=h-((1/i)*t)
	t=-t
print("H =",round(abs(h),6))