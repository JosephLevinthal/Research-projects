# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a = float(input())
b = float(input())
c = float(input())
d = float(input())


if b>a and d>c:
    if d>=a and d <=b or b>=c and b<=d:
        print("Intervalo 1:", a, ",", b , "\n", "Intervalo 2:", c, ",", d , "\n", "Ha intersecao")
    else:
        print("Intervalo 1:", a, ",", b, "\n", "Intervalo 2:", c, ",", d, "\n", "Nao ha intersecao")
else:
    print("Intervalo 1:", a, ",", b, "\n", "Intervalo 2:", c, ",", d, "\n", "Entradas invalidas")