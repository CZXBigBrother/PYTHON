#!/usr/bin/python
#encoding:gbk

from tkinter import *
root = Tk()

frame  = Frame(root,height=400,width=800,bg='red')
frame1 = Frame(root,height=400,width=800,bg='blue')
frame2 = Frame(root,height=400,width=800,bg='white')
frame.pack()
frame1.pack()
frame2.pack()
#---------------ָ����ť�Ŀ�Ⱥ͸߶�-------------------------------------------------------------------------------------
b1 = Button(frame,text = '30x1',width=30,height=1); b1.pack(side='left')
b2 = Button(frame,text = '30x2');b2['width']=30;b2['height']=2; b2.pack(side='left')
b3 = Button(frame,text = '30x3');b3.config(width=30,height=3); b3.pack(side='left')

#---------------����Button�ı��ڿؼ��ϵ���ʾλ��-------------------------------------------------------------------------------------
place = ['n','s','e','w','ne','nw','se','sw','center']
for i in place:
	Button(frame1,text=i,anchor=i,width=15,height=2).pack(side='left')

#---------------����Button��ǰ��ɫ�ͱ���ɫ-------------------------------------------------------------------------------------
bfg = Button(frame2,text='change foreground',fg='blue'); bfg.pack(side='left')
bbg = Button(frame2,text='change background',bg='blue'); bbg.pack(side='left')

#---------------����Button�ı߿���-------------------------------------------------------------------------------------
for b in range(0,5):
	Button(frame2,text=str(b),bd=b).pack(side='left')

#---------------����Button��״̬-------------------------------------------------------------------------------------
st = ['normal','active','disabled']
def statePrint():
	print('state')
for s in st:
	Button(frame2,text = s, state=s, width=30, command=statePrint).pack(side='left')

#---------------��Button�����������Button��textvariable����-------------------------------------------------------------------------------------
def changeText():
	if b['text']=='text':
		v.set('change')
		print('change')
	else:
		v.set('text')
		print('text')
v = StringVar()
b = Button(frame2,textvariable=v,command=changeText)
v.set('text')
b.pack()


root.mainloop()
