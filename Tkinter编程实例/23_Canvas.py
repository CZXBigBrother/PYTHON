#!/usr/bin/python
#coding:gbk

from tkinter import *
root = Tk()
fm = Frame(root)
fm.pack()
cv = Canvas(root,bg='white')
#---------------------�ƶ� item ---------------------------------------------
rt1 = cv.create_rectangle(150,40,250,140,tags=('r1','r2','r3'),width=10,outline='lightblue')
rt2 = cv.create_rectangle(10,10,110,140,tags=('s1','s2','s3'))
def move():
	cv.move(rt1,1,0) #ע�������λ����˿���Ϊ��ֵ
Button(fm,text='move',command=move).pack(side='left')

#---------------------ɾ�� item ---------------------------------------------
def delete1():
	'''ʹ��idɾ��rt1'''
	cv.delete(rt1)
def delete2():
	'''ʹ�� tag ɾ�� rt2'''
	cv.delete('s1')
Button(fm,text='del ID',command=delete1).pack(side='left')
Button(fm,text='del tag',command=delete2).pack(side='left')

#---------------------���� item ---------------------------------------------
# scale: ���㹫ʽ (coords-offset)*scale+offset
#����Ĺ�ʽ���ʹ�ã���û����ԭ��
def zoom_in(): #�Ŵ�
	cv.scale(rt3,1,2,2,2)
def zoom_out(): #��С
	cv.scale(rt3,0,0,0.5,0.5)
rt3 = cv.create_rectangle(2,2,3,3,fill='blue')
cv.lower(rt3)
Button(fm,text='�Ŵ�',command=zoom_in).pack(side='left')
Button(fm,text='��С',command=zoom_out).pack(side='left')

#---------------------�� item �� event ---------------------------------------------
def change_color(event):
	cv.itemconfig('r1',fill='red')
def change_color1(event):
	cv.itemconfig('r1',fill='springgreen')
cv.tag_bind('r1','<Button-1>',change_color)
cv.tag_bind('r1','<Button-3>',change_color1)
# ֻ�е�������εı߿�ʱ�Żᴥ���¼�
cv.create_line(10,200,100,200,width = 15,tags = 'r1')

cv.pack()
mainloop()