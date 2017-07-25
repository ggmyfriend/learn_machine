import copy
#traing set
postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]

classVec = [0,1,0,1,0,1]#1 侮辱性文字 ， 0 代表正常言论

def freshTheDict():   #清空字典并给出测试样本的一个字典
    dic = {}
    for i in range(postingList.__len__()):
        for j in range(postingList[i].__len__()):
            dic[postingList[i][j]]=0
    return dic


def naive_bayes(dic):            #计算p(x|y=?)
    dic_yes = copy.deepcopy(dic)    #每个字在p(x|y=1)的概率   注意不能dic_yes = dic 且dic_no=dic 属于浅拷贝
    dic_no = copy.deepcopy(dic)    #每个字在p(x|y=0)的概率
    a=0
    b=0
    for i in range(classVec.__len__()):
       if(classVec[i]==1):
           a=a+1
       else:
           b=b+1
    for i in dic.keys():
        c=0
        d=0
        for j in range(postingList.__len__()):
            if(i in postingList[j] and classVec[j]==1):
                c=c+1
            if(i in postingList[j] and classVec[j]==0):
                d=d+1
        dic_yes[i]=(c+1)/(a+2) #拉普拉斯平滑
        dic_no[i]=(d+1)/(b+2)
        print(a,b,dic.__len__(),c, d,dic_yes[i],dic_no[i])
    return dic_yes,dic_no

def cal_p_y():        #算出p(y=？)的概率
    a = 0
    b = 0
    for i in range(classVec.__len__()):
        a = a + 1
        if (classVec[i] == 1):
            b = b + 1
    p_y1 = b / a
    p_y2 = (a-b)/a
    return p_y1,p_y2

str1 = input("输入语言")
str1 = str1.split(" ")
dic1 = freshTheDict()
p_y1,p_y2 = cal_p_y()
dic1_yes,dic1_no = naive_bayes(dic1)
print(dic1_yes,dic1_no,sep="\n")
#计算最后一个样本的概率
EqualsOne=p_y1
EqualsZero=p_y2
for i in str1:
    EqualsOne = EqualsOne * dic1_yes[i]
    EqualsZero = EqualsZero * dic1_no[i]
    print(dic1_yes[i],dic1_no[i],sep=" ")
print(EqualsOne,EqualsZero,p_y1,p_y2)
if(EqualsZero>EqualsOne):
    print(0)
else:
    print(1)
