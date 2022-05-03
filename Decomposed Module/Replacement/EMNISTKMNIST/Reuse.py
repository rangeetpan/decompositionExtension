#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:38:03 2020

@author:
"""
from utils.mnistutil import MNISTUitl
#from utils.sliceutil import Slice
from tensorflow.keras.models import load_model
#import numpy as np
#Module Load
labs = [0,1,2,3,4,5,6,7,8,9]
labs1 = [0,1,2,3,4,5,6,7,8,9]
module=[]
accuracy=[]
class1=0
class2=0
counter=0
for k in range(0,10):
    class1=k
    label=[]
    if(class1==0):
        #Emodule0=load_model('Emodule0.h5')
        EmoduleA=load_model('Emodule1.h5')
        EmoduleB=load_model('Emodule2.h5')
        EmoduleC=load_model('Emodule3.h5')
        EmoduleD=load_model('Emodule4.h5')
        EmoduleE=load_model('Emodule5.h5')
        EmoduleF=load_model('Emodule6.h5')
        EmoduleG=load_model('Emodule7.h5')
        EmoduleH=load_model('Emodule8.h5')
        EmoduleI=load_model('Emodule9.h5')
        label=[1,2,3,4,5,6,7,8,9]
    if(class1==1):
        EmoduleA=load_model('Emodule0.h5')
        #Emodule1=load_model('Emodule1.h5')
        EmoduleB=load_model('Emodule2.h5')
        EmoduleC=load_model('Emodule3.h5')
        EmoduleD=load_model('Emodule4.h5')
        EmoduleE=load_model('Emodule5.h5')
        EmoduleF=load_model('Emodule6.h5')
        EmoduleG=load_model('Emodule7.h5')
        EmoduleH=load_model('Emodule8.h5')
        EmoduleI=load_model('Emodule9.h5')
        label=[0,2,3,4,5,6,7,8,9]
    if(class1==2):
        EmoduleA=load_model('Emodule0.h5')
        EmoduleB=load_model('Emodule1.h5')
        #Emodule2=load_model('Emodule2.h5')
        EmoduleC=load_model('Emodule3.h5')
        EmoduleD=load_model('Emodule4.h5')
        EmoduleE=load_model('Emodule5.h5')
        EmoduleF=load_model('Emodule6.h5')
        EmoduleG=load_model('Emodule7.h5')
        EmoduleH=load_model('Emodule8.h5')
        EmoduleI=load_model('Emodule9.h5')
        label=[0,1,3,4,5,6,7,8,9]
    if(class1==3):
        EmoduleA=load_model('Emodule0.h5')
        EmoduleB=load_model('Emodule1.h5')
        EmoduleC=load_model('Emodule2.h5')
        #Emodule3=load_model('Emodule3.h5')
        EmoduleD=load_model('Emodule4.h5')
        EmoduleE=load_model('Emodule5.h5')
        EmoduleF=load_model('Emodule6.h5')
        EmoduleG=load_model('Emodule7.h5')
        EmoduleH=load_model('Emodule8.h5')
        EmoduleI=load_model('Emodule9.h5')
        label=[0,1,2,4,5,6,7,8,9]
    if(class1==4):
        EmoduleA=load_model('Emodule0.h5')
        EmoduleB=load_model('Emodule1.h5')
        EmoduleC=load_model('Emodule2.h5')
        EmoduleD=load_model('Emodule3.h5')
        #Emodule4=load_model('Emodule4.h5')
        EmoduleE=load_model('Emodule5.h5')
        EmoduleF=load_model('Emodule6.h5')
        EmoduleG=load_model('Emodule7.h5')
        EmoduleH=load_model('Emodule8.h5')
        EmoduleI=load_model('Emodule9.h5')
        label=[0,1,2,3,5,6,7,8,9]
    if(class1==5):
        EmoduleA=load_model('Emodule0.h5')
        EmoduleB=load_model('Emodule1.h5')
        EmoduleC=load_model('Emodule2.h5')
        EmoduleD=load_model('Emodule3.h5')
        EmoduleE=load_model('Emodule4.h5')
        #Emodule5=load_model('Emodule5.h5')
        EmoduleF=load_model('Emodule6.h5')
        EmoduleG=load_model('Emodule7.h5')
        EmoduleH=load_model('Emodule8.h5')
        EmoduleI=load_model('Emodule9.h5')
        label=[0,1,2,3,4,6,7,8,9]
    if(class1==6):
        EmoduleA=load_model('Emodule0.h5')
        EmoduleB=load_model('Emodule1.h5')
        EmoduleC=load_model('Emodule2.h5')
        EmoduleD=load_model('Emodule3.h5')
        EmoduleE=load_model('Emodule4.h5')
        EmoduleF=load_model('Emodule5.h5')
        #Emodule6=load_model('Emodule6.h5')
        EmoduleG=load_model('Emodule7.h5')
        EmoduleH=load_model('Emodule8.h5')
        EmoduleI=load_model('Emodule9.h5')
        label=[0,1,2,3,4,5,7,8,9]
    if(class1==7):
        EmoduleA=load_model('Emodule0.h5')
        EmoduleB=load_model('Emodule1.h5')
        EmoduleC=load_model('Emodule2.h5')
        EmoduleD=load_model('Emodule3.h5')
        EmoduleE=load_model('Emodule4.h5')
        EmoduleF=load_model('Emodule5.h5')
        EmoduleG=load_model('Emodule6.h5')
        #Emodule7=load_model('Emodule7.h5')
        EmoduleH=load_model('Emodule8.h5')
        EmoduleI=load_model('Emodule9.h5')
        label=[0,1,2,3,4,5,6,8,9]
    if(class1==8):
        EmoduleA=load_model('Emodule0.h5')
        EmoduleB=load_model('Emodule1.h5')
        EmoduleC=load_model('Emodule2.h5')
        EmoduleD=load_model('Emodule3.h5')
        EmoduleE=load_model('Emodule4.h5')
        EmoduleF=load_model('Emodule5.h5')
        EmoduleG=load_model('Emodule6.h5')
        EmoduleH=load_model('Emodule7.h5')
        #Emodule8=load_model('Emodule8.h5')
        EmoduleI=load_model('Emodule9.h5')
        label=[0,1,2,3,4,5,6,7,9]
    if(class1==9):
        EmoduleA=load_model('Emodule0.h5')
        EmoduleB=load_model('Emodule1.h5')
        EmoduleC=load_model('Emodule2.h5')
        EmoduleD=load_model('Emodule3.h5')
        EmoduleE=load_model('Emodule4.h5')
        EmoduleF=load_model('Emodule5.h5')
        EmoduleG=load_model('Emodule6.h5')
        EmoduleH=load_model('Emodule7.h5')
        EmoduleI=load_model('Emodule8.h5')
        #Emodule9=load_model('Emodule9.h5')
        label=[0,1,2,3,4,5,6,7,8]

    for j in range(0,10):
        #print("class1a: "+str(class1))

        class2=j

        #print("class1: "+str(class1))

        if(class2==0):
            Fmodule0=load_model('Kmodule0.h5')
        if(class2==1):
            Fmodule0=load_model('Kmodule1.h5')
        if(class2==2):
            Fmodule0=load_model('Kmodule2.h5')
        if(class2==3):
            Fmodule0=load_model('Kmodule3.h5')
        if(class2==4):
            Fmodule0=load_model('Kmodule4.h5')
        if(class2==5):
            Fmodule0=load_model('Kmodule5.h5')
        if(class2==6):
            Fmodule0=load_model('Kmodule6.h5')
        if(class2==7):
            Fmodule0=load_model('Kmodule7.h5')
        if(class2==8):
            Fmodule0=load_model('Kmodule8.h5')
        if(class2==9):
            Fmodule0=load_model('Kmodule9.h5')
        sx = 28
        sy = 28
        # class1=0
        # class2=0
        mn = MNISTUitl()
        X, Y, x, y = mn.getdata2(0,0,class1,class2,sx,sy)
        #nm , xt, yt = mn.train2(X, Y, x,y,sx,sy,10,50)
        xt, yt = mn.trainData(X, Y, x,y,sx,sy,10,50)
        #In[]: Parallel execution of modules
        finalPred=[]
        Fmod = Fmodule0.predict(xt)
        EModA = EmoduleA.predict(xt)
        EModB = EmoduleB.predict(xt)
        EModC = EmoduleC.predict(xt)
        EModD = EmoduleD.predict(xt)
        EModE = EmoduleE.predict(xt)
        EModF = EmoduleF.predict(xt)
        EModG = EmoduleG.predict(xt)
        EModH = EmoduleH.predict(xt)
        EModI = EmoduleI.predict(xt)
        for i in range(0,len(yt)):
            #M0 prediction
            Fpred = Fmod[i]
            maxPredF= Fpred.argmax()
            if(maxPredF!=class2):
                maxPredF=10
            else:
                maxPredF=class1
            #MA prediction
            pred1 = EModA[i]
            maxPred1= pred1.argmax()
            if(maxPred1!=label[0]):
                maxPred1=10
            #MB prediction
            pred2 = EModB[i]
            maxPred2= pred2.argmax()
            if(maxPred2!=label[1]):
                 maxPred2=10
            #MC prediction
            pred3 = EModC[i]
            maxPred3= pred3.argmax()
            if(maxPred3!=label[2]):
               maxPred3=10
            #MD prediction
            pred4 = EModD[i]
            maxPred4= pred4.argmax()
            if(maxPred4!=label[3]):
                maxPred4=10
            #ME prediction
            pred5 = EModE[i]
            maxPred5= pred5.argmax()
            if(maxPred5!=label[4]):
                maxPred5=10
            #MF prediction
            pred6 = EModF[i]
            maxPred6= pred6.argmax()
            if(maxPred6!=label[5]):
                maxPred6=10
            #MG prediction
            pred7 = EModG[i]
            maxPred7= pred7.argmax()
            if(maxPred7!=label[6]):
               maxPred7=10
            #MH prediction
            pred8 = EModH[i]
            maxPred8= pred8.argmax()
            if(maxPred8!=label[7]):
                maxPred8=10
            #MI prediction
            pred9 = EModI[i]
            maxPred9= pred9.argmax()
            if(maxPred9!=label[8]):
               maxPred9=10
        #In[]: compute accuracy
            pred=[]
            if(class1==0):
                pred.append(maxPredF)
                pred.append(maxPred1)
                pred.append(maxPred2)
                pred.append(maxPred3)
                pred.append(maxPred4)
                pred.append(maxPred5)
                pred.append(maxPred6)
                pred.append(maxPred7)
                pred.append(maxPred8)
                pred.append(maxPred9)
            if(class1==1):
                pred.append(maxPred1)
                pred.append(maxPredF)
                pred.append(maxPred2)
                pred.append(maxPred3)
                pred.append(maxPred4)
                pred.append(maxPred5)
                pred.append(maxPred6)
                pred.append(maxPred7)
                pred.append(maxPred8)
                pred.append(maxPred9)
            if(class1==2):
                pred.append(maxPred1)
                pred.append(maxPred2)
                pred.append(maxPredF)
                pred.append(maxPred3)
                pred.append(maxPred4)
                pred.append(maxPred5)
                pred.append(maxPred6)
                pred.append(maxPred7)
                pred.append(maxPred8)
                pred.append(maxPred9)
            if(class1==3):
                pred.append(maxPred1)
                pred.append(maxPred2)
                pred.append(maxPred3)
                pred.append(maxPredF)
                pred.append(maxPred4)
                pred.append(maxPred5)
                pred.append(maxPred6)
                pred.append(maxPred7)
                pred.append(maxPred8)
                pred.append(maxPred9)
            if(class1==4):
                pred.append(maxPred1)
                pred.append(maxPred2)
                pred.append(maxPred3)
                pred.append(maxPred4)
                pred.append(maxPredF)
                pred.append(maxPred5)
                pred.append(maxPred6)
                pred.append(maxPred7)
                pred.append(maxPred8)
                pred.append(maxPred9)
            if(class1==5):
                pred.append(maxPred1)
                pred.append(maxPred2)
                pred.append(maxPred3)
                pred.append(maxPred4)
                pred.append(maxPred5)
                pred.append(maxPredF)
                pred.append(maxPred6)
                pred.append(maxPred7)
                pred.append(maxPred8)
                pred.append(maxPred9)
            if(class1==6):
                pred.append(maxPred1)
                pred.append(maxPred2)
                pred.append(maxPred3)
                pred.append(maxPred4)
                pred.append(maxPred5)
                pred.append(maxPred6)
                pred.append(maxPredF)
                pred.append(maxPred7)
                pred.append(maxPred8)
                pred.append(maxPred9)
            if(class1==7):
                pred.append(maxPred1)
                pred.append(maxPred2)
                pred.append(maxPred3)
                pred.append(maxPred4)
                pred.append(maxPred5)
                pred.append(maxPred6)
                pred.append(maxPred7)
                pred.append(maxPredF)
                pred.append(maxPred8)
                pred.append(maxPred9)
            if(class1==8):
                pred.append(maxPred1)
                pred.append(maxPred2)
                pred.append(maxPred3)
                pred.append(maxPred4)
                pred.append(maxPred5)
                pred.append(maxPred6)
                pred.append(maxPred7)
                pred.append(maxPred8)
                pred.append(maxPredF)
                pred.append(maxPred9)
            if(class1==9):
                pred.append(maxPred1)
                pred.append(maxPred2)
                pred.append(maxPred3)
                pred.append(maxPred4)
                pred.append(maxPred5)
                pred.append(maxPred6)
                pred.append(maxPred7)
                pred.append(maxPred8)
                pred.append(maxPred9)
                pred.append(maxPredF)
        #In[]:
        #pred=np.array(pred)
        #Case 1: if all of them are negative
            if(pred.count(10)==10):
                maxPrediction=[]
                if(class1==0):
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==1):
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==2):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==3):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==4):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==5):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==6):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==7):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==8):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred9[label[8]])
                if(class1==9):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                    maxPrediction.append(Fpred[class2])
                finalPred.append(maxPrediction.index(max(maxPrediction)))
             # More than one vote
            elif (pred.count(10)<9):
                maxPrediction=[]
                if(class1==0):
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==1):
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==2):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==3):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==4):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==5):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==6):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==7):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                if(class1==8):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred9[label[8]])
                if(class1==9):
                    #maxPrediction.append(Fpred[class2])
                    maxPrediction.append(pred1[label[0]])
                    maxPrediction.append(pred2[label[1]])
                    maxPrediction.append(pred3[label[2]])
                    maxPrediction.append(pred4[label[3]])
                    maxPrediction.append(pred5[label[4]])
                    maxPrediction.append(pred6[label[5]])
                    maxPrediction.append(pred7[label[6]])
                    maxPrediction.append(pred8[label[7]])
                    maxPrediction.append(pred9[label[8]])
                    maxPrediction.append(Fpred[class2])
                argPred=[]
                valPred=[]
                for i in pred:
                    if(i!=10):
                        valPred.append(maxPrediction[i])
                        #argPred.append(i)
                finalPred.append(maxPrediction.index(max(valPred)) )
            #Case 3: One vote
            elif(pred.count(10)==9):
                for i in pred:
                    if(i!=10):
                        finalPred.append(i)
        #In[]
        from sklearn.metrics import accuracy_score
        score = accuracy_score(finalPred,yt)
        print("Modularized Accuracy: "+str(score))
        print("Counter:"+str(counter))
        counter=counter+1
        #acc.append(score)
        module.append([class1,class2])
        #print("class1: "+str(class1))
        accuracy.append(score)
with open("outputSequence.txt", "w") as txt_file:
    for line in module:
        txt_file.write(" ".join(str(line)) + "\n")
with open("outputAcc.txt", "w") as txt_file:
    for line in accuracy:
        txt_file.write(str(line) + "\n")
