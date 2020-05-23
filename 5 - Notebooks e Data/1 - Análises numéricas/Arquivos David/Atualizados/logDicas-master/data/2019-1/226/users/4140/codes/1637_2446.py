senha=int(input())

sexto=senha%10;

segundo=(senha//10000)%10

quarto=(senha//100)%10

primeiro=senha//100000;

quinto=(senha%100)//10

terceiro=(senha//1000)%10

if (((sexto+segundo+quarto)%(primeiro+terceiro+quinto))==0):
	print("acesso liberado")
else:
	print("senha invalida")