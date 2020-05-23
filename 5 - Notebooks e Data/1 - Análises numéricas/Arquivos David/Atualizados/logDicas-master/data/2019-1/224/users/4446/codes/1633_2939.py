quant_espet= float(input("quantidade de espetinhos vendidos ao dia:"))
lucro_do_espet= 12 * 0.83
valor= quant_espet * lucro_do_espet 
final= valor - 0.20 * valor - 100 


print(round(final , 2))