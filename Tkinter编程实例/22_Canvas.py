#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
#---------------------���� item �� tags------------------------------------
#rt = cv.create_rectangle(10,10,110,110,tags='r1') #ʹ�� tags ָ��һ��tag('r1')
#print(cv.gettags(rt))
#cv.itemconfig(rt,tags=('r1','r2','r3','r4')) #ʹ��tags ����ָ�����tags,����������tags ������
#print(cv.gettags(rt))

##---------------------��� item ʹ��ͬһ�� tag------------------------------------
#rt1 = cv.create_rectangle(120,10,220,110,tags='r1')
#print(cv.find_withtag('r1'))

##---------------------ͨ�� tag ������ item------------------------------------
## �õ���tag ֵҲ�͵õ������item�����Զ����item ������ص�����
#for item in cv.find_withtag('r1'):
#	cv.itemconfig(item,outline='cyan')

#---------------------������ item ��� tag------------------------------------
#addtag_above������һ��item���tag
#addtag_below������һ��item���tag
rt2 = cv.create_rectangle(120,120,180,70,tags=('r1','r2','r3'))
rt3 = cv.create_rectangle(190,120,250,70,tags=('s1','s2','s3'))
rt4 = cv.create_rectangle(260,120,310,70,tags=('t1','t2','t3'))
cv.addtag_above('r4',rt3)
cv.addtag_below('r5',rt3)
for item in [rt2,rt3,rt4]:
	print(cv.gettags(item))
#Canvas ʹ����stack �ļ������´�����item ����λ��ǰһ��������item ֮�ϣ��ʵ���above
#ʱ���������rt3 �����item Ϊrt4,��rt4 �������tag('r4')��ͬ��add_below ����������
#item��

#---------------------��������item--------------------------------------------
cv.itemconfig(cv.find_above(rt3),outline='red')
cv.itemconfig(cv.find_below(rt3),outline='green')

#---------------------�ı�item��stack�е�˳��--------------------------------------------
cv.tag_lower(rt4)	#��rt4���� stack �ĵײ�
cv.tag_raise(rt2)	#��rt1���� stack �Ķ���
cv.itemconfig(cv.find_above(rt3),outline='red')
cv.itemconfig(cv.find_below(rt3),outline='green')


cv.pack()
mainloop()