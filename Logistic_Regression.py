import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import re
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
def read_test(name):
    f = open(name,"r")
    a = f.readline()
    test_number = {}
    b=0
    while a:
        test_number[b]=a
        a = f.readline()
        b=b+1
    return test_number,b

def get_test_train(train_set,length):
    print("this is in get_test_train fuction")
    train_para=[]
    train_res=[]
    for i in range(length):
        x = re.split("\s+",train_set[i])
        train_para.append((float(x[0]),float(x[1])))
        train_res.append(float(x[2]))
    return train_para,train_res

def function_Logistic(a,b,x):
    return 1.0/(1+exp(-a*x[0]-b*x[1]))

x , length  = read_test("E:\pythonFile\machine_learning\logistic_regression_testset.txt")
train_para,train_res=get_test_train(x,length)
foot = 0.001
print("this is main")
a = np.random.normal()
b = np.random.normal()

for i in range(500):
    sum_a = 0
    sum_b = 0
    for x,y in zip(train_para,train_res):
        sum_a = sum_a + foot*(y-function_Logistic(a,b,x))*x[0]
        sum_b = sum_b + foot*(y-function_Logistic(a,b,x))*x[1]
    a = a + sum_a
    b = b + sum_b

test_num = function_Logistic(a,b,[1,1])
print(test_num)


for x,y in zip(train_para,train_res):
    if(y==1):
        ax.scatter(x[0],x[1],y,color="red")
    else:
        ax.scatter(x[0],x[1],y,color="yellow")
print(a,b)
ax.plot([x[0] for x in train_para],[x[1] for x in train_para],[function_Logistic(a,b,x) for x in train_para])
plt.show()


#输出为2维表可能需要降维
