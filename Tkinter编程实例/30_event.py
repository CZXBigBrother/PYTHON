#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#---------------------------���������(Click)�¼� ---------------------------------------
#<Button-1>
def printCoords(event):
	print(event.x,event.y) # �õ���������ֵ
bt1 = Button(root,text='ClickMe')
bt1.bind('<Button-2>',printCoords)
bt1.grid()

#---------------------------��������ƶ�(Motion)�¼� ---------------------------------------
# ����갴�º��ƶ����������¼�
# <Bx-Motion>  x=1,2,3�ֱ��ʾ���У���������
bt2 = Button(root,text='leftmost button')
bt2.bind('<B1-Motion>',printCoords)
bt3 = Button(root,text='middle button')
bt3.bind('<B2-Motion>',printCoords)
bt4 = Button(root,text='rightmost button')
bt4.bind('<B3-Motion>',printCoords)
bt1.config(width=40)
bt2.config(width=40)
bt3.config(width=40)
bt4.config(width=40)

bt2.grid()
bt3.grid()
bt4.grid()
root.columnconfigure(0,minsize=200)

#---------------------------��������ͷ�(Release)�¼� ---------------------------------------
#<ButtonRelease-x>  x=1,2,3
def printCoord(event):
	print(event.x,event.y)
bt5 = Button(root,text = 'leftmost button')
bt5.bind('<ButtonRelease-1>',printCoord)
bt5.grid()

#---------------------------����(Enter)�¼�---------------------------------------
bt1.bind('<Enter>',printCoords) #������ʱ
bt1.focus() #����Ϊ����
bt1.bind('<Return>',printCoords)  #���س�ʱ

root.mainloop()
