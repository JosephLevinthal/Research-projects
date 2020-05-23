valor= int(input("qual valor a ser sacado? "))

cqnt= valor//50
restocqnt=valor%50

dez= restocqnt//10
restodez= restocqnt%10

dois= restodez//2

print(cqnt,dez,dois)