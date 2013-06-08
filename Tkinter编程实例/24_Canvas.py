#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
cv = Canvas(root,bg='#8c1557',height=600,width=800)

#----------------���ƻ��Σ����Σ����Σ�-------------------------------------------------
#Create arc shaped region with coordinates x1,y1,x2,y2.
cv.create_arc((20,20,110,110)) #ʹ��Ĭ�ϲ�������90�ȵ�����
style={1:PIESLICE,2:CHORD,3:ARC}
#for i in style:
#	cv.create_arc((10,10+60*i,90,90+60*i),style=style[i]) #����
#cv.create_arc((80,80,210,210),style=PIESLICE)  #����
#cv.create_arc((90,90,210,210),style=ARC) #����

#----------------���û��Σ����Σ����Σ��Ƕ�-------------------------------------------------
#for i in style:
#	cv.create_arc((30,30,60*i,60*i),style=style[i],start=30,extent=62) #����

xy = 20, 20, 180, 180 #��ʵ�γ���һ�����ӣ�Ȼ���������״�Ž�ȥ
cv.create_arc(xy, start=0, extent=270, fill="red")
cv.create_arc(xy, start=270, extent=60, fill="blue")
cv.create_arc(xy, start=330, extent=30, fill="green")

#----------------����λͼ------------------------------------------------------------
bitmap = {1:'error',2:'info',3:'question',4:'hourglass'}
for i in bitmap:
	cv.create_bitmap((20*i,20*i),bitmap=bitmap[i])

#----------------���� gif ͼ��------------------------------------------------------------
pic = PhotoImage(file=r'c:\temp\format_org.gif')
cv.create_image((450,250),image=pic)

#----------------����ֱ��------------------------------------------------------------
line_style=[(0,'none','bevel'),(1,'first','miter'),(2,'last','round'),(3,'both','round')]
for i in line_style:
	cv.create_line((200,30+i[0]*30,310,30+i[0]*30),width=1,
				arrow=i[1], #���ͷ���Ҽ�ͷ����ʽ���߶��м�ͷ
				arrowshape='8 10 3', #���ü�ͷ����״(��䳤�ȣ���ͷ���ȣ���ͷ���)
				joinstyle = i[2], #����
				)

#----------------������Բ------------------------------------------------------------
cv.create_oval((350,20,550,120),fill='gold')

#----------------���������------------------------------------------------------------
cv.create_polygon((200,200,200,300,250,300,400,400),
				  smooth = True,
				  splinesteps = 20,
				  fill='red')
# ��ָ�������������ʱ������������������������εĶ��塣

#----------------�����ı�------------------------------------------------------------
# create_text�������ı�
# anchor�������ı�λ��
# justify�������ı����뷽ʽ
txt = cv.create_text((500,500),text='�����ı��������ı�',font = '΢���ź� 18',anchor=W)
#-----------------ѡ���ı�------------------------------------------------------------
cv.select_from(txt,0)
cv.select_to(txt,3)

#-----------------�������------------------------------------------------------------
def click_me():
	from mycolor import get_color
	from random  import randint
	cv.itemconfig(txt,fill=get_color()[randint(1,400)])	
bt = Button(cv,text='ClickMe',command=click_me)
cv.create_window((540,540),window=bt,anchor=W)
cv.create_line((520,520,580,570))
cv.create_line((580,570,600,600))

cv.pack()
root.mainloop()
