#Протокол Деффи-Хелмана
import random
def chif(p,g):
	z=int(input("Введите количество участников чата"))
	print("Изначально всем участникам извстны следующее числа p = %d и g = %d"%(p,g))
	priv=[]
	print("Каждая сторона выберает свое уникальное число")
	for i in range(z):
		e=random.randint(1,p-1)
		priv.append(e)
	print(priv)
	print("Все игроки поделились своеми публичными ключами, теперь на основе полученых ключей они расчитают")
	outzn=[]
	for i in range(z):
		b=g
		for j in range(z):
			if i==j:
				None
			else:
				b=b**priv[j]%p
		outzn.append(b)
		print("Учистник %d выбрал параметр %d и после того как расчитали получили участник %d получил следующее число %d"%(i+1,priv[i],i+1,b))
	print(outzn)
	print("Теперь каждый считает ключ который должен быть у всех одинаковый")
	rez=[]
	for i in range(z):
		pp=(outzn[i]**priv[i])%p
		rez.append(pp)
	print(rez)

p=3011
g=random.randint(1,p-1)
chif(p,g)

