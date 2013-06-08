#!/usr/bin/python
#coding:gbk

from tkinter import *
root = Tk()
t = Text(root,font='΢���ź� 12')

#-------------------ʹ�� tag ��ָ���ı�������--------------------------------------

t.tag_config('b',foreground='red')
t.tag_config('a',foreground='blue')
t.insert(1.0,'0123456xxx',('b','a')) #���ǰ���('b','a')��˳�����趨�ģ����ǰ���'b','a'�Ĵ���˳�����趨��
t.insert(1.0,'0123456','b')
t.pack()

#-------------------���� tag �ļ���--------------------------------------
#tag_lower
#tag_raise
t.tag_lower('b')
t.insert(1.0,'abcde',('b','a'))

#-------------------���ı������һ��tag--------------------------------------
t.tag_config('c',foreground='lightblue')
t.tag_lower('c')
for i in range(4):
	t.insert(1.0,'!@$%^&*()_+\n')
t.tag_add('c','2.5','4.end')

#-------------------ʹ���Զ��� mark ���ı������ tag--------------------------------------
t.tag_config('d',foreground='gray')
t.tag_lower('d')
for i in range(4):
	t.insert(1.0,'*******\n')
t.mark_set('ab','3.1')
t.mark_set('cd','4.2')
t.tag_add('d','ab','cd')

#-------------------ʹ�� indexes ��� Text �е�����--------------------------------------
t.tag_config('e',foreground='cyan')
t.mark_set('ea','1.0')
t.mark_set('eb','4.0')
t.tag_add('e','ea','eb')
ea = '3.3'
t.delete('1.0','3.0') #����ɾ���ı�������ɾ����֮��ص�����
print(t.get(ea,'eb'))
t.tag_delete('e') #ɾ��tag��������֮��ص����Ծ�������






root.mainloop()