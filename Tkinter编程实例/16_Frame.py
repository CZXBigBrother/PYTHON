#!/usr/bin/python
#encoding:gbk

from tkinter import *
root = Tk()
# Frame ������Ļ�ϵ�һ���������һ��������������container�������ִ���

##------------------���� Frame ------------------------------
import mycolor
colorDB = mycolor.get_color()
#for color in colorDB[:20]:
#	Frame(height=20,width=400,bg=color).pack()

##------------------���� Frame �����������Widget ------------------------------
#fm = []
#for color in ['red','blue','green']:
#	fm.append(Frame(height=200,width=400,bg=color))
#Label(fm[0],text = 'Hello Color Lebal').pack()
##Label(fm[1],text = 'Hello Color Lebal').pack()
##Label(fm[2],text = 'Hello Color Lebal').pack()
#fm[0].pack()
#fm[1].pack()
#fm[2].pack()
##Ҫ��ӱ�ǩ�������� fm.pack()֮ǰ��ӣ�������Ӳ���ȥ

##------------------ LabelFrame �����Title��֧�� ------------------------------
for color in colorDB[90:100]:
	lf = LabelFrame(height=40,width=300,text=color,bg=color)
	lf.pack(fill='both')





mainloop()
