#!/usr/bin/python
#coding:gbk

#PaneWindow(���)��һgm������������Widget
from tkinter import *
root = Tk()
#----------------------��PaneWindow�����Pane---------------------------------------------
#panes = PanedWindow(orient=VERTICAL)
#panes.pack(fill='both',expand=1)
#for w in [Label,Button,Checkbutton,Radiobutton]:
#	panes.add(w(panes,text=str(w)[16:-2],relief='groove'))

#----------------------ɾ��PaneWindowָ����pane---------------------------------------------
#ɾ��:ʹ��forget��remove
ws = []
panes1 = PanedWindow(orient = VERTICAL)
panes1.pack(fill='both',expand=1)
#����4��pane
for w in [Label,Button,Checkbutton,Radiobutton]:
	ws.append(w(panes1,text=str(w)[16:-2],relief='groove'))
for w in ws:
	panes1.add(w)

panes1.forget(ws[0])
panes1.remove(ws[3])
#----------------------���PaneWindow��ָ����pane---------------------------------------------
panes1.paneconfig(Label(panes1,text='world'),after=ws[1])

#��һwidget��Ҫʹ�����������ģ�ʹ���˴�����gm����


root.mainloop()

