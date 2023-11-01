kolbr = int(input("количество брусков"))
a = kolbr
c = 1
liswt = []

seet = []
while a != 0 :
    b = int(input(f"введите длину {c} бруска"))
    while b > 999 :
        print("длина больше тысячи")
        b = int(input(f"введите длину {c} бруска"))
    liswt.append(int(b))
    a -= 1
    c += 1
lisz = set(liswt)
for i in liswt:
    l = liswt.pop(0)
    for r in liswt:
        if r == l:
            seet.append(l)
            break
m = 1
while len(seet) != 0:
    m += 1
    sett = set(seet)
    for i in sett :
        seet.remove(i)
print("это максимальная высота")
print(m)
print("это минимальное количество башен")
print(len(lisz))