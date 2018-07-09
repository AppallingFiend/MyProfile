import time
arr="АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
izk=" ,.!-123456789\|/@#$%^&?*()+='№[]IVX"
def fopen(f):
	m=f.readlines()
	z=""
	for i in range(len(m)):
		for y in range(len(m[i])):
			if m[i][y]=="\n":
				break
			z+=z.join(m[i][y])
	m=alf(z)
	return m

def alf(arrr):
	arrr=arrr.upper()
	arrlist = []
	for i in range(len(arrr)):
		arrlist.append(arrr[i])
		for j in range(len(izk)):
			if arrr[i] == izk[j]:
				arrlist.remove(arrr[i])
	arrr = arrlist
	return arrr
arr=alf(arr)
def alfshow(n):
    while n < len(arr):
        for i in arr:
            if i == arr[0]:
                print(end="|")
            print(i, end="|")
        arr.append(arr[0])
        arr.remove(arr[0])
        print()
        n += 1
alfshow(0)

def shif(m,k,arr):
	#print("Ключ:", "".join(k))
	#print("Текс:", "".join(m))
	c=[]
	for i in range(len(m)):
		for j in range(len(arr)):
			if arr[j]==m[i]:
				c.append(j)
	for i in range(len(c)):
		for j in range(len(arr)):
			if arr[j]==k[i]:
				c[i]=(c[i]+j)%len(arr)
	for i in range(len(c)):
		for j in range(len(arr)):
			if j==c[i]:
				c[i]=arr[j]

	#print("Шифровка:","".join(c))
	print("-----------------------------------")
	w = open('shif.txt', 'w')
	w.writelines(c)
	w.close()
	return c

def deshif(m,k,arr):
	#print("Ключ:","".join(k))
	#print("Текст:", "".join(m))
	c=[]
	for i in range(len(m)):
		for j in range(len(arr)):
			if arr[j]==m[i]:
				c.append(j)
	for i in range(len(m)):
		for j in range(len(arr)):
			if arr[j]==k[i]:
				c[i]=(c[i]-j)%len(arr)
	for i in range(len(c)):
		for j in range(len(arr)):
			if j==c[i]:
				c[i]=arr[j]
	#print("Дешифровка:","".join(c))
	print("-----------------------------------")
	w=open('deshif.txt','w')
	w.writelines(c)
	w.close()
	return c
start=time.time()
f=open('text.txt')
m=fopen(f)
f.close()
#m=input("Введите текст:")
#k=input("Введите Ключ:")
k = "ПРОГРАММИРОВАНИЕ ЭТО ЗАМЕЧАТЕЛЬНО"
k=alf(k)
print("Ключ:","".join(k))
k *= len(m) // len(k) + 1
print()
c=shif(m,k,arr)
c=deshif(c,k,arr)
print("Все выполнено")
print("Затраченое время %s секунд ---" %(time.time()-start))
time.sleep(60)