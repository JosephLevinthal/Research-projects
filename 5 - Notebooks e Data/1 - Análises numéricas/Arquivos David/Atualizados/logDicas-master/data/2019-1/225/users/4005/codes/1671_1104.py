# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a=float(input())
b=float(input())
c=float(input())
d=float(input())
if not((b>a)and(c<d)):
	z="Entradas invalidas"
elif((a<c)and(b>d))or((a>c)and(b<d))or((a==c)and(b==d)):
	z="Ha intersecao"
else:
	z="Nao ha intersecao"
print("Intervalo 1:",a,",",b)
print("Intervalo 2:",c,",",d)
print(z)