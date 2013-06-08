#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()

def printReturn(event):
	print ('<Return>',event.keycode)
def printEvent(event):
	print ('<Key>',event.keycode)
root.bind('<Return>',printReturn)
root.bind('<Key>',printEvent)
# ������ΪReturn ʱ����printReturn ������,������������Ǹ��¼�����ʲô���������


## �� instance ������ printEvent ��
#bt1 = Button(root,text = 'instance event')
#bt1.bind('<Return>',printEvent)
## �� bt1 ��Toplevel ������ printToplevel ��
#bt1.winfo_toplevel().bind('<Return>',printToplevel)
## ��class ������¼�printClass
#root.bind_class('Button','<Return>',printClass)
## ��application all �����printAppAll
#bt1.bind_all('<Return>',printAppAll)
#bt1.focus_set()
#bt1.grid()
## Return ��߼�������ˡ�����",����˳��Ϊinstance/class/toplevel/all

# bind_class������������¼�����������Ӱ������������instance
# root.bind_class('Button','<Return>',printClass)
# �����е�Button ��Return �¼�������Ӧ��

def printProtocol():
	print('WM_DELETE_WINDOW')
	root.destroy()
# ʹ��protocol ��WM_DELETE_WINDOW ��printProtocol ��
root.protocol('WM_DELETE_WINDOW',printProtocol)
root.mainloop()
# �������˳�ʱ��ӡ'WM_DELETE_WINDOW'

root.mainloop()