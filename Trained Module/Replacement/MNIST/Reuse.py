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
#In[]: Data Load
labs = [0,1,2,3,4,5,6,7,8,9]
sx = 28
sy = 28
mn = MNISTUitl()
X, Y, x, y = mn.getdata2(0,0,sx,sy)
#nm , xt, yt = mn.train2(X, Y, x,y,sx,sy,10,50)
xt, yt = mn.trainData(X, Y, x,y,sx,sy,10,50)
for k in range(0,10):
    #for j in range(0,10):
        #print("class1a: "+str(class1))
        class1=k
        #class2=j
        #print("class1: "+str(class1))      
        if(class1==0):
            module0=load_model('MNISTReplacedBy/module0.h5')
            module1=load_model('MNISTReplace/module1.h5')
            module2=load_model('MNISTReplace/module2.h5')
            module3=load_model('MNISTReplace/module3.h5')
            module4=load_model('MNISTReplace/module4.h5')
            module5=load_model('MNISTReplace/module5.h5')
            module6=load_model('MNISTReplace/module6.h5')
            module7=load_model('MNISTReplace/module7.h5')
            module8=load_model('MNISTReplace/module8.h5')
            module9=load_model('MNISTReplace/module9.h5')
        if(class1==1):
            module0=load_model('MNISTReplace/module0.h5')
            module1=load_model('MNISTReplacedBy/module1.h5')
            module2=load_model('MNISTReplace/module2.h5')
            module3=load_model('MNISTReplace/module3.h5')
            module4=load_model('MNISTReplace/module4.h5')
            module5=load_model('MNISTReplace/module5.h5')
            module6=load_model('MNISTReplace/module6.h5')
            module7=load_model('MNISTReplace/module7.h5')
            module8=load_model('MNISTReplace/module8.h5')
            module9=load_model('MNISTReplace/module9.h5')
        if(class1==2):
            module0=load_model('MNISTReplace/module0.h5')
            module1=load_model('MNISTReplace/module1.h5')
            module2=load_model('MNISTReplacedBy/module2.h5')
            module3=load_model('MNISTReplace/module3.h5')
            module4=load_model('MNISTReplace/module4.h5')
            module5=load_model('MNISTReplace/module5.h5')
            module6=load_model('MNISTReplace/module6.h5')
            module7=load_model('MNISTReplace/module7.h5')
            module8=load_model('MNISTReplace/module8.h5')
            module9=load_model('MNISTReplace/module9.h5')
        if(class1==3):
            module0=load_model('MNISTReplace/module0.h5')
            module1=load_model('MNISTReplace/module1.h5')
            module2=load_model('MNISTReplace/module2.h5')
            module3=load_model('MNISTReplacedBy/module3.h5')
            module4=load_model('MNISTReplace/module4.h5')
            module5=load_model('MNISTReplace/module5.h5')
            module6=load_model('MNISTReplace/module6.h5')
            module7=load_model('MNISTReplace/module7.h5')
            module8=load_model('MNISTReplace/module8.h5')
            module9=load_model('MNISTReplace/module9.h5')
        if(class1==4):
            module0=load_model('MNISTReplace/module0.h5')
            module1=load_model('MNISTReplace/module1.h5')
            module2=load_model('MNISTReplace/module2.h5')
            module3=load_model('MNISTReplace/module3.h5')
            module4=load_model('MNISTReplacedBy/module4.h5')
            module5=load_model('MNISTReplace/module5.h5')
            module6=load_model('MNISTReplace/module6.h5')
            module7=load_model('MNISTReplace/module7.h5')
            module8=load_model('MNISTReplace/module8.h5')
            module9=load_model('MNISTReplace/module9.h5')
        if(class1==5):
            module0=load_model('MNISTReplace/module0.h5')
            module1=load_model('MNISTReplace/module1.h5')
            module2=load_model('MNISTReplace/module2.h5')
            module3=load_model('MNISTReplace/module3.h5')
            module4=load_model('MNISTReplace/module4.h5')
            module5=load_model('MNISTReplacedBy/module5.h5')
            module6=load_model('MNISTReplace/module6.h5')
            module7=load_model('MNISTReplace/module7.h5')
            module8=load_model('MNISTReplace/module8.h5')
            module9=load_model('MNISTReplace/module9.h5')
        if(class1==6):
            module0=load_model('MNISTReplace/module0.h5')
            module1=load_model('MNISTReplace/module1.h5')
            module2=load_model('MNISTReplace/module2.h5')
            module3=load_model('MNISTReplace/module3.h5')
            module4=load_model('MNISTReplace/module4.h5')
            module5=load_model('MNISTReplace/module5.h5')
            module6=load_model('MNISTReplacedBy/module6.h5')
            module7=load_model('MNISTReplace/module7.h5')
            module8=load_model('MNISTReplace/module8.h5')
            module9=load_model('MNISTReplace/module9.h5')
        if(class1==7):
            module0=load_model('MNISTReplace/module0.h5')
            module1=load_model('MNISTReplace/module1.h5')
            module2=load_model('MNISTReplace/module2.h5')
            module3=load_model('MNISTReplace/module3.h5')
            module4=load_model('MNISTReplace/module4.h5')
            module5=load_model('MNISTReplace/module5.h5')
            module6=load_model('MNISTReplace/module6.h5')
            module7=load_model('MNISTReplacedBy/module7.h5')
            module8=load_model('MNISTReplace/module8.h5')
            module9=load_model('MNISTReplace/module9.h5')
        if(class1==8):
            module0=load_model('MNISTReplace/module0.h5')
            module1=load_model('MNISTReplace/module1.h5')
            module2=load_model('MNISTReplace/module2.h5')
            module3=load_model('MNISTReplace/module3.h5')
            module4=load_model('MNISTReplace/module4.h5')
            module5=load_model('MNISTReplace/module5.h5')
            module6=load_model('MNISTReplace/module6.h5')
            module7=load_model('MNISTReplace/module7.h5')
            module8=load_model('MNISTReplacedBy/module8.h5')
            module9=load_model('MNISTReplace/module9.h5')
        if(class1==9):
            module0=load_model('MNISTReplace/module0.h5')
            module1=load_model('MNISTReplace/module1.h5')
            module2=load_model('MNISTReplace/module2.h5')
            module3=load_model('MNISTReplace/module3.h5')
            module4=load_model('MNISTReplace/module4.h5')
            module5=load_model('MNISTReplace/module5.h5')
            module6=load_model('MNISTReplace/module6.h5')
            module7=load_model('MNISTReplace/module7.h5')
            module8=load_model('MNISTReplace/module8.h5')
            module9=load_model('MNISTReplacedBy/module9.h5')
        module0 = module0.predict(xt)
        module1 = module1.predict(xt)
        module2 = module2.predict(xt)
        module3 = module3.predict(xt)
        module4 = module4.predict(xt)
        module5 = module5.predict(xt)
        module6 = module6.predict(xt)
        module7 = module7.predict(xt)
        module8 = module8.predict(xt)
        module9 = module9.predict(xt)
        # sx = 28
        # sy = 28
        # # class1=0
        # # class2=0
        # mn = MNISTUitl()
        # X, Y, x, y = mn.getdata2(0,0,class1,class2,sx,sy)
        # #nm , xt, yt = mn.train2(X, Y, x,y,sx,sy,10,50)
        # xt, yt = mn.trainData(X, Y, x,y,sx,sy,10,50)
        #In[]: Parallel execution of modules
        finalPred=[]
        for i in range(0,len(yt)):
            #M0 prediction
            pred0 = module0[i]
            maxPred0= pred0.argmax()
            if(maxPred0!=0):
                maxPred0=10
            else:
                maxPred0=0
            #M1 prediction
            pred1 = module1[i]
            maxPred1= pred1.argmax()
            if(maxPred1!=0):
                maxPred1=10
            else:
                maxPred1=1
            #M2 prediction
            pred2 = module2[i]
            maxPred2= pred2.argmax()
            if(maxPred2!=0):
                maxPred2=10
            else:
                maxPred2=2
            #M3 prediction
            pred3 = module3[i]
            maxPred3= pred3.argmax()
            if(maxPred3!=0):
                maxPred3=10
            else:
                maxPred3=3
            #M4 prediction
            pred4 = module4[i]
            maxPred4= pred4.argmax()
            if(maxPred4!=0):
                maxPred4=10
            else:
                maxPred4=4
            #M5 prediction
            pred5 = module5[i]
            maxPred5= pred5.argmax()
            if(maxPred5!=0):
                maxPred5=10
            else:
                maxPred5=5
            #M6 prediction
            pred6 = module6[i]
            maxPred6= pred6.argmax()
            if(maxPred6!=0):
                maxPred6=10
            else:
                maxPred6=6
            #M7 prediction
            pred7 = module7[i]
            maxPred7= pred7.argmax()
            if(maxPred7!=0):
                maxPred7=10
            else:
                maxPred7=7
            #M8 prediction
            pred8 = module8[i]
            maxPred8= pred8.argmax()
            if(maxPred8!=0):
                maxPred8=10
            else:
                maxPred8=8
            #M9 prediction
            pred9 = module9[i]
            maxPred9= pred9.argmax()
            if(maxPred9!=0):
                maxPred9=10
            else:
                maxPred9=9
        #In[]: compute accuracy
            pred=[]
            pred.append(maxPred0)
            pred.append(maxPred1)
            pred.append(maxPred2)
            pred.append(maxPred3)
            pred.append(maxPred4)
            pred.append(maxPred5)
            pred.append(maxPred6)
            pred.append(maxPred7)
            pred.append(maxPred8)
            pred.append(maxPred9)
        #In[]:
        #pred=np.array(pred)
        #Case 1: if all of them are negative
            if(pred.count(10)==10):
                maxPrediction=[]
                maxPrediction.append(pred0[0])
                maxPrediction.append(pred1[0])
                maxPrediction.append(pred2[0])
                maxPrediction.append(pred3[0])
                maxPrediction.append(pred4[0])
                maxPrediction.append(pred5[0])
                maxPrediction.append(pred6[0])
                maxPrediction.append(pred7[0])
                maxPrediction.append(pred8[0])
                maxPrediction.append(pred9[0])
                finalPred.append(maxPrediction.index(max(maxPrediction)))
             # More than one vote   
            elif (pred.count(10)<9):
                maxPrediction=[]
                maxPrediction.append(pred0[0])
                maxPrediction.append(pred1[0])
                maxPrediction.append(pred2[0])
                maxPrediction.append(pred3[0])
                maxPrediction.append(pred4[0])
                maxPrediction.append(pred5[0])
                maxPrediction.append(pred6[0])
                maxPrediction.append(pred7[0])
                maxPrediction.append(pred8[0])
                maxPrediction.append(pred9[0])
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
        #acc.append(score)
        module.append([class1,class2])
        #print("class1: "+str(class1))
        accuracy.append(score)
print('Replacing the modules accuracy')
print(accuracy)
with open("outputSequence.txt", "w") as txt_file:
    for line in module:
        txt_file.write(" ".join(str(line)) + "\n")
with open("outputAcc.txt", "w") as txt_file:
    for line in accuracy:
        txt_file.write(str(line) + "\n")