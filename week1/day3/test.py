with open("db.txt","r+",encoding="utf-8") as f, open("db2.txt","w+",encoding="utf-8") as f2:
    r = f.read()
    # print(r)
    num = 0
    for line in r:
        if num <=5:
            f2.write(line)
            num +=1
        else:
            break