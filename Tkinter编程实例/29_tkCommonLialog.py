#!/usr/bin/python
#coding:gbk
from tkinter import *
from tkinter.simpledialog import *
root = Tk()
#------------------------ģ̬�Ի���SimpleDialg---------------------------
# SimpleDialog�� ����һ��ģ̬�Ի���
# buttons:       ��ʾ�İ�ť
# default:       Ĭ��ѡ�еİ�ť
#dlg = SimpleDialog(root,text='hello SimpleDialog',
#				   buttons=['Yes','No','cancel'],
#				   default = 0)
#ִ�жԻ���
#print(dlg.go())  #��ӡ�����ť�� buttons �е�����ֵ

# askinteger�� ����һ������ֵ
# askfloat��   ����һ��������
# askstring��  ����һ���ַ���

# initialvalue ָ��һ����ʼֵ
# prompt       ��ʾ��Ϣ
# title        ��ʾ�����
#askinteger(title='prompt',prompt='input a integer:',
#		   initialvalue = 100,minvalue=0,maxvalue=101)
#askstring(title = 'string',initialvalue = 'a string',
#		  prompt = 'input a string')
# ����ֵΪ���������ֵ��

#------------------------���ļ��Ի���---------------------------
#from tkinter.filedialog import *
#fd = LoadFileDialog(root)
# go �����ķ���ֵ��Ϊѡ�е��ı�·�������ѡ��"ȡ��"����ֵ��ΪNone
#print(fd.go())

#------------------------�����ļ��Ի���---------------------------
# SaveFileDialog������Ի���
#fs = SaveFileDialog(root)
#print(fs.go())

#------------------------ʹ����ɫ�Ի���---------------------------
#from tkinter.colorchooser import *
#print(askcolor())
# ����askcolor ����ѡ����ɫ��(R,G,B)��ɫֵ��#RRGGBB ��ʾ

#------------------------ʹ����Ϣ�Ի���---------------------------
# showinfo��			��Ϣ�Ի���
# showwarning��		����Ի���
# showerror��		����Ի���
# showquestion��		ѯ�ʶԻ���
# showokcancel��		��ʾȷ��/ȡ���Ի���
# showyesno��		��/��Ի���
# showretrycancel��	����/ȡ���Ի���
from tkinter.messagebox import *
stds=[
	showinfo, # ��ʾ��Ϣ��Ϣ��
	showwarning, # ��ʾ������Ϣ��
	showerror, # ��ʾ������Ϣ��
	askquestion, # ��ʾѯ����Ϣ��
	askokcancel, # ��ʾȷ��/ȡ����Ϣ��
	askyesno, # ��ʾ��/����Ϣ��
	askretrycancel # ��ʾ����/ȡ����Ϣ��	  
	]
#for std in stds:
#	print(str(std),std(title=str(std),message=str(std)))
# ���Ҫȷ�ϵ��������һ����ť��������ж������Ϣ��ķ���ֵ��ע�����ֵ������ͬ
# ����ֵ��ok/yes/True
print(askokcancel(title='quit application��',
				  message='woul you like quit this application',
				  default = OK #ָ��Ĭ�Ͻ���
				  )
	  )
# ʹ��default ��ָ��Ĭ�Ͻ���λ�ã�ABORT/RETRY/IGNORE/OK/CANCEL/YES/NO
# ���ָ���İ�ť�����ڣ����׳��쳣

root.mainloop()