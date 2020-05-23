# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a=input("qual a resposta:")
b=input("qual a resposta:")
c=input("qual a resposta:")
d=input("gabarito:")
e=input("gabarito:")
f=input("gabarito:")
if((a==d) and (b==e) and (c==f)):
	print(3)
elif(((b==e)and(c==f))or((a==d)and(b==e))or((a==d)and(c==f))):
	print(2)
elif(((a!=d)and(b!=e)and(c==f)) or ((a==d)and(b!=e)and(c!=f)) or((a!=d)and(b==e)and(c!=f))):
	print(1)
else:
	print(0)