#!/usr/bin/python
#coding:gbk

from tkinter import *
root = Tk()
#-----------------------�����ʹ��----------------------------------------------------------
for ft in ('Arial',('Courier New',),('Comic Sans MS',),'Fixdsys',('MS Sans Serif',),('MS Serif',),'Symbol','System',('Times New Roman',),'Verdana'):
	Label(root,text='hello World',font=ft).grid()
# ��Windows �ϲ���������ʾ��ע�������а����пո���������Ʊ���ָ��Ϊ tuple ���͡�

#-----------------------ʹ��ϵͳ��������----------------------------------------------------------
# Font: ָ����������
# family��ָ����������
# size��ָ�������С
# wight����ʽ
from tkinter.font import *
ft = Font(family = '΢���ź�',size = 20,weight = BOLD)
Label(root,text = 'hello sticky',font = ft ).grid()

for ft in ('ansi','ansifixed','device','oemfixed','system','systemfixed'):
	Label(root,text = 'hello font',font = ft ).grid()
for ft in ('Times','Helvetica','Courier','Symbol',):
	Label(root,text = 'hello font',font = ('-*-%s-*-*-*--*-240-*')%(ft)).grid()
root.mainloop()










###��ȡϵͳ����ĳ����
#import os
#import glob
#os.chdir(r'c:\windows\fonts')
#name = glob.glob('*.*')
#name = name[::]
#fonts = []
#for i in range(len(name)):
#	(shortname,ext)=os.path.splitext(name[i])
#	fonts.append(shortname)
#print(fonts)
#r,col = 0,0
#for font in fonts:
#	Label(root,text='M',font=font).grid(row=r,column=col)
#	col = col + 1
#	if col%80==0:
#		r = r + 1
#		col = 0