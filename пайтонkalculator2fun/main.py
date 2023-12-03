def plus(aa,ba) :
    return  aa + ba
def minus(aa,ba) :
    return  aa - ba
def dele(aa,ba) :
    if ba == 0:
        return " I remember that it is impossible to divide by 0"
    else:
        return  aa / ba
def ymnohenie(aa,ba) :
    return  aa * ba
while True:
    a = int(input("первое число"))
    b = input("знак")
    c = int(input("второе число"))
    if b == "+":
        print(plus(a,c))
    if b == "-":
        print(minus(a,c))
    if b == "/":
        print(dele(a,c))
    if b == "*":
        print(ymnohenie(a,c))