#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
fm1 = Frame(root)
fm1.pack(anchor=W)
fm2 = Frame(root)
fm2.pack(anchor=W)
fm3 = Frame(root)
fm3.pack(anchor=W)
#ListboxΪ�б��ؼ�
#���԰���һ�������ı��
#��������Ϊ��ѡ���ѡ

#---------------------����һ��Listbox-------------------------------------------------------------------------------------
lb = Listbox(fm1)
item = ['python','tkinter','widget']
for i in item:
	lb.insert(END,i)
lb.pack(side='left')

#---------------------Listbox����ѡ�ж��item-----------------------------------------------------------------------------
#selectmode:SINGLE, BROWSE, MULTIPLE, or EXTENDED. Default is BROWSE
listbox = Listbox(fm1,selectmode=SINGLE)
for i in item:
	listbox.insert(END,i)
listbox.pack(side='left')

#---------------------ʹListbox֧������ƶ�ѡ��λ��-------------------------------------------------------------------------
#selectmode������ΪBROWSE��Ĭ�ϣ������϶���꣬Ҳ�������¼���
#��SINGEL�Ͳ�֧�ִ��ֲ���
lb1 = Listbox(fm1,selectmode=SINGLE)
for i in item:
	lb1.insert(END,i)
lb1.pack(side='left')

#---------------------ʹListbox֧��Shift��Control-----------------------------------------------------------------------
#selectmode:EXTENDED
lb2 = Listbox(fm1,selectmode=EXTENDED)
for i in item:
	lb2.insert(END,i)
lb2.pack(side='left')

#---------------------��Listbox�����һ��item----------------------------------------------------------------------------
lb3 = Listbox(fm1)
for i in item:
	lb3.insert(END,i)
lb3.insert(0,['linux','win','unix'])
lb3.insert(0,'linux','win','unix')
lb3.pack(side='left')
def ins():
	lb3.insert(ACTIVE,'mac OS') #ACTIVE��ǰѡ��������һ��
Button(fm1,text='����',command=ins).pack(side='left')

#---------------------ɾ��Listbox��item------------------------------------------------------------------------------
lb4 = Listbox(fm2)
for i in range(10):
	lb4.insert(END,str(i))
lb4.delete(1,3)
lb4.pack(side='left')

#---------------------ѡ�л�ȡ��Listbox��item---------------------------------------------------------------------------
lb5 = Listbox(fm2)
for i in range(10):
	lb5.insert(END,str(i))
lb5.selection_set(0,9)		#ѡ��0����9
lb5.pack(side='left')
lb5.selection_clear(1,3)	#ȡ��0����2

#---------------------�õ���ǰListbox��item����--------------------------------------------------------------------------
lb6 = Listbox(fm2)
for i in range(10):
	lb6.insert(END,str(i))
lb6.delete(3)
lb6.delete(3)
print(lb6.size())
lb6.pack(side='left')

#---------------------����ָ��������item(һ������)-----------------------------------------------------------------------
lb7 = Listbox(fm2)
for i in range(10):
	lb7.insert(END,str(i*100))
lb7.pack(side='left')
print(lb7.get(3))
print(lb7.get(3,7))

#---------------------���ص�ǰѡ�е�item������(һ������)------------------------------------------------------------------
lb8 = Listbox(fm2)
for i in range(100):
	lb8.insert(END,str(i*100))
lb8.selection_set(3,8)
print(lb8.curselection())
lb8.pack(side='left')

#---------------------�ж�һ��item�Ƿ�ѡ��------------------------------------------------------------------------------
lb9 = Listbox(fm3)
for i in range(10):
	lb9.insert(END,str(i*100))
lb9.selection_set(3,8)
print(lb9.selection_includes(8))
print(lb9.selection_includes(0))
lb9.pack(side='left')

#---------------------Listbox������İ�------------------------------------------------------------------------------
lbvar = StringVar()
lb10 = Listbox(fm3,listvariable=lbvar)
for i in range(10):
	lb10.insert(END,str(i*100))
#��ӡ��ǰ�б��е�����itemֵ
print(lbvar.get())
lbvar.set(('1000','200'))
lb10.pack(side='left')

#---------------------Listbox���¼���------------------------------------------------------------------------------
def printList(event):
	print(lb11.get(lb11.curselection()))
lb11 = Listbox(fm3)
lb11.bind('<Double-Button-1>',printList) #˫��
for i in range(10):
	lb11.insert(END,str(i*100))
lb11.pack()
# ����֧��command ���������ûص������ˣ�ʹ��bind ��ָ���ص�����,��ӡ��ǰѡ�е�ֵ


mainloop()