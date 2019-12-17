# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:53:43 2019

@author: paulj
"""
# Some sample output here: https://github.com/p-j-r/voter-verification/issues/1#issue-539113485
import os
import qrcode
from random import randint,choice

course=['bphy','bche','phil','sans','econ','bapa','bscp']
count=1
while(count<=1200):
    yy=str(randint(17,19))
    cr=choice(course)
    no=str(randint(1,60))
    if (len(no)==1):
        no="0"+no
    data =yy+cr+"0"+no          # eg: 19BPHY060
    
    filename = data+".png"       
    
    path="C:\\Users\alpha\Documents\QR"
    fullname=os.path.join(path,filename)
    img = qrcode.make(data)
    img.save(fullname)
    
    count=count+1
    
#print(count)
# This program generates about 780 images. I guess it is because id is getting repeated 
# And Windows is preventing same filenames from getting saved or it's being replaced.
