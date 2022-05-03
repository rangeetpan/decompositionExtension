from utils.mnistutil import MNISTUitl
from Reuse import Reuse
from sklearn.metrics import accuracy_score
from keras.datasets import mnist

# In[]
sx = 28
sy = 28
accuracyCheck=[]
labs = [0,1,2,3,4,5,6,7,8]
mn = MNISTUitl()
ru=Reuse()
#x_train = mnist.load_data('kmnist-train-imgs.npz')
#x_test = mnist.load_data('kmnist-test-imgs.npz')
#y_train = mnist.load_data('kmnist-train-labels.npz')
#y_test = mnist.load_data('kmnist-test-labels.npz')
X, Y, x, y = mn.getdata2(0,0,sx,sy)
#xt, yt, xT, yT = mn.trainData(X, Y, x,y,sx,sy,9,50)
# In[]
for i in range(10):
    cl=i
    Xtt, Ytt, xtt, ytt = mn.getdata50(X, Y, x, y,cl,sx,sy)
    nm , xttt, yttt = mn.trainDense2(Xtt, Ytt, xtt,ytt,sx,sy,2,50)
    nm.save('module'+str(cl)+'.h5')
xt, yt, xT, yT = mn.trainData(X, Y, x,y,sx,sy,9,50)
ru.reuseModule(xt, yt, xT, yT)