# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("digite x: "))
y = float(input("digite y: "))

if((x > 0) and (x < 0)):
	mensagem = "X"
elif((y > 0) and (y < 0)):
	mensagem = "Y"

print("Eixo" ,mensagem, )