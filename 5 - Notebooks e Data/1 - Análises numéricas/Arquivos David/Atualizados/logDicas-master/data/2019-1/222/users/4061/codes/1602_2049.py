# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

#var int dividendo
#var int divisor
#var int quociente
#var int resto
#var = int(input("texto para o usuario: "))
#gerar input de dividendo e divisor
#calcular quociente e resto
#mostrar todas as variaveis
dividendo = int(input("Digite o valor do dividendo: ")) #dividendo = int("10") -> dividendo = 10 -> 10 é um número agora
divisor = int(input("Digite o valor do divisor: ")) #divisor = int("2") -> divisor = 2 -> 2 é um número agora
quociente = dividendo // divisor #quociente = 10/2 -> quociente = 5 -> 5 ainda é um número
resto = dividendo % divisor #resto = 10%2 -> resto = 0 -> não há resto, e 0 ainda é número
#para imprimir, transformar todos os números em texto, se for preciso -> str(dividendo) ou só o print(dividendo)
print(dividendo)
print(divisor)
print(quociente)
print(resto)