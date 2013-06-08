#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#root.geometry('400x300')
#---------------Button �������ܴ����¼�-----------------------------------------------------------------------------------------------------------------
def Hello():
	print('Hello World')
Button(root,text = 'SayHello',command=Hello).pack()

#---------------Button relief���ԣ����-----------------------------------------------------------------------------------------------------------------
X=[RAISED, SUNKEN,GROOVE ,RIDGE,FLAT,SOLID]
for key in X:
	Button(root,text = '%s'%key,relief = key).pack(side='left',expand=1)

#---------------Button ��ʾͼ����ı�-----------------------------------------------------------------------------------------------------------------
pic = PhotoImage(file=r'C:\temp\ButtonQuit.gif')
Button(root,text='��ť',image=pic,compound='left').pack(side = 'left')

#---------------�ؼ���������-----------------------------------------------------------------------------------------------------------------
def cb1():print('button1 clicked')
def cb2(event):print('button2 clicked')
def cb3():print('button3 clicked')
b1 = Button(root,text='button1',command=cb1)
b2 = Button(root,text='button2',command=cb1)
b2.bind('<Return>',cb2)
b3 = Button(root,text='button3',command=cb1)
b1.pack(side='left');b2.pack(side='left');b3.pack(side='left')
b2.focus_set()

#---------------�¼���Ϣ-----------------------------------------------------------------------------------------------------------------
def printEvenInfo(event):
	print('event.time = ',event.time)
	print('event.type = ',event.type)
	print('event.WidgetId = ',event.widget)
	print('event.KeySymbol = ',event.keysym)
	print('event.time = ',event.time)
b = Button(root,text='Information')
##���س���ʱ����ӡ�¼���Ϣ
##<Enter>����ʾ��������ʱ��ӡ��Ϣ
b.bind('<Return>',printEvenInfo)
b.pack()
##��λ����ť b����ʱ���س���Ч
#b.focus_set()

mainloop()
