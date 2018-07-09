def che(text,stat):
    text=[]
    for x in range(len(stat)):
        for y in range(len(stat[x])):
            text+=stat[x][y]
    return text
def rev1(resh):
    bin = []
    k = []
    for i in resh:
        k += i
        if len(k) == 10:
            k.reverse()
            bin.append(k)
            k = []
    bin.reverse()
    return bin
def rev3(resh):
    bin = []
    k = []
    for i in resh:
        k += i
        if len(k) == 10:
            k.reverse()
            bin.append(k)
            k = []
    return bin
def rev2(resh):
    bin = []
    k = []
    for i in resh:
        k += i
        if len(k) == 10:
            k
            bin.append(k)
            k = []
    bin.reverse()
    return bin

def funct(stat,resh,i):
    for x in range(len(stat)):
        for y in range(len(stat[x])):
            if resh[x][y] == "1":
                if stat[x][y] =="0":
                    stat[x][y] = text[i]
                else:
                    stat[x][y] ="#ERROR#"
                    print("Где-то было перезаполненние")
                    break
                i += 1
    #print(stat)
    return stat

def deshif(stat,resh,i,tex):
    for x in range(len(stat)):
        for y in range(len(stat[x])):
            if resh[x][y] == "1":
                if stat[x][y] !="0":
                    tex += stat[x][y]
                    stat[x][y] = "0"
                    
                i += 1
    #print(stat)
    return stat

resh=[
    ["0","1","0","0","0","0","0","0","0","0"],
    ["1","0","0","0","1","0","1","1","0","0"],
    ["0","1","0","0","0","1","0","0","0","1"],
    ["0","0","0","1","0","0","0","1","0","0"],
    ["0","1","0","0","0","0","0","0","0","0"],
    ["0","0","1","0","0","1","1","0","0","1"]
]
stat=[
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0"]
]
def schet(i,resh):
    for x in range(len(resh)):
        for y in range(len(resh[x])):
            if resh[x][y] == "1":
                i+=1
    return i

def check(text,i):
    flag=0
    i=schet(i,resh)
    if len(text)== (4*i):
        print("Текст подходящего размера")
        flag=1
    elif len(text)>(4*i):
        print("Зашифруется только %d элементов из %d" %(i*4,len(text)))
        flag=1
    else:
        print("Текст слишком короткий еще необходимо добавить %d символ(-а)"%(4*i-len(text)))
    return flag
i =0
tex=[]
text="ШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИ"
text=list(text)
flag=check(text,i)
print("---------------------------------")
if flag==1:
    stat=funct(stat,resh,i)
    bin=rev1(resh)
    i=schet(i,resh)
    stat=funct(stat,bin,i)
    i=schet(i,resh)
    bin=rev2(resh)
    stat=funct(stat,bin,i)
    i=schet(i,resh)
    bin=rev3(resh)
    stat=funct(stat,bin,i)
    text=che(text,stat)
    print("Зашифрованное сообщение:","".join(text))
    print("---------------------------------")
    i=0
    stat=deshif(stat,resh,i,tex)
    bin=rev1(resh)
    i=schet(i,resh)
    stat=deshif(stat,bin,i,tex)
    i=schet(i,resh)
    bin=rev2(resh)
    stat=deshif(stat,bin,i,tex)
    i=schet(i,resh)
    bin=rev3(resh)
    stat=deshif(stat,bin,i,tex)
    print("Дешифрованное сообщейние:","".join(tex))
else:
    print("Исправьте размерность текста")