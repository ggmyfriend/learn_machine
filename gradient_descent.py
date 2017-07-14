import numpy as np
from numpy import *
import matplotlib.pyplot as plt

rate = 0.001  # 梯度下降的步长
# 数据
x_train = np.array([[1, 2], [2, 1], [2, 3], [3, 5], [1, 3], [4, 2], [7, 3], [4, 5], [11, 3], [8, 7]])
y_train = np.array([7, 8, 10, 14, 8, 13, 20, 16, 28, 26])
x_test = np.array([[1, 4], [2, 2], [2, 5], [5, 3], [1, 5], [4, 1]])
# 假设机器学习的J(i)=i1*x1+i2*x2
a = np.random.normal()
b = np.random.normal()
c = np.random.normal()

def h(x):
    return a*x[0]+b*x[1]
#小容量样本比较合适的梯度下 降批梯度下降  梯度下降

for i in range(100):
    sum_a=0
    sum_b=0
    for x, y in zip(x_train, y_train):
        sum_a = sum_a + rate*(y-h(x))*x[0]
        sum_b = sum_b + rate*(y-h(x))*x[1]
    a = a + sum_a
    b = b + sum_b
plt.plot([h(xi) for xi in x_test],color="yellow")
print(a,b,sep="\n")

#样本如果过大可以选择如下的梯度下降算法(随机梯度下降)  但是样本过小偏差很大，需要在考虑应该怎么写以下伪代码
'''
for every x in train{
    chose the next one in x 
    do gradient_descent
}
'''
'''
last_a = a-1
last_b = b-1
time = 0
for i in range(100):
    last_a = a
    last_b = b
    time=time+1
    for x,y in zip(x_train,y_train):
        a = a + rate*(y-h(x))*x[0]
        b = a + rate*(y-h(x))*x[1]

plt.plot([h(xi) for xi in x_test],color="red")
print(a,b)'''
#plt.show()
#不借助迭代求得的梯度下降，函数的参数


#加权梯度下降
#算法是根据所求点的x来使用加权的形式求预测值
#算法比较麻烦所以只写伪代码
'''
number_want为所求值
for i in range(100):
    sum_a=0
    sum_b=0
    sum_c=0
    for x, y in zip(x_train, y_train):
        rate = np.e**(-np.square(x[0]-number_want[0])/2)
        sum_a = sum_a + rate*(y-h(x))*x[0]
        rate = np.e**(-np.square(x[1]-number_want[1])/2)
        sum_b = sum_b + rate*(y-h(x))*x[1]
        rate = 1
        sum_c = sum_c + rate*(y-h(x))
    a = a + sum_a
    b = b + sum_b
    c = c + sum_c
plt.plot([h(xi) for xi in x_test],color="yellow")
'''

matrix1 = mat(x_train)
matrix2 = mat(y_train)

matrix3 = matrix1.T*matrix1
matrix3 = matrix3.I
matrix3 = matrix3*matrix1.T
matrix3 = matrix3*matrix2.T

matrix3 = array(matrix3)
i = matrix3[0]
j = matrix3[1]

def hh(x):
    return i*x[0]+j*x[1]


plt.plot([hh(xi) for xi in x_test],color="blue")

print(i)
print(j)
plt.show()
