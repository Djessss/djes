def fun(*mas):
    b = []
    for i in mas:
        c = ""
        while i != 0:
            c += "."
            i -= 1
        b.append(c)
    return b
print(fun(3,5,7,8))