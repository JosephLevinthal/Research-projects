numero=int(input("numero com quatro algarismo: "))
pri_algarismo=numero//1000
seg_algarismo=(numero%1000)//100
terc_algarismo=((numero%1000)%100)//10
quart_algarismo=(((numero%1000)%100)%10)
somatorio_algarismos= pri_algarismo+seg_algarismo+terc_algarismo+quart_algarismo
print(somatorio_algarismos)