#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#--------------------Text ����--------------------------------------------
t = Text(root,height=10,font='΢���ź� 12')
t.pack()
#--------------------Text ����(ʹ�� line.col ����)-----------------------------------------
#���һ�У���һ������ı� 0123456789
#t.insert(0.0,'0123456789')
#t.insert('2.end','\n\n')
#t.insert(1.0,'ABCDEFGHIJ')
#���Կ�����ʹ��indexesʱ�������ֵ������Text ��buffer�����򲻻�
#�׳��쳣���������ֵ����

#-------------------- ʹ�����õ� mark ����λ��-----------------------------------------
#��ʾʹ�����õ�mark��
#INSERT	  ��  ����λ��
#CURRENT  ��  ��ǰ�������λ��
#END	  ��  ����buffer�����
#SEL_FIRST��  ѡ���ı��Ŀ�ʼ
#SEL_LAST ��  ѡ���ı������
#mark = [INSERT,CURRENT,END,SEL_FIRST,SEL_LAST]
#for i in range(10):
#	t.insert(1.0,'*'*i+'\n')

#def text_fun():
#	def fun(flag):	#ʹ��"�պ�"����
#		t.insert(flag,flag)
#	return fun
#def fun1():
#	t.insert(CURRENT,'  current  ')
#for i in range(len(mark)):
#	Button(root,text='insert jcodeer at '+mark[i],
#		width=20,command=lambda x=mark[i]:text_fun()(x)).pack()
	
#������ Button(root,text='insert jcodeer at '+mark[i],command=lambda :text_fun()(mark[i])).pack()
#�������ݲ�����������ġ���lambda ��������ʹ��ʱӦ��С�ģ�
#���û��ѡ���ַ����� sel.first �� sel.end λ�û�����쳣��

#-------------------- ʹ��ʹ�ñ��ʽ����ǿ mark -----------------------------------------
for i in range(1,10):
	t.insert(1.0,'0123456789\n')
a = 'test_mark'
def forwardChars():
	t.mark_set(a,CURRENT+'+5c')
def backwardChars():
	t.mark_set(a,CURRENT+'-5c')
def forwardLines():
	t.mark_set(a,CURRENT+'-5l')
def backwardLines():
	t.mark_set(a,CURRENT+'-5l')
def lineStart():
	t.mark_set(a,CURRENT+' linestart')
def lineEnd():
	t.mark_set(a,CURRENT+' lineend')
def wordStart():
	t.mark_set(a,CURRENT+' wordstart')
def wordEnd():
	t.mark_set(a,CURRENT+' wordend')

t.mark_set(a,CURRENT)
Button(root,text='forward 5 chars ', command=forwardChars ).pack(fill=X)
Button(root,text='backward 5 chars ',command=backwardChars).pack(fill=X)
Button(root,text='forward 5 lines ', command=forwardLines ).pack(fill=X)
Button(root,text='backward 5 lines ',command=backwardLines).pack(fill=X)
Button(root,text='line start ',		 command=lineStart	  ).pack(fill=X)
Button(root,text='line end ',		 command=lineEnd	  ).pack(fill=X)
Button(root,text='word start ',		 command=wordStart	  ).pack(fill=X)
Button(root,text='word end ',		 command=wordEnd	  ).pack(fill=X)

def insertText():
	t.insert(INSERT,'insert')
def currentText():
	t.insert(CURRENT,'current')
def markText():
	t.insert(a,'mark')
Button(root,text = 'insert jcodeer',command=insertText).pack(fill=X)
Button(root,text = 'insert jcodeer',command=currentText).pack(fill=X)
Button(root,text = 'insert jcodeer',command=markText).pack(fill=X)


root.mainloop()

