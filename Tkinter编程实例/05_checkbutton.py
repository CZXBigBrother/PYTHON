#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#-----------------CheckButton����ѡ��---------------------------------------------------------------------------------
#��ѡ��������״̬��on��off
#ÿѡһ��ʱ���ص�����������
def callCB():
	if sv.get()=='�ر�':
		sv.set('��')
	else:
		sv.set('�ر�')

sv = StringVar()
lb = Label(root,textvariable=sv,font='��Բ '+'-30'+' normal')
sv.set('�ر�')
lb.pack(side='left',anchor='nw')
cb = Checkbutton(root,text='python',command=callCB)
cb.pack(side='left',anchor='nw')

def callCheckButton():
	v.set('check Tkinter')
v = StringVar()
v.set('check python')
Checkbutton(root,text='check python',textvariable=v,command=callCheckButton).pack(anchor='w')

#-----------------��ʾCheckbutton��ֵ---------------------------------------------------------------------------------
sta = IntVar()
def callCButton():
	print(sta.get())

Checkbutton(root,variable=sta,text='checkbutton value',command=callCButton).pack(anchor='w')

#-----------------onvalue,offvalue---------------------------------------------------------------------------------
onoff = StringVar()
onoff.set(0)
def callonoff():
	print(onoff.get())

Checkbutton(root,variable = onoff, text = 'checkbutton value',
			onvalue='python',offvalue='tkinter',
			command=callonoff).pack()


mainloop()