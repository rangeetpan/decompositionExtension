'''
Created on Feb 8, 2019

@author:  
'''

from keras.datasets import mnist
from skimage.transform import resize
import numpy as np
from keras import backend as K
import keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from sklearn.utils import shuffle



class MNISTUitl:
    
    
    def __init__(self):
        self.name = None
    def load(self,f):
        return np.load(f)['arr_0'] 
    
    def getdata50(self,x_train, y_train, x_test, y_test, mod, img_rows = 28, img_cols = 28):
    # the data, split between train and test sets
#        x_train = self.load('emnist-train-imgs.npz')
#        x_test = self.load('emnist-test-imgs.npz')
#        y_train = self.load('emnist-train-labels.npz')
#        for i in range(0,len(y_train)):
#            y_train[i]=y_train[i]-1
#        y_test = self.load('emnist-test-labels.npz')
#        for i in range(0,len(y_test)):
#            y_test[i]=y_test[i]-1
        x_zo = []
        y_zo = []
        for i in range(len(y_train)):
            if y_train[i] in [mod]:
                A = resize(x_train[i], (img_rows,  img_cols),mode='constant')
                Ay = y_train[i]#resize(y_train[i], (img_rows, img_cols))
                x_zo.append(A)
                y_zo.append(0)
        positiveExampleLen = len(y_zo)
        eachLength = int(positiveExampleLen/9)
        print(eachLength)
        for i in range(10):
            count=0
            if(i!=mod):
                print(i)
                for j in range(len(y_train)):
                    if(count>eachLength):
                        break
                    else:
                        if y_train[j] in [i]:
                            A = resize(x_train[j], (img_rows,  img_cols),mode='constant')
                            Ay = y_train[j]#resize(y_train[i], (img_rows, img_cols))
                            x_zo.append(A)
                            y_zo.append(1)
                            count+=1
        xt_zo = []
        yt_zo = []
        x_zo, y_zo = shuffle(x_zo, y_zo, random_state=0)
        for i in range(len(y_test)):
            if y_test[i] in [0,1,2,3,4,5,6,7,8,9]:
                A = resize(x_test[i], (img_rows,  img_cols),mode='constant')
                Ay = y_test[i]#resize(y_train[i], (img_rows, img_cols))
                xt_zo.append(A)
                yt_zo.append(Ay)
        x_zo = np.array(x_zo)
        y_zo = np.array(y_zo)
        xt_zo = np.array(xt_zo)
        yt_zo = np.array(yt_zo)
        return x_zo, y_zo, xt_zo, yt_zo
    
    def getdata(self,a,b,img_rows = 28, img_cols = 28):
    # the data, split between train and test sets
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_zo = []
        y_zo = []
        for i in range(len(y_train)):
            if y_train[i] == a or y_train[i] == b:
                A = resize(x_train[i], (img_rows,  img_cols),mode='constant')
                Ay = y_train[i]#resize(y_train[i], (img_rows, img_cols))
                x_zo.append(A)
                y_zo.append(Ay)
        xt_zo = []
        yt_zo = []
    
        for i in range(len(y_test)):
            if y_test[i] == a or y_test[i] == b:
                A = resize(x_test[i], (img_rows,  img_cols),mode='constant')
                Ay = y_test[i]#resize(y_train[i], (img_rows, img_cols))
                xt_zo.append(A)
                yt_zo.append(Ay)
        x_zo = np.array(x_zo)
        y_zo = np.array(y_zo)
        xt_zo = np.array(xt_zo)
        yt_zo = np.array(yt_zo)
        return x_zo, y_zo, xt_zo, yt_zo
    def getdata2(self,a,b,img_rows = 28, img_cols = 28):
    # the data, split between train and test sets
        x_train = self.load('kmnist-train-imgs.npz')
        x_test = self.load('kmnist-test-imgs.npz')
        y_train = self.load('kmnist-train-labels.npz')
        y_test = self.load('kmnist-test-labels.npz')
        x_zo = []
        y_zo = []
        for i in range(len(y_train)):
            if y_train[i] in [0,1,2,3,4,5,6,7,8,9]:
                A = resize(x_train[i], (img_rows,  img_cols),mode='constant')
                Ay = y_train[i]#resize(y_train[i], (img_rows, img_cols))
                x_zo.append(A)
                y_zo.append(Ay)
        xt_zo = []
        yt_zo = []
    
        for i in range(len(y_test)):
            if y_train[i] in [0,1,2,3,4,5,6,7,8,9]:
                A = resize(x_test[i], (img_rows,  img_cols),mode='constant')
                Ay = y_test[i]#resize(y_train[i], (img_rows, img_cols))
                xt_zo.append(A)
                yt_zo.append(Ay)
        x_zo = np.array(x_zo)
        y_zo = np.array(y_zo)
        xt_zo = np.array(xt_zo)
        yt_zo = np.array(yt_zo)
        return x_zo, y_zo, xt_zo, yt_zo    
    def trainDense(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        nm=Sequential()
        nm.add(Flatten(input_shape=(img_rows, img_cols,1), name = "Input"))
        nm.add(Dense(49, activation='relu' ,name = "H1"))
        #nm.add(Dense(49, activation='relu' ,name = "H2"))
        nm.add(Dense(numclass, activation='softmax' ,name = "output"))
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        #print(nm.summary())
        nm.fit(x_train, y_train, epochs=ep)
        return nm, x_test, y_test
    def trainDense2(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        nm=Sequential()
        nm.add(Flatten(input_shape=(img_rows, img_cols,1), name = "Input"))
        nm.add(Dense(49, activation='relu' ,name = "H1"))
        nm.add(Dense(49, activation='relu' ,name = "H2"))
        nm.add(Dense(numclass, activation='softmax' ,name = "output"))
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        #print(nm.summary())
        nm.fit(x_train, y_train, epochs=ep)
        return nm, x_test, y_test
    def trainDense3(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        nm=Sequential()
        nm.add(Flatten(input_shape=(img_rows, img_cols,1), name = "Input"))
        nm.add(Dense(49, activation='relu' ,name = "H1"))
        nm.add(Dense(49, activation='relu' ,name = "H2"))
        nm.add(Dense(49, activation='relu' ,name = "H3"))
        nm.add(Dense(numclass, activation='softmax' ,name = "output"))
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        #print(nm.summary())
        nm.fit(x_train, y_train, epochs=ep)
        return nm, x_test, y_test
    def trainDense4(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        nm=Sequential()
        nm.add(Flatten(input_shape=(img_rows, img_cols,1), name = "Input"))
        nm.add(Dense(49, activation='relu' ,name = "H1"))
        nm.add(Dense(49, activation='relu' ,name = "H2"))
        nm.add(Dense(49, activation='relu' ,name = "H3"))
        nm.add(Dense(49, activation='relu' ,name = "H4"))
        nm.add(Dense(numclass, activation='softmax' ,name = "output"))
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        #print(nm.summary())
        nm.fit(x_train, y_train, epochs=ep)
        return nm, x_test, y_test
    def trainData(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        # nm = keras.Sequential([
        #     keras.layers.Flatten(input_shape=(img_rows, img_cols,1), name = "Input"),
        #     keras.layers.Dense(49, activation=tf.nn.relu ,name = "H"),
        #     keras.layers.Dense(numclass, activation=tf.nn.softmax, name = "output")
        # ])
    
        # nm.compile(optimizer='adam',
        #               loss='sparse_categorical_crossentropy',
        #               metrics=['accuracy'])
        # print(nm.summary())
        # nm.fit(x_train, y_train, epochs=ep)
        return x_test, y_test,x_train, y_train