#!/usr/bin/python
#coding:gbk
# Scale Ϊ����޶���Χ���������䣬����Ϊָ֮�����ֵ����Сֵ������ֵ
from tkinter import *
root = Tk()
root.geometry('400x400')
#=====================����Scale�����飩=================================================
Scale(root).pack()
#Ĭ�����100����С0������1����ֱ����

#=====================���Ӳ���������Scale�����飩=========================================
Scale(root,
	  from_ = -500,
	  to = 500,
	  resolution = 5,	#����
	  orient = HORIZONTAL #ˮƽ����
	  ).pack()

#=====================Scale�󶨱���=====================================================
v1 = StringVar()
s = Scale(root,
	  orient = HORIZONTAL, #ˮƽ����
	  variable = v1
	  )
s.pack()
print(v1.get())
#v��ֵ��Scale��ֵһ��

#=====================Scale֮�¼�������=====================================================
#����ص�������һ�����������ֵ���ǵ�ǰScale��ֵ
def printScale(text):
	print('text = ',text)
	print('   v = ',v.get())
v = StringVar()
scale = Scale(root,
			  resolution = 0.0001,
			  orient = HORIZONTAL,
			  variable = v,
			  command = printScale
			  ).pack()
print(v.get())

#=====================����Scale��ʾλ��===================================================================
def printScale(text):
	print('text = ',text)
	print('   v = ',var.get())
var = StringVar()
scale = Scale(root,
			  resolution = 0.0001,
			  orient = HORIZONTAL,
			  digits = 9,	#λ�����������Ϊ׼���Ұ����������֣���Ϊ�����ֵ���λ����
			  variable = var,
			  command = printScale
			  ).pack(fill='x')
print(var.get())

#=====================����/ȡ��Scale��ֵ=====================================================
s2 = Scale(root,label='��ѡ��',font='���� -18',orient=HORIZONTAL)
s2.set(50)
print(s2.get())
s2.pack(fill='x')

s


mainloop()