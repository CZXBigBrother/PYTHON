# -*- coding: cp936 -*-
import urllib, urllib2, cookielib
import time
import json


############################################################
#Create by Jack 2009.5.25 
#xiaonei:http://http://xiaonei.com/profile.do?id=228857313
#csdn:http://hi.csdn.net/blessyou312
#baidu:http://hi.baidu.com/blessyou312/blog
#
#�����ٹ�ҽԺ��û�����֣�����Ƚ�æ��ûʱ�������ƴ���
#ϣ���ҵĴ����ܹ�����ש���������
#��ҿ���д�����ܸ�ȫ���������
#
#���Ҫʹ�ã����޸�Login�Ĳ�����mainuid spyid1 spyid2
############################################################

##################################################
#ȫ�ֱ���
cookiejar = cookielib.CookieJar()
hpcookiejar=cookielib.CookieJar()
friendscookiejar=cookielib.CookieJar()#���Ѳ���ʱҪ�����

sessionkey=''
mainuid='�Լ���ID'#�Լ���ID
spyid1='xxxx'#�ɼ���Ա1��ID
spyid2='xxxx'#�ɼ���Ա2��ID

opurl='http://xn.rongame.com/ac.php?t='

callbacktime=60*60  #�л��Լ����Աʱ�䣨�룩��Ӧ��30���ϣ�Ϊ�˱�֤�ܹ��ɹ�����������35��������

##################################################
#��¼У�ڷ���
def login(email,pwd):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    params = {'email':email, 'password':pwd}
    data = urllib.urlencode(params)
    fobj = opener.open('http://login.xiaonei.com/Login.do', data)

#���ָ��URL������
def GetHtml(visturl):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    fobj=opener.open(visturl)
    data=fobj.read()
    return data

#��¼ҽԺ
def loginhp():
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(hpcookiejar))
    #http://xn.rongame.com/xn_index.php?origin=103&xn_sig_in_iframe=1&xn_sig_method=get&xn_sig_time=1242962110548&xn_sig_added=1&xn_sig_user=228857313
    #&xn_sig_session_key=2.b02c67c5388d1727d1696046873942d2.3600.1242968400-228857313
    #&xn_sig_expires=0&xn_sig_api_key=b3563e6eba0349b898ed0810cc3a9de4&xn_sig_app_id=29507
    hpurl='http://xn.rongame.com/xn_index.php?origin=103&xn_sig_in_iframe=1&xn_sig_method=get&xn_sig_time='+GetTime()+'&xn_sig_added=1&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&xn_sig_expires=0&xn_sig_api_key=b3563e6eba0349b898ed0810cc3a9de4&xn_sig_app_id=29507'
    fobj = opener.open(hpurl)
    res=fobj.read()
    return res

#�õ�ҽԺ����
def hpGetHtml(visiturl):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(hpcookiejar))
    fobj=opener.open(visiturl)
    data=fobj.read()
    return data

#�õ�������Ϣ
def GetFriends():
    frurl=opurl+GetTime()+'&ac=friends&pid=2&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=9'
    content=hpGetHtml(frurl)
    return content

#�õ�sessionkey
def GetSessionkey():
    sessionkeycontent=GetHtml('http://apps.xiaonei.com/ronhospital/?origin=103')
    begin=sessionkeycontent.index("xn_sig_session_key=")
    if begin==-1:
        return -1
    end=sessionkeycontent.index("&",begin,begin+100)
    if end>begin:
        global sessionkey
        sessionkey=sessionkeycontent[begin+19:end]
    return 0

#���ɲ�����URL
def InitUrl(act):
    mainurl=opurl+GetTime()+'&ac='+act+'&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=9'
    return mainurl

#����ʱ��
def GetTime():
    s=time.time()
    ss=str(s*100)[0:12]+'0'
    return ss


############################################################################
#����Լ���ҽԺ��û�����ڼ���,����ID������
def Checkhp():
    opstr=InitUrl('userdata')
    content=hpGetHtml(opstr)
    begin=content.index('v={')
    newc=content[begin+2:]
    locations=json.loads(newc)
    fuid1=locations["friendadminid1"]
    funame1=locations['friendadminname1']
    fuid2=locations["friendadminid2"]
    funame2=locations['friendadminname2']
    return fuid1+':'+funame1+':'+fuid2+':'+funame2

