# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input('lado a: '))
b = float(input('lado b: '))
c = float(input('lado c: '))

print("Entradas:", a, ",", b, ",", c)
if a<=0 or b<=0 or c<=0 :
   print("Lados nulos ou negativos nao sao aceitos.")
   quit()
if a>=b+c or b>=c+a or c>=a+b :
   print("Tipo de triangulo: invalido")
   quit()

if a==b and b==c :
   print("Tipo de triangulo: equilatero")

elif a==b or b==c or c==a :
   print("Tipo de triangulo: isosceles")

else:
   print("Tipo de triangulo: escaleno")