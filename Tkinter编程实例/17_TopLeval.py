#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
## TopLevel �� Frame ���ƣ����������������ԣ�eg.title��
##-----------------------�����򵥵� TopLevel --------------------------------
#tl = Toplevel(root)
#Label(tl,text='hello label').pack()

##-----------------------���� TopLevel ������ --------------------------------
#tl.title('TopLevel')
#tl.geometry('400x300')

#-----------------------ʹ�� TopLevel �Լ�������ʾ�� --------------------------------
mbYes ,mbYesNo, mbYesNoCancel, mbYesNoAbort=0,1,2,3
def MessageBox(mbType):
	textShow='YesNo'
	print(mbType)
	if mbType == mbYes:
		textShow = 'Yes'
	if mbType == mbYesNo:
		textshow = 'YesNo'
	if mbType == mbYesNoCancel:
		textShow = 'YesNoCancel'
	if mbType == mbYesNoAbort:
		textShow = 'YesNoAbort'
	tl = Toplevel(root,height=200,width=400)
	Label(tl,text=textShow).pack()
cmd = mbYesNoAbort
Button(root,text='click me',command =lambda:MessageBox(cmd)).pack()



root.mainloop()