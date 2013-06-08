#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
t = Text(root,height=50)
#-------------------------�Զ��� tag ��������������--------------------------
t.tag_config('b',foreground='skyblue')
for i in range(10):
	t.insert(1.0,'0123456789\n')
t.mark_set('ab','3.1')
t.mark_set('cd',END)
t.tag_add('b','ab','cd')
# ��tag('b')֮ǰ����'first'
t.insert('b.first','first\n')
# ��tag('b')֮�����'last'
t.insert('b.last','last\n')
# ע�⣺first û��ʹ��tag('b')���ԣ�last ʹ����tag('b')����
	##��� mark: 'cd' ���� END������last��Ҳ����ʹ�� tag('b')�����ԡ�

#-------------------------�� Text �д�����ť����һ����������---------------------------------
def printbt():
	t.insert('2.0','button in text')
bt = Button(t,text='button',command=printbt,cursor='hand2')
t.window_create('1.0',window=bt)

sb3 = Scrollbar(root)
sb3.pack(fill=Y,side='right')
t['yscrollcommand'] = sb3.set 
sb3['command'] = t.yview #ָ��Scrollbar��command�¼�������Ϊyview

#-------------------------�� Text �д���һ��ͼ��---------------------------------
pic = PhotoImage(file = r'c:\temp\bee.gif')
t.image_create('20.0',image=pic)
print(t.image_names())

#-------------------------�� tag ���¼�----------------------------------------
t.tag_config('a',foreground='lightskyblue',underline=1)
def enterTag(event):
	print('Enter Event')
t.tag_bind('a','<Enter>',enterTag)
t.insert(2.0,'Enter event\n\n','a')

#-------------------------ʹ�� edit_xxx ʵ�ֳ��õı༭����----------------------------------------
def undoText():
	t.edit_undo()
def insertText():
	t.insert(1.0,'insert text')

Button(root,text='undo',command=undoText).pack(fill=X)
Button(root,text='insert text',command=insertText).pack(fill=X)
#t.edit_undo()�����е����⣬����ʵ�֡�

t.pack(fill='both')
mainloop()