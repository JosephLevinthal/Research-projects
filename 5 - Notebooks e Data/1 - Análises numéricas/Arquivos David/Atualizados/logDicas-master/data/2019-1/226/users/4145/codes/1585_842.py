num = int(input("numero de quatro digitos "))
cal1 = num//1000
cal2 = num//100 - (cal1*10)
cal3 = num//10 - (num//100)*10
cal4 = num%cal3

print(cal1 + cal2 + cal3 + cal4)