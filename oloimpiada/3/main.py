a = input("число")

d = []
for i in a:
    d.append(i)
k = True
b = 1
while b <= len(a):
    c = 9
    while c != 0 and k == True:
        if int(d[0]) < c :
            h = a[:b-1] + str(c) + a[b:]
            if int(h) % 3 == 0:
                print(h)
                k = False
        c -= 1
    b +=1
