import time
def calculate_time(func):
    def walkot(a):
        tim = time.time()
        b = func(a)
        timee = time.time()
        return b ,timee - tim
    return walkot
@calculate_time
def some_function(a):
    spisok = []
    while not a == 0:
        spisok.append(a)
        spisok.sort()
        a -=1
    return spisok
chiclo = int(input("числом"))
aa,aaa = some_function(chiclo)
print(aa)
print(aaa)
"""
другой вариант
def calculate_time(func):
    def walkot(a):
        tim = time.time()
        b = func(a)
        timee = time.time()
        print(timee - tim)
        return b
    return walkot
@calculate_time
def some_function(a):
    spisok = list(range(1,a+1))
    print(spisok)
chiclo = int(input("числом"))
some_function(chiclo)"""