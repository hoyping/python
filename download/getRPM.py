#!/usr/bin/env python
# *-*coding: UTF-8 *-*
#######################################
#File Name: getRPM.py
#Created Time: 2016-06-04 22:21:42
#Author: hoyping@163.com
#######################################
import re
import urllib2

url = "http://download.opensuse.org/repositories/SUSE:/SUSEStudio/SLE_11_SP2/x86_64/"

f = urllib2.urlopen(url)
content = f.read()
#print content
# <a href="skanlite-frameworks-git-20151018.g0999e40-0-x86_64.pkg.tar.xz">skanlite-frameworks-git-20151018.g0999e40-0-x86_64.pkg.tar.xz</a>
array = content.split(' ')
#print array
new_a = [ x for x in array if 'rpm</a>' in x ]
#print new_a
#pattern = re.compile('.*>(.?*rpm)</a>')
rpm = 'susegallery'
rpm_pat = re.compile(rpm + "-\d.*")
for line in new_a:
    #href="susegallery-debugsource-1.0.0-3.1.x86_64.rpm">susegallery-debugsource-1.0.0-3.1.x86_64.rpm</a>
    #print line
    #str = patter.findall(line)
    #m = re.search('.?*>(.?*rpm)</a>', line)
    try:
        m = re.search('.*>(.*rpm)</a>', line)
        #m = re.search('(.*)', line)
        name =  m.group(1)
        if name.startswith(rpm):
            result = re.match(rpm_pat, name)
            if result:
                print name
             
    except Exception, e:
        print e
