#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#-----------------Radiobutton�ؼ�---------------------------------------------------------------------------------
#Radiobutton�ؼ�����ĸ�����������δָ���飬ÿ���ؼ��Գ�һ��
Radiobutton(root,text='python' ).pack()
Radiobutton(root,text='tkinter').pack()
Radiobutton(root,text='widget' ).pack()

#-----------------�����飬�󶨱���---------------------------------------------------------------------------------
v = IntVar()
v.set(1)
for i in range(3):
	Radiobutton(root,variable=v,text='python',value=i).pack()

#-----------------����������ͬ����---------------------------------------------------------------------------------
vLang = IntVar()
vOS = IntVar()
vLang.set(1)
vOS.set(2)

for var in [vLang,vOS]:
	for i in range(3):
		Radiobutton(root,variable=var,value=i,text='python'+str(i)).pack()

#-----------------RadioButton��indicatoron����Ĭ��Ϊ1----------------------------------------------------------------
idon = IntVar()
idon.set(1)
for i in range(3):
	Radiobutton(root,variable=idon,indicatoron=0,text = 'python & tkinter',value=i).pack()
#indicatoron=0ʱ���õ��ǰ�ť�İ��»�������ʾѡ��


mainloop()