#�鿴�Լ��ļ��Ա���
def CheckMyhp():
    opstr=InitUrl('prexy')
    content=hpGetHtml(opstr)
    begin=content.index('v={')
    newc=content[begin+2:]
    locations=json.loads(newc)

    fuid1=locations['ownadminid1']
    funame1=locations['ownadminname1']
    futime1=locations['ownadminpasstime1']
    fumoney1=locations['ownadmingivemoney1']

    fuid2=locations['ownadminid2']
    funame2=locations['ownadminname2']
    futime2=locations['ownadminpasstime2']
    fumoney2=locations['ownadmingivemoney2']

    return fuid1+':'+funame1+':'+futime1+':'+fumoney1+':'+fuid2+':'+funame2+':'+futime2+':'+fumoney2

#���Լ��ļ��Ա
def SendMySpy(fuid):
    purl=opurl+GetTime()+'&ac=action&key=k2&fuid='+fuid+'&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=2'
    strres=hpGetHtml(purl)
    return CheckRes(strres)
#�л��Լ��ļ��Ա
def CallBackSpy(pid,fuid):
    purl=opurl+GetTime()+'&ac=action&key=a3&pid='+pid+'&fuid='+fuid+'&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=2'
    strres=hpGetHtml(purl)
    return CheckRes(strres)

#������ѵļ��Ա
def DriveSpy(fuid):
    purl=opurl+GetTime()+'&ac=action&key=a1&fuid='+fuid+'&xn_sig_user='+mainuid+'&xn_sig_session_key='+sessionkey+'&disposeNext=2'
    strres=hpGetHtml(purl)
    return CheckRes(strres)
#��鷵�ص����
def CheckRes(content):
    begin=content.index('v={')
    newc=content[begin+2:]
    locations=json.loads(newc)
    state=locations['stat']
    return state



def mainfun():
    print '���Ե�¼У����'
    login('email','password');
    print '��¼�ɹ�����¼����Sessionkey'
    loghpres=GetSessionkey()
    print '��¼ҽԺ'
    loginhp()
    if loghpres==-1:
        print '��¼ҽԺʧ��'
    
    print '��¼ҽԺ�ɹ�������Լ�����̽״̬'


    #����Լ���ҽԺ��û�˼���
    myhpdata=Checkhp()
    #����У���������
    spylist=myhpdata.split(':')
    if spylist[0]!='0':
        print DriveSpy(str(spylist[0]))
    if spylist[2]!='0':
        print DriveSpy(str(spylist[2]))

    #����Լ��ļ���Ա��������žͷŵ�ָ����ID��
    myspydata=CheckMyhp()
    myspylist=myspydata.split(':')
    if myspylist[0]=='0':
        print '1�ż��Ա���У������ɵ����Ѵ�'
        print SendMySpy(spyid1)
    elif int(myspylist[2])>=callbacktime:
        print u'1�ż��Ա��['+myspylist[1]+u']����׬�ý�Ǯ��'+myspylist[3]+u' ����ָ��ʱ�䣬�����л�'
        print CallBackSpy('1',myspylist[0])
        print SendMySpy(spyid1)
    else:
        print u'1�ż��Ա��['+myspylist[1]+u']����׬�ý�Ǯ��'+myspylist[3]+u' ����ָ��ʱ�䣬���л�'
    if myspylist[4]=='0':
        print '2�ż��Ա���У������ɵ����Ѵ�'
        print SendMySpy(spyid2)
    elif int(myspylist[6])>=callbacktime:
        print u'2�ż��Ա��['+myspylist[5]+u']����׬�ý�Ǯ��'+myspylist[7]+u' ����ָ��ʱ�䣬�����л�'
        print CallBackSpy('2',myspylist[4])
        print SendMySpy(spyid2)
    else:
        print u'2�ż��Ա��['+myspylist[5]+u']����׬�ý�Ǯ��'+myspylist[7]+u' ����ָ��ʱ�䣬���л�'
    print 'һ��ִ����ϣ�'


#********************************************************
#����Ϊ���ù���
#********************************************************
mainfun()

