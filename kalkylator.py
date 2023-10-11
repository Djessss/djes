a=int(input('введите первое число'))
b=input('введите знак чмсло')
c=int(input('введите второе число'))
if type(c) or type(a) != int:
    print('invalid syntax')
if b=="*"  :
    print(a * c)
elif b=="+" :
    print(a + c)
elif b=="-" :
    print(a - c)
elif b == "/" and c != 0:
    print(a / c)
elif b=="/" and c ==0:
    print("Э на ноль нельзя делить")
else:
    print('invalid syntax')
input()





#замена переменных
#a = 5
#b = 7
#c = a
#a = b
#b = a