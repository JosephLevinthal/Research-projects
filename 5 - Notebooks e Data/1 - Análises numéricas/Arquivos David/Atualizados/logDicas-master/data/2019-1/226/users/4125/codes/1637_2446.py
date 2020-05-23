x = int(input("digite a senha: "))
x1 = x//100000
x2 = x//10000 - (x1) *10
x3 = x//1000 - (x//10000) * 10
x4 = x//100  - (x//1000) * 10 
x5 = x//10   - (x//100)  * 10
x6 = x       - (x//10)   * 10
if ((x2 + x4 + x6)%(x1 + x3 + x5) == 0):
	print("acesso liberado")
else:
	print("senha invalida")