#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#root.geometry('800x600')
#----------------ʹ�þ������꽫����ŵ�ָ����λ��----------------------
#lb = Label(root,text='���� Place',relief='groove')
#lb.place(x=0,y=0,anchor=NW)

##----------------ʹ��������꽫����ŵ�ָ����λ��----------------------

#lb1 = Label(root,text='��� Place',relief='groove')
#lb1.place(relx=0.5,rely=0.5,anchor=CENTER)

#-----------------ָ��������------------------------------------------
#v = IntVar()
#for i in range(5):
#	Radiobutton(
#	root,
#	text = 'Radio' + str(i),
#	variable = v,
#	value = i
#	).place(y = 25* i,anchor = NW)

##-----------------ͬʱʹ����Ժ;�������------------------------------------------
#lb1 = Label(root,text='��ǩ1',fg='green')
#lb2 = Label(root,text='��ǩ2',fg='red')
#lb1.place(relx=0.5,rely=0.5,anchor=CENTER,x=-100,y=-100)
#lb2.place(relx=0.5,rely=0.5,anchor=CENTER,x=-200,y=-200)
## ͬʱʹ����Ժ;�������ʱ������������Ȳ�����Ȼ����������������Ļ����Ͻ���ƫ��

##-----------------ʹ�� in ��ָ�����õ�����------------------------------------------
#bt1 = Button(root,text='��ť1',fg='red')
#bt2 = Button(root,text='��ť2',fg='yellow')
#bt1.place(in_=lb1,anchor=W)
#bt2.place(anchor=W)

#-----------------����ʹ�� in ��ָ�����õ�����------------------------------------------

#fm1 = Frame(root,bg='red',width=200,height=200)
#fm2 = Frame(root,bg='blue',width=100,height=100)
#fm3 = Frame(fm1,bg='yellow',width=100,height=100)

#lb1 = Label(fm1,text='labe1',fg='green')
#lb1.place(in_=fm1,relx=0.5,rely=0.5,anchor=CENTER)

#bt1 = Button(fm2,text='button',fg='red')
#bt1.place(in_ = fm2,x=50,y=50,anchor = CENTER)
#fm1.pack(fill=BOTH)
#fm2.pack()
#fm3.pack()
# in ���ǿ�������ָ�����õ�����ģ����ʹ��in ��������������������㣺���丸����
#�������������

#-------------------�¼���Place ���ʹ��--------------------------------------
#ʹ������place ��������̬�ı�����Frame �Ĵ�С��
split = 0.5
fm1 = Frame(root,bg='red')
fm2 = Frame(root,bg='blue')
#����fm1ʱ��������ռ������0.1
def incFm1(event):
	global split
	if split<1:
		split+=0.01
	fm1.place(rely=0,relheight=split,relwidth=1)
	fm2.place(rely=split,relheight=1-split,relwidth=1)
#����fm2ʱ��������ռ������0.1
def incFm2(event):
	global split #�����˵��ʹ�õ�ȫ�ֱ�����������չ��
	if split>0:
		split -= 0.01
	fm1.place(rely=0,relheight=split,relwidth=1)
	fm2.place(rely=split,relheight=1-split,relwidth=1)
# �������Ҫʹ�ã���Ȼ��ʼ����������frame��Ҳ��û�����������
fm1.place(rely = 0,relheight = split,relwidth = 1)
fm2.place(rely = split,relheight = 1 - split,relwidth = 1)
# �󶨵����¼�
fm1.bind('<Button-1>',incFm1)
fm2.bind('<Button-1>',incFm2)
# ΪSplitWindow ��ԭ���ˣ��ٸĶ�һ�¾Ϳ���ʵ��һ��SplitWindow �ˡ�


root.mainloop()
