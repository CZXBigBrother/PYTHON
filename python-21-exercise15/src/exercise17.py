'''
Created on 2009-10-23

@author: selfimpr
'''
import re

datas = ['Thu Jul 22 19:21:19 2004::izsp@dicqdhytvhv.edu::1090549279-4-11', 
         'Sun Jul 13 22:42:11 2008::zqeu@dxaibjgkniy.com::1216014131-4-11', 
         'Sat May 5 16:36:23 1990::fclihw@alwdbzpsdg.edu::641950583-6-10', 
         'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8', 
         'Thu Jun 26 19:08:59 2036::ugxfugt@jkhuqhs.net::2098145339-7-7', 
         'Tue Apr 10 01:04:45 2012::zkwaq@rpxwmtikse.com::1334045085-5-10']

pattern = re.compile('^(?i)\w{3}')

if __name__ == '__main__':
    results = dict.fromkeys(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 0)
    for data in datas:
        week = pattern.search(data).group()
        results[week] += 1
    for key in results:
        print '%s: %d' % (key, results[key])
    