#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by LiuWei 2018-02-06 14:50:00
import datetime
import os
#The days of mysql database's backupfiles
days=3
#DB user
root='root'
#DB Password
password='weoffice'
dbname='eoffice'
eofficepath='D:\\eoffice\\'
bakpath='d:\\oabak\\'
mysqlpath='D:\\eoffice\\mysql\\bin\\'
rarpath='\"C:\\Program Files\\WinRAR\\WinRAR.exe\"'

#get today's date
def GetToday():
    datenow=datetime.datetime.now();
    datetoday=datenow.strftime('%Y%m%d%H%M');
    return datetoday;
  
#get old date
def GetOldDay(days):
    datenow=datetime.datetime.now();
    oldday=datenow+datetime.timedelta(days=-days);
    olddate=oldday.strftime('%Y%m%d%H%M');
    return olddate;

#backup files
def BackUpDb(*args):
    date = GetToday();
    #print(date);
    cmd = mysqlpath + "mysqldump -u" + root + " -p" + password + " " + dbname + ">" \
    + bakpath + date + "eoffice.sql";
    print (cmd)
    os.system(cmd);
    print ('%s' % cmd);

def BackUpFiles(srcpath):
    date = GetToday();
    cmd = rarpath + " a " + bakpath + date + "eoffice.rar " + "@c:\\backup.lst";
    print (cmd);
    os.system(cmd);
    

#delete old files that N days before
def DelOldFile(days):
    oldday=GetOldDay(days)[:8];
    cmd = "del " + bakpath + oldday + "*";
    print (cmd);
    os.system(cmd);

def RunBak():
    BackUpDb(root,password,dbname,mysqlpath,bakpath);
    #BackUpFiles(eofficepath);
    DelOldFile(days);

    
RunBak();






