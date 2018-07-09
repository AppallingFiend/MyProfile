import random
import sqlite3
import os
import operator
from tkinter import *
import tkinter.ttk as ttk

database="base.db"
profbase="profile.db"
global cur,cur2,n
cur2="1"
cur="class7a"
prof=sqlite3.connect(profbase)
cursor2=prof.cursor()
red=sqlite3.connect(database)
cursor=red.cursor()

def lenbase():
	count=cursor.execute("SELECT * FROM quations").fetchall()
	return len(count)
def right(r):
	zen=str(r)
	return cursor.execute('SELECT right_ans FROM quations WHERE id = ?',(zen,)).fetchall()
def wrong(r):
	zen=str(r)
	return cursor.execute('SELECT wrong_ans FROM quations WHERE id = ?',(zen,)).fetchall()
def quation(r):
	zen=str(r)
	return cursor.execute('SELECT quation FROM quations WHERE id = ?',(zen,)).fetchall()
def klass(cur):
	return cursor2.execute('SELECT id FROM  %s '%cur)

def scor():
	global score,cur2,cur
	print(cur2,cur)
	cursor2.execute('UPDATE %s SET SCORE = ? WHERE ID = ?'%cur,(score,cur2))
	prof.commit()
def shaf(a):
	fla=str(a)
	return cursor.execute('SELECT id FROM quations WHERE theam = ?',(fla)).fetchall()
def shaf2():
	return cursor.execute('SELECT theam FROM quations').fetchall()	
def zap(zap1):
	zap1=[]
	for i in range(len(b)):
		m=b[i][0]
		zap1.append(m)
	random.shuffle(zap1)
	return zap1
def error(cur):
	cursor2.execute('UPDATE '+cur+' SET FAILED = ? WHERE ID = ?',(str(masf),cur2))
	prof.commit()
def scoretable(cur):
	return cursor2.execute('SELECT ID,SCORE FROM '+cur+' ')
def on_exit():
	root.destroy()
def get_selected1(papram):
	global cur
	cur=clas(cur)
	print(combobox1.get())

def get_selected2(papram):
	global cur2
	cur2=combobox2.get()
	print(combobox2.get())
def table():
	global cur
	cur=clas(cur)
	klas=klass(cur).fetchall()
	lable44=Label(root,width=100,height=200,font="Arial 20")
	lable44.place(x=400,y=500)
	lable44.pack()
	mad=scoretable(cur)
	mad=sorted(mad, key=lambda mad: mad[1], reverse=True)
	print(mad)
	for i in range(len(klas)):
		lab="Компьютер номер "+str(mad[i][0])+" набрал "+str(mad[i][1])+"очков \n"
		lable44["text"]+=lab
def clas(cur):
	if combobox1.get()==list1[0]:
		cur="class7a"
	if combobox1.get()==list1[1]:
		cur="class7a1"
	if combobox1.get()==list1[2]:
		cur="class7b"
	if combobox1.get()==list1[3]:
		cur="class7b1"
	if combobox1.get()==list1[4]:
		cur="class7c"
	if combobox1.get()==list1[5]:
		cur="class7c1"
	if combobox1.get()==list1[6]:
		cur="class8a"
	if combobox1.get()==list1[7]:
		cur="class8a1"
	if combobox1.get()==list1[8]:
		cur="class8b"
	if combobox1.get()==list1[9]:
		cur="class8b1"
	if combobox1.get()==list1[10]:
		cur="class8c"
	if combobox1.get()==list1[11]:
		cur="class8c1"
	return cur
def ansver(ans):
	global wronge,score,masf,res
	if wronge[ans-1]==res:
		score+=1
	else:
		masf.append(masq[n])
def but1():
	global n
	n+=1
	ans=1
	ansver(ans)
	start()
def but2():
	global n
	n+=1
	ans=2
	ansver(ans)
	start()	
def but3():
	global n
	n+=1
	ans=3
	ansver(ans)
	start()
def but4():
	global n
	n+=1
	ans=4
	ansver(ans)
	start()
def but5():
	global n
	n+=1
	ans=5
	ansver(ans)
	start()
def helf():
	global wronge,score,masf,res,maskick,fl1
	ans=0
	maskick=[]
	for i in range(len(wronge)):
		if wronge[ans]==res:
			print(res)
		else:
			maskick.append(ans)
		ans+=1
	random.shuffle(maskick)
	print(maskick)
	fl1=1
	start()

