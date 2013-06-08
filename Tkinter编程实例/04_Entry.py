#!/usr/bin/python
#coding:gbk
from tkinter import *

root = Tk()
root.geometry('200x200')
#---------------��Entry�����뵥���ı�-------------------------------------------------------------------------------------
Entry(root,text='input your text here',bg='peach puff').pack()
#˵����Entry��text��Button��Label��text��ͬ
#     ��������ʾ�ı�

#---------------Entry���趨��ʼֵ��ʹ��textvariable��������Entry��-------------------------------------------------------------------------------------
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('init value')
entry.pack()

#---------------Entry���趨ֻ��-------------------------------------------------------------------------------------
e1 = StringVar()
st = ['normal','disabled','readonly']
for s in st:
	entry1 = Entry(root,textvariable=e1,state=s)
	e1.set('input your text here')
	entry1.pack()

#---------------����Ϊ���������-------------------------------------------------------------------------------------
e2 = StringVar()
entry2 = Entry(root,textvariable = e2)
e2.set('password')
entry2.pack()
entry2.configure(show='*')

#---------------��֤����������Ƿ����Ҫ��-------------------------------------------------------------------------------------
#e3 = StringVar()
#def validateText(contents):
#	print(contents)
#	return contents.isanum()

#entry3 = Entry(root, validate = 'key', textvariable = e3, validatecommand = validateText)
#entry3.pack()

#---------------������������-------------------------------------------------------------------------------------
def gtc(even=None):
	key = ent.get()
	sv.set('['+key+']')
	print(key)
sv = StringVar()
ent = Entry(root,textvariable=sv)
ent.bind('<Return>',gtc)
ent.pack()

but = Button(root,text='������',command=gtc)
but.pack()



mainloop()
