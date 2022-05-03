#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 13:26:25 2022

@author: rangeet
"""

from utils.mnistutil import MNISTUitl
from tensorflow.keras.models import load_model
import numpy as np

class Reuse():
    def reuseModule(self,xt, yt, xT, yT):
        #Module Load
        a=[]
        module0=load_model('module0.h5')
        module1=load_model('module1.h5')
        module2=load_model('module2.h5')
        module3=load_model('module3.h5')
        module4=load_model('module4.h5')
        module5=load_model('module5.h5')
        module6=load_model('module6.h5')
        module7=load_model('module7.h5')
        module8=load_model('module8.h5')
        module9=load_model('module9.h5')
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
# In[]: Parallel execution of modules
        finalPred=[]
        totalCheck=len(yt)
        for i in range(0,totalCheck):
            #print(i)
            #i=8
            #M0 prediction
            
            pred0 = module0[i]
            maxPred0= pred0.argmax()
            if(maxPred0!=0):
                maxPred0=10
            #M1 prediction
            pred1 = module1[i]
            maxPred1= pred1.argmax()
            if(maxPred1!=0):
                maxPred1=10
            #M2 prediction
            pred2 = module2[i]
            maxPred2= pred2.argmax()
            if(maxPred2!=0):
                maxPred2=10
            #M3 prediction
            pred3 = module3[i]
            maxPred3= pred3.argmax()
            if(maxPred3!=0):
                maxPred3=10
            #M4 prediction
            pred4 = module4[i]
            maxPred4= pred4.argmax()
            if(maxPred4!=0):
                maxPred4=10
            #M5 prediction
            pred5 = module5[i]
            maxPred5= pred5.argmax()
            if(maxPred5!=0):
                maxPred5=10
            #M6 prediction
            pred6 = module6[i]
            maxPred6= pred6.argmax()
            if(maxPred6!=0):
                maxPred6=10
            #M7 prediction
            pred7 = module7[i]
            maxPred7= pred7.argmax()
            if(maxPred7!=0):
                maxPred7=10
            #M8 prediction
            pred8 = module8[i]
            maxPred8= pred8.argmax()
            if(maxPred8!=0):
                maxPred8=10
            #M9 prediction
            pred9 = module9[i]
            maxPred9= pred9.argmax()
            if(maxPred9!=0):
                maxPred9=10
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
                a=maxPrediction
                argPred=[]
                valPred=[]
                count=0
                for k in pred:
                    if(k!=10):
                        valPred.append(maxPrediction[count])
                    count+=1
                        #argPred.append(i)
                finalPred.append(maxPrediction.index(max(valPred)) )
            #Case 3: One vote
            elif(pred.count(10)==9):
                count=0
                for k in pred:
                    if(k!=10):
                       finalPred.append(count)
                    count+=1
        # In[]
        from sklearn.metrics import accuracy_score
        score = accuracy_score(finalPred,yt[:totalCheck])
        print("Composed Model Accuracy: "+str(score))
        return score

#        # In[]:
#        from sklearn.metrics import confusion_matrix
#        matrix = confusion_matrix(yt[:totalCheck], finalPred)
#        matrix.diagonal()/matrix.sum(axis=1)
