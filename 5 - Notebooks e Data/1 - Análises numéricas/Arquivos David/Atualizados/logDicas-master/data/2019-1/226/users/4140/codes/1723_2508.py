n=int(input())
i=0
resultado=0
while(i<n-1):
	soma=((-1)**i)*4/((2+2*i)*(3+2*i)*(4+i*2))
	resultado=resultado+soma
	i=i+1
resultado=resultado+3
print(round(resultado,8))