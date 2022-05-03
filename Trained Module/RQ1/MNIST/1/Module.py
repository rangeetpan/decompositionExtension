#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 12:56:15 2022

@author: rangeet
"""
from utils.mnistutil import MNISTUitl
from Reuse import Reuse
from sklearn.metrics import accuracy_score
sx = 28
sy = 28
accuracyCheck=[]
labs = [0,1,2,3,4,5,6,7,8]
mn = MNISTUitl()
ru=Reuse()
x_train, y_train, x_test, y_test = mn.load_data()
X, Y, x, y = mn.getdata2(0,0,sx,sy)
xt, yt, xT, yT = mn.trainData(X, Y, x,y,sx,sy,9,50)
for i in range(10):
    cl=i
    X, Y, x, y = mn.getdata50(x_train, y_train, x_test, y_test,cl,sx,sy)
    nm , xtt, ytt = mn.trainDense(X, Y, x,y,sx,sy,2,50)
    nm.save('module'+str(cl)+'.h5')
ru.reuseModule(xt, yt, xT, yT)