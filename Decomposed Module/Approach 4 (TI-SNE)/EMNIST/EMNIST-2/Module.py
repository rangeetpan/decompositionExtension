#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:47:48 2020

@author: 
"""
# In[]: Library
from utils.mnistutil import MNISTUitl
from utils.sliceutil2 import Slice
from keras.models import load_model
from datetime import datetime
import numpy as np
sx = 28
sy = 28
accuracyCheck=[]
# In[]: Data Acquisition and Model Training
# mn = MNISTUitl()
# X, Y, x, y = mn.getdata2(0,0,sx,sy)
# nm , xt, yt = mn.train2(X, Y, x,y,sx,sy,10,50)
# #X, Y, x, y = mn.getdata2(0,0,sx,sy)
# model , xt1, yt1 = mn.train2(X, Y, x,y,sx,sy,10,50)
labs = [0,1,2,3,4,5,6,7,8,9]
mn = MNISTUitl()
X, Y, x, y = mn.getdata2(0,0,sx,sy)
#nm , xt, yt = mn.trainDense2(X, Y, x,y,sx,sy,10,50)
xt, yt, xT, yT = mn.trainData(X, Y, x,y,sx,sy,10,50)
# In[]: Module 0
test=[]
accuracyCheck=[]
nonDigit=[]
print("Start Time:"+datetime.now().strftime("%H:%M:%S"))
#nm.save('mnist.h5')
for j in labs:
    print("#Module "+str(j)+" in progress....")
    #test=[]
    slicingModel=load_model('emnist.h5')
    #X, Y, x, y = mn.getdata2(0,0,sx,sy)
    model=load_model('emnist.h5')
    digit  = []
    slc = Slice()
    W1, W2, W3, b1, b2, b3 = slc.getweights(slicingModel)
    for i in range(0,len(yt)):
        if yt[i] == j and model.predict(xT[i:i+1])[0][j] >.9:
            digit.append(xT[i])
    #print(len(zero),len(Y))
    #np.random.shuffle(digit)
    digit = digit[0:100]
    mc = 0
    for x in digit:
        W1, W2, W3, b1, b2, b3 = slc.modifyThroughInterSection(slicingModel,x,sx,sy)
        mc=mc+1
        if np.count_nonzero(slc.D3) < 45:
            #print("Breaking at mc ", mc,np.count_nonzero(slc.D2))
            slc.first = True
    digit=[]
    for k in labs:
        if(k!=j):
            temp=xT[yT==k]
            temp=temp[0:11]
            for u in temp:
                digit.append(u)
    #digit = digit[0:200]
    np.random.shuffle(digit)
    mc = 0
    for x in digit:
        W1, W2, W3, b1, b2, b3 = slc.dynamicmodify(slicingModel,x,sx,sy)
        mc=mc+1
        if np.count_nonzero(slc.D3) < 45:
            #print("Breaking at mc ", mc,np.count_nonzero(slc.D2))
            slc.first = True
    #In[]: Verifiy
    model.layers[1].set_weights([slc.D1,slc.d1])
    model.layers[2].set_weights([slc.D2,slc.d2])
    model.layers[3].set_weights([slc.D3,slc.d3])
    model.save('module'+str(j)+'.h5')
    # # In[]:
    # from sklearn.metrics import accuracy_score
    # zeros = []
    # pred = []
    # tr = []
    # #labs = [0,1,2,3,4,5,6,7,8,9]
    # acc = []
    # count = 0
    # #for l in labs:
    # pred = []
    # tr = []
    # for i in range(0,len(yt)):
    # #for i in range(0,len(yt[0:500])):
    #     count += 1
    #     #if yt[i] == j:
    #     p = model.predict(xt[i:i+1])
    #     m = p.argmax()
    #     test.append(p)
    #     if(yt[i]!=j):
    #         tr.append(1)
    #         if(m!=j):
    #             pred.append(1)
    #         else:
    #             pred.append(0)
    #     else:
    #         if(m==j):
    #             pred.append(0)
    #         else:
    #             pred.append(1)
    #         tr.append(0)
    # score = accuracy_score(pred,tr)
    # acc.append(score)
    # accuracyCheck.append(score)
