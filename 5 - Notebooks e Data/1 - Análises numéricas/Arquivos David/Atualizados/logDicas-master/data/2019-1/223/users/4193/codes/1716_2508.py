num=int(input("digite um numero: "))

contadora=1

apr=3

while(contadora<num):
    denominador=(contadora*2)*(contadora*2+1)*(contadora*2+2)
    apr=apr+(-1)**(contadora+1)*4/denominador
   
    contadora=contadora+1
   
print(round(apr, 8))