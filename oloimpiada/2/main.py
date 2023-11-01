list=[]
a = int(input("количество инопланетян"))
b = 0
while a >= b:
    b += 1
    c = int(input(f"вес {b} инопланетянина "))
    list.append(c)

print(f"минимальный вес {min(list)} у {list.index(min(list))+1} инопланетянина")
print(f"максимальный вес {max(list)} у {list.index(max(list))+1} инопланетянина")