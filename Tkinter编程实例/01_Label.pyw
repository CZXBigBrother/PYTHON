#!/usr/bin/python
#encoding:gbk

from tkinter import *

root = Tk()
root.minsize(300,200)
root.title('Hello World')

#---------------��ǩ-----------------------------------------------------------------------------------------------------------------
Label(root,text='Hello World',relief=GROOVE).pack()

#---------------��ǩ��ʹ��λͼ---------------------------------------------------------------------------------------------------------
#x = ["error","gray12","gray25","gray50","gray75",
#     "hourglass","info","question","warning"]
#bm = BitmapImage(file=r'c:\temp\bitmap.bmp')   #���ʹ���ⲿλͼ�������д���
Label(root,bitmap='gray50',relief=GROOVE).pack()

#---------------��ǩ��ʹ��ͼƬ---------------------------------------------------------------------------------------------------------
pic = PhotoImage(file=r'c:\temp\python.gif')
Label(root,image=pic,relief=GROOVE).pack()

#---------------��ǩ��ǰ��ɫ������ɫ----------------------------------------------------------------------------------------------------
Label(root,text='�������',fg='lightskyblue',bg='white').pack()
Label(root,text='�������',fg='#000000',bg='#A0FC96').pack()

#---------------��ǩ����ȣ��߶�--------------------------------------------------------------------------------------------------------
Label(root,text='�������',height=2,width=20,fg='#000000',bg='#FFFC96').pack()

#---------------��ǩ��ͼƬ���ı��Ļ��---------------------------------------------------------------------------------------------------
#compoound���Ե�ʹ�ã������ø�����ʱ��������ı�����ͼƬ��ֻ��ʾͼƬ
#����ֵ��left,right,top,bottom,center,
pic1 = PhotoImage(file=r'C:\temp\re.gif')
Label(root,text='�ı���ͼƬ�Ļ��',image=pic1,compound='right',relief=GROOVE).pack()
Label(root,text='�ı���ͼƬ�Ļ��',image=pic1,compound='center',relief=GROOVE).pack()
Label(root,text='�ı���ͼƬ�Ļ��',image=pic1,compound='top',relief=GROOVE).pack()
Label(root,text='�ı���ͼƬ�Ļ��',image=pic1,compound='left',relief=GROOVE).pack()
Label(root,text='�ı���ͼƬ�Ļ��',image=pic1,compound='bottom',relief=GROOVE).pack()

#---------------��ǩ���Զ�����----------------------------------------------------------------------------------------------------------
#wraplength��ָ�����ٸ���λ��ʼ����
#justify��ָ�����еĶ��뷽ʽ
#�ֶ����� \n
Label(root,text='���˶������ɺã�Ω�й��������ˣ�',height=3,width=30,wraplength=120,justify='left',fg='#000000',bg='#FFFCFF').pack()

#---------------��ǩ��ָ���ı���ͼ����Label�е���ʾλ��-------------------------------------------------------------------------------------
#anchor
#nw		n		ne
#w	  center    e
#sw		s		se
Label(root,text='���˶������ɺ�',width=40,height=3,anchor='ne',relief=GROOVE).pack()


mainloop()
