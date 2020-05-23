s=int(input("digite a senha: "))
#primeiro numero
a=s//100000
#segundo numero
b=s//10000
c=b%10
#terceiro numero
d=s//1000
e=d%10
#quarto numero
f=s//100
g=f%10
#quinto numero
h=s//10
i=h%10
#sexto numero
j=s%10

sx=c+g+j
sy=a+e+i
m=sx%sy
if(m==0):
	men="acesso liberado"
else:
	men="senha invalida"
print(men)
