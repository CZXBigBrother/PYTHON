#!/usr/bin/python
#coding:gbk

# Tkinter �ο������Ƽ�ʹ�õ�һ����������ʵ�ֻ����ǽ�Widget �߼��Ϸָ�ɱ����ָ
#����λ�÷�����Ҫ��Widget �Ϳ����ˡ�

from tkinter import *
root = Tk()
root.geometry('600x400')
#--------------------------ʹ�� grid----------------------------------------
#lb1 = Label(root,text='hello',bg='gold')
#lb2 = Label(root,text='grid',bg='yellow')
#lb1.grid()
#lb2.grid()
#grid ��������Ϊ��Ҫ�Ĳ���������ָ����������õ�ʲôλ�ã�һ����row,��һ����
#column�������ָ��row,�Ὣ������õ���һ�����õ����ϣ������ָ��column����ʹ��
#��һ�С�


#lb2.grid(row=0,column=1)

#Label(root,text = 'Hello').grid()
## �ڵ�һ�У���10 �з���lb2
#Label(root,text = 'Grid').grid(row = 0,column = 2)
## Lable(root,text = '3').grid(row = 0,column = 3)

# grid���������
#Label(root,text = '1').grid()
# �ڵ�1 �У���11 �з���lb2
#Label(root,text = '2',relief='groove').grid(row = 0,column = 2)
#Label(root,text = '3',relief='groove').grid(row = 0,column = 3)

#lb3 = Label(root,text='��ǩ3')
#lb4 = Label(root,text='��ǩ4')
#lb3.grid(row=1,column=0)
#lb4.grid(row=1,column=0)
#def forgetLabel():
#	# grid_slaves ����grid ��(0,0)λ�õ��������
#	# grid_forget ����������grid ���Ƴ�����δɾ��������ʹ��grid �ٽ�����ʾ����)
#	root.grid_slaves(1,0)[0].grid_forget()

#Button(root,text='forget last',command=forgetLabel).grid(row=2,column=1)

#root.columnconfigure(2,minsize=100) #����Ϊ2�������У����е���С���
#root.rowconfigure(2,minsize=100) #
# �����л���(rowconfigure)������ʱʹ�ø������ķ���,�����Լ����á�


#-------------------���ʹ�ö��У����У�-------------------------------
# columnspan��ָ��ʹ�ü���
# rowspan��ָ��ʹ�ü���
lbA = Label(root,text = 'A',bg = 'red')
lbB = Label(root,text = 'B',bg = 'blue')
lbC = Label(root,text = 'C',bg = 'red')
lbD = Label(root,text = 'D',bg = 'yellow')
lbE = Label(root,text = 'E',bg = 'pink')

lbA.grid(row = 0,column = 0,columnspan = 2,sticky=W)
lbB.grid(row = 1,column = 0)
lbC.grid(row = 1,column = 1)
lbD.grid(row = 2)
lbE.grid(row = 0,column = 2)

#-------------------���ö�������----------------------------------------------
# sticky������������뷽ʽ
# Ĭ�������£�����Ķ��뷽ʽΪ���У�����sticky ���Կ��Կ��ƶ��뷽ʽ�����õ�ֵ
#��N,S,E,W���������ֵ
root.mainloop()