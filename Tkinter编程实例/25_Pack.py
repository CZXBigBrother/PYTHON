#!/usr/bin/python
#coding:gbk
# Pack Ϊһ���ֹ��������ɽ�����Ϊһ�����Ե�����
from tkinter import *
root = Tk()

#---------------------��һ�� pack --------------------------------------------
# �鿴��ǰroot �µ������,������û�б��쳣��˵��Pack �Ѵ�����������ʹ��,��ʱ�����
#Ϊ�գ���root û���κ��������
#print( root.pack_slaves() )
#Label(root,text='pack',relief='groove').pack()
# �ٴδ�ӡ��root ������������Կ����Ѿ�����һ����������ղŴ�����Label��˵��Label
#����pack()�ǽ��Լ����뵽��root �С�
print( root.pack_slaves() )
# pack_salves ��ӡ��ǰ���ӵ�е��������ͨ������������Բ鿴��������Ƿ��а�����ϵ��

#--------------------- pack �� root �Ĺ�ϵ --------------------------------------------
#root.geometry('80x80+400+300')  #���ô�С��λ�ã���80����80����ʼ���꣩
#���Կ���Pack �Ľ��û��ʲô�仯��������root ����Ӱ�죬Ҳ����˵Pack ���ԡ���С��
#��ֻ����һ��Label �����root �����Լ��ؼ��Լ��Ĵ�С��

#----------------------��Pack ����Ӷ�����------------------------------------------

#print(root.pack_slaves())
#for i in range(5):
#	Label(root,text = 'pack' + str(i)).pack()
#print(root.pack_slaves())
#Label(root,
#	text = 'pack1',
#	bg = 'red').pack(fill = Y,expand=1,side=LEFT)
#Label(root,
#	text = 'pack2',
#	bg = 'blue').pack(fill = BOTH,expand=1,side=RIGHT)
#Label(root,
#	text = 'pack3',
#	bg = 'green').pack(fill = X,expand=0,side=LEFT)

#----------------------���֮��ļ�϶��С------------------------------------------
L1 = LabelFrame(root,text='pack1',bg='red')
L1.pack(side=LEFT,ipadx=20)
Label(L1,text='inside',bg='blue').pack(expand=1,side=LEFT)

Label(root,text='pack2',bg='blue').pack(fill=BOTH,expand=1,side=LEFT,padx=10)

Label(root,text='pack3',bg='green').pack(fill=X,expand=0,side=LEFT,padx=10)

root.mainloop()