fl1=0;fl2=0;fl3=0
def start():
	global n,res,wronge,masf,maskick,fl1,fl2,fl3
	qual=Label(root,text="Бла",width=1000,height=1000,font="Arial 20",fg='blue')
	qual.place(x=0,y=0)
	if n<countquat:
		flag=1
		quat=quation(masq[n])[0][0]
		wronge=wrong(masq[n])[0][0].split("#")
		res=right(masq[n])[0][0]
		wronge.append(res)
		random.shuffle(wronge)
		qual=Label(root,text="Бла",width=100,height=100)
		qual.place(x=200,y=100)
		qualab="Вопрос"+str(n+1)+": "+str(quat)
		txt=Text(root,width=70,height=5,font="13")
		txt.pack()
		txt.place(x=180,y=100)
		txt.insert(1.0,qualab)
		for i in range(len(wronge)):
			if i==0:
				buttans1=Button(root,text='СТАРТ',font='Arial 10',width=120,height=3,bg='white',fg='blue',command=but1)
				buttans1['text']=" %s "%wronge[i]
				buttans1.pack()
				buttans1.place(x=25,y=200)
			if i==1:
				buttans2=Button(root,text='СТАРТ',font='Arial 10',width=120,height=3,bg='white',fg='blue',command=but2)
				buttans2['text']=" %s "%wronge[i]
				buttans2.pack()
				buttans2.place(x=25,y=300)
			if i==2:
				buttans3=Button(root,text='СТАРТ',font='Arial 10',width=120,height=3,bg='white',fg='blue',command=but3)
				buttans3['text']=" %s "%wronge[i]
				buttans3.pack()
				buttans3.place(x=25,y=400)
			if i==3:
				buttans4=Button(root,text='СТАРТ',font='Arial 10',width=120,height=3,bg='white',fg='blue',command=but4)
				buttans4['text']=" %s "%wronge[i]
				buttans4.pack()
				buttans4.place(x=25,y=500)
			if i==4:
				buttans5=Button(root,text='СТАРТ',font='Arial 10',width=120,height=3,bg='white',fg='blue',command=but5)
				buttans5['text']=" %s "%wronge[i]
				buttans5.pack()
				buttans5.place(x=25,y=600)
			i+=1
	else:
		qualab=Label(root,text="Вот и все",font="Arial 20",fg='blue')
		qualab["text"]="Поздравляем, вы завершили тест на %s компьютере.\n Вы правильно ответили на %s вопроса(ов)"%(cur2,score)
		qualab.place(x=200,y=300)
		scor()
		error(cur)
		cursor.close()
		cursor2.close()
		red.close()
		prof.close()


#main

n=0;score=0;num=0;zap1=[];zap2=[];zap3=[];zap4=[];masq=[];countquat=12;masf=[];
count=lenbase()
root = Tk()
root.title('Знание Сила')
root.geometry("1024x720")
root.resizable(False,False)
lable1=Label(root,text='Выберите ваш класс и компьютер',font='Arial 20',fg='blue')
lable1.place(x=300, y = 100)
list1=["7A группа 1","7A группа 2","7Б группа 1","7Б группа 2","7В группа 1","7В группа 2","8A группа 1","8A группа 2","8Б группа 1","8Б группа 2","8В группа 1","8В группа 2"]
frame=Frame(root)
frame.place(x=350,y=150)
combobox1= ttk.Combobox(frame,values=list1,height=len(list1))
combobox1.set("Выбор Класса")
combobox1.grid(column=0,row=0)
button2=Button(root,text='СПИСОК ЛИДЕРОВ',font='Arial 20',width=20,height=1,bg='white',fg='blue',command=table)
button2.pack()
button2.place(x=350,y=250)
quitButton=Button(root,text='ВЫХОД',font='Arial 20',width=20,height=1,bg='white',fg='blue',command=root.quit)
quitButton.pack()
quitButton.place(x=350,y=310)
cur=clas(cur)
klas=klass(cur).fetchall()
frame=Frame(root)
frame.place(x=500,y=150)
combobox2 = ttk.Combobox(frame,values=klas,height=len(klas))
combobox2.set("Выбор компьютера")
combobox2.grid(column=0,row=0)
combobox2.bind("<<ComboboxSelected>>",get_selected2)
combobox1.bind("<<ComboboxSelected>>",get_selected1)
am=shaf2()
am=sorted(set(am))
i=0
flag=0
for i in range(len(am)):
	flag+=1
	b=shaf(flag)
	if flag==1:
		zap1=zap(zap1)
	if flag==2:
		zap2=zap(zap2)
	if flag==3:
		zap3=zap(zap3)
	if flag==4:
		zap4=zap(zap4)
zz=0
while i<count:
	flag=0
	while flag!=len(am):
		flag+=1
		i+=1
		if flag==1:
			masq.append(zap1[zz])
		if flag==2:
			masq.append(zap2[zz])
		if flag==3:
			masq.append(zap3[zz])
		if flag==4:
			masq.append(zap4[zz])
	zz+=1
button1=Button(root,text='СТАРТ',font='Arial 20',width=20,height=1,bg='white',fg='blue',command=start)
button1.pack()
button1.place(x=350,y=190)

root.mainloop()