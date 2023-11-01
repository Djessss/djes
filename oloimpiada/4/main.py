a = int(input("люди"))+1
people=list(range(1,a))
kill = int(input("разброс"))
killer = kill -1
while len(people) !=1:
    if killer >= len(people):
        killer = killer % len(people)
    print(f"умер {people[killer]}")
    del people[killer]
    killer += kill -1
print(people)
