def bank(a,b,c):
    while b !=0 :
        a += a*c*0.01
        b -=1
    return a
K =int(input("сумма"))
N =int(input("года"))
L =int(input("годовые проценты "))
print(bank(K,N,L))
