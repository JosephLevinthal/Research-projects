# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
import math as m
raio = float(input("raio do tanque: "))
h_ar = float(input("altura da coluna: "))
option = input("Numero da opcao desejada\n1 - volume de ar\t2 - volume de combustivel: ")

V_esfera = (4/3)*m.pi*raio**3
V_ar		= (1/3)*m.pi*h_ar**2*(3*raio - h_ar)
V_combus = V_esfera - V_ar

if option == '1':
	print(round(V_ar, 4))
elif option == '2':
	print(round(V_combus, 4))