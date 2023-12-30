with open("account.txt","r") as file:
    fil = open('login.txt', 'w')
    fil.write("")
    fil.close()
    for line in file:
        res_line = line.split(":")
        login = res_line[0] + ":" + res_line[1]
        with open("login.txt","a") as file1:
            file1.write(login + "\n")
