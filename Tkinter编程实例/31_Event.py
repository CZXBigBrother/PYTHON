#!/usr/bin/python
#coding:gbk

from tkinter import *
root = Tk()
def printCoords(event):
	print(event.x,event.y)

#----------------------����뿪��Leave��ʱ�¼�--------------------------------
#bt1 = Button(root,text='leftmost button')
#bt1.bind('<Leave>',printCoords)
#bt1.grid()

#----------------------��Ӧ�������Special Key��--------------------------------
#def printSK(event):
#	print('   event.char = ',event.char)
#	print('event.keycode = ',event.keycode)
#bt2 = Button(root,text='Press BackSpace')
#bt2.bind('<BackSpace>',printSK)
#bt2.grid()

#----------------------��Ӧ���еİ���(key)�¼�--------------------------------
ms = Message(root,text='�밴��',font='΢���ź� 18',relief='solid',width=400)
def printAllKey(event):
	ms.config(text='char:'+event.char+'\tkeycode:'+str(event.keycode))

bt = Button(root,text='All Key')
bt.bind('<Key>',printAllKey)
ms.grid()
bt.grid()
bt.focus()

# һ��İ���ֱ��ʹ�þͿ����ˣ�������д'key',����'<key>'; �磺'a','A'
# ����������Ҫ�ر�ע��:�ո���С�ڵĴ���ʹ�÷�ʽΪ'<space>��<less>


#----------------------��Ӧ��ϰ����¼�--------------------------------
#<Shift-Up>
#<Ctrl-Up>
#<Ctrl-Shift>
#<Ctrl-Alt-a>
#����ʹ�� <Ctrl-Alt>

# configure���ı������С�¼�
# ������Ĵ�С�ı�ʱ������evnet.width/height �ֱ𷵻ظı��Ŀ�Ⱥ͸߶ȡ�
def printSize(event):
	print (event.width,event.height)
root.bind('<Configure>',printSize)
#----------------------�ı������С�¼�--------------------------------
# ��������佹����л�����ʹ��TAB ����
# ����� 
#Cancel
#Break
#BackSpace
#Tab
#Return
#Sift_L
#Shift_R
#Control_L
#Control_R
#Alt_L
#Alt_R
#Pause
#Caps_Loack
#Escape
#Prior(Page Up)
#Next(PageDown)
#End
#Home
#Left
#Up
#Right
#Down
#Print
#Insert
#Delete

# F1-12
#Num_Lock
#Scroll_Lock

# ��Щ����char �ǲ��ɴ�ӡ�ģ�����ʹ��event.keycode �鿴��



root.mainloop()