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
        #Mmodule0=load_model('Fmodule0.h5')
        MmoduleA=load_model('Fmodule1.h5')
        MmoduleB=load_model('Fmodule2.h5')
        MmoduleC=load_model('Fmodule3.h5')
        MmoduleD=load_model('Fmodule4.h5')
        MmoduleE=load_model('Fmodule5.h5')
        MmoduleF=load_model('Fmodule6.h5')
        MmoduleG=load_model('Fmodule7.h5')
        MmoduleH=load_model('Fmodule8.h5')
        MmoduleI=load_model('Fmodule9.h5')
        label=[1,2,3,4,5,6,7,8,9]
    if(class1==1):
        MmoduleA=load_model('Fmodule0.h5')
        #Mmodule1=load_model('Fmodule1.h5')
        MmoduleB=load_model('Fmodule2.h5')
        MmoduleC=load_model('Fmodule3.h5')
        MmoduleD=load_model('Fmodule4.h5')
        MmoduleE=load_model('Fmodule5.h5')
        MmoduleF=load_model('Fmodule6.h5')
        MmoduleG=load_model('Fmodule7.h5')
        MmoduleH=load_model('Fmodule8.h5')
        MmoduleI=load_model('Fmodule9.h5')
        label=[0,2,3,4,5,6,7,8,9]
    if(class1==2):
        MmoduleA=load_model('Fmodule0.h5')
        MmoduleB=load_model('Fmodule1.h5')
        #Mmodule2=load_model('Fmodule2.h5')
        MmoduleC=load_model('Fmodule3.h5')
        MmoduleD=load_model('Fmodule4.h5')
        MmoduleE=load_model('Fmodule5.h5')
        MmoduleF=load_model('Fmodule6.h5')
        MmoduleG=load_model('Fmodule7.h5')
        MmoduleH=load_model('Fmodule8.h5')
        MmoduleI=load_model('Fmodule9.h5')
        label=[0,1,3,4,5,6,7,8,9]
    if(class1==3):
        MmoduleA=load_model('Fmodule0.h5')
        MmoduleB=load_model('Fmodule1.h5')
        MmoduleC=load_model('Fmodule2.h5')
        #Mmodule3=load_model('Fmodule3.h5')
        MmoduleD=load_model('Fmodule4.h5')
        MmoduleE=load_model('Fmodule5.h5')
        MmoduleF=load_model('Fmodule6.h5')
        MmoduleG=load_model('Fmodule7.h5')
        MmoduleH=load_model('Fmodule8.h5')
        MmoduleI=load_model('Fmodule9.h5')
        label=[0,1,2,4,5,6,7,8,9]
    if(class1==4):
        MmoduleA=load_model('Fmodule0.h5')
        MmoduleB=load_model('Fmodule1.h5')
        MmoduleC=load_model('Fmodule2.h5')
        MmoduleD=load_model('Fmodule3.h5')
        #Mmodule4=load_model('Fmodule4.h5')
        MmoduleE=load_model('Fmodule5.h5')
        MmoduleF=load_model('Fmodule6.h5')
        MmoduleG=load_model('Fmodule7.h5')
        MmoduleH=load_model('Fmodule8.h5')
        MmoduleI=load_model('Fmodule9.h5')
        label=[0,1,2,3,5,6,7,8,9]
    if(class1==5):
        MmoduleA=load_model('Fmodule0.h5')
        MmoduleB=load_model('Fmodule1.h5')
        MmoduleC=load_model('Fmodule2.h5')
        MmoduleD=load_model('Fmodule3.h5')
        MmoduleE=load_model('Fmodule4.h5')
        #Mmodule5=load_model('Fmodule5.h5')
        MmoduleF=load_model('Fmodule6.h5')
        MmoduleG=load_model('Fmodule7.h5')
        MmoduleH=load_model('Fmodule8.h5')
        MmoduleI=load_model('Fmodule9.h5')
        label=[0,1,2,3,4,6,7,8,9]
    if(class1==6):
        MmoduleA=load_model('Fmodule0.h5')
        MmoduleB=load_model('Fmodule1.h5')
        MmoduleC=load_model('Fmodule2.h5')
        MmoduleD=load_model('Fmodule3.h5')
        MmoduleE=load_model('Fmodule4.h5')
        MmoduleF=load_model('Fmodule5.h5')
        #Mmodule6=load_model('Fmodule6.h5')
        MmoduleG=load_model('Fmodule7.h5')
        MmoduleH=load_model('Fmodule8.h5')
        MmoduleI=load_model('Fmodule9.h5')
        label=[0,1,2,3,4,5,7,8,9]
    if(class1==7):
        MmoduleA=load_model('Fmodule0.h5')
        MmoduleB=load_model('Fmodule1.h5')
        MmoduleC=load_model('Fmodule2.h5')
        MmoduleD=load_model('Fmodule3.h5')
        MmoduleE=load_model('Fmodule4.h5')
        MmoduleF=load_model('Fmodule5.h5')
        MmoduleG=load_model('Fmodule6.h5')
        #Mmodule7=load_model('Fmodule7.h5')
        MmoduleH=load_model('Fmodule8.h5')
        MmoduleI=load_model('Fmodule9.h5')
        label=[0,1,2,3,4,5,6,8,9]
    if(class1==8):
        MmoduleA=load_model('Fmodule0.h5')
        MmoduleB=load_model('Fmodule1.h5')
        MmoduleC=load_model('Fmodule2.h5')
        MmoduleD=load_model('Fmodule3.h5')
        MmoduleE=load_model('Fmodule4.h5')
        MmoduleF=load_model('Fmodule5.h5')
        MmoduleG=load_model('Fmodule6.h5')
        MmoduleH=load_model('Fmodule7.h5')
        #Mmodule8=load_model('Fmodule8.h5')
        MmoduleI=load_model('Fmodule9.h5')
        label=[0,1,2,3,4,5,6,7,9]
    if(class1==9):
        MmoduleA=load_model('Fmodule0.h5')
        MmoduleB=load_model('Fmodule1.h5')
        MmoduleC=load_model('Fmodule2.h5')
        MmoduleD=load_model('Fmodule3.h5')
        MmoduleE=load_model('Fmodule4.h5')
        MmoduleF=load_model('Fmodule5.h5')
        MmoduleG=load_model('Fmodule6.h5')
        MmoduleH=load_model('Fmodule7.h5')
        MmoduleI=load_model('Fmodule8.h5')
        #Mmodule9=load_model('Fmodule9.h5')
        label=[0,1,2,3,4,5,6,7,8]

    for j in range(0,10):
        #print("class1a: "+str(class1))

        class2=j

        #print("class1: "+str(class1))

        if(class2==0):
            Fmodule0=load_model('Emodule0.h5')
        if(class2==1):
            Fmodule0=load_model('Emodule1.h5')
        if(class2==2):
            Fmodule0=load_model('Emodule2.h5')
        if(class2==3):
            Fmodule0=load_model('Emodule3.h5')
        if(class2==4):
            Fmodule0=load_model('Emodule4.h5')
        if(class2==5):
            Fmodule0=load_model('Emodule5.h5')
        if(class2==6):
            Fmodule0=load_model('Emodule6.h5')
        if(class2==7):
            Fmodule0=load_model('Emodule7.h5')
        if(class2==8):
            Fmodule0=load_model('Emodule8.h5')
        if(class2==9):
            Fmodule0=load_model('Emodule9.h5')
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
        Fmodule0X = Fmodule0.predict(xt)
        MmoduleAX = MmoduleA.predict(xt)
        MmoduleBX = MmoduleB.predict(xt)
        MmoduleCX = MmoduleC.predict(xt)
        MmoduleDX = MmoduleD.predict(xt)
        MmoduleEX = MmoduleE.predict(xt)
        MmoduleFX = MmoduleF.predict(xt)
        MmoduleGX = MmoduleG.predict(xt)
        MmoduleHX = MmoduleH.predict(xt)
        MmoduleIX = MmoduleI.predict(xt)
        for i in range(0,len(yt)):
            #M0 prediction
            Fpred = Fmodule0X[i]
            maxPredF= Fpred.argmax()
            if(maxPredF!=class2):
                maxPredF=10
            else:
                maxPredF=class1
            #MA prediction
            pred1 = MmoduleAX[i]
            maxPred1= pred1.argmax()
            if(maxPred1!=label[0]):
                maxPred1=10
            else:
                maxPred1=label[0]
            #MB prediction
            pred2 = MmoduleBX[i]
            maxPred2= pred2.argmax()
            if(maxPred2!=label[1]):
                 maxPred2=10
            else:
                maxPred2=label[1]
            #MC prediction
            pred3 = MmoduleCX[i]
            maxPred3= pred3.argmax()
            if(maxPred3!=label[2]):
               maxPred3=10
            else:
                maxPred3=label[2]
            #MD prediction
            pred4 = MmoduleDX[i]
            maxPred4= pred4.argmax()
            if(maxPred4!=label[3]):
                maxPred4=10
            else:
                maxPred4=label[3]
            #ME prediction
            pred5 = MmoduleEX[i]
            maxPred5= pred5.argmax()
            if(maxPred5!=label[4]):
                maxPred5=10
            else:
                maxPred5=label[4]
            #MF prediction
            pred6 = MmoduleFX[i]
            maxPred6= pred6.argmax()
            if(maxPred6!=label[5]):
                maxPred6=10
            else:
                maxPred6=label[5]
            #MG prediction
            pred7 = MmoduleGX[i]
            maxPred7= pred7.argmax()
            if(maxPred7!=label[6]):
               maxPred7=10
            else:
                maxPred7=label[6]
            #MH prediction
            pred8 = MmoduleHX[i]
            maxPred8= pred8.argmax()
            if(maxPred8!=label[7]):
                maxPred8=10
            else:
                maxPred8=label[7]
            #MI prediction
            pred9 = MmoduleIX[i]
            maxPred9= pred9.argmax()
            if(maxPred9!=label[8]):
               maxPred9=10
            else:
                maxPred9=label[8]
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
