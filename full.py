from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import mglearn
import pandas as pd
import random


max0 = [0, 0, 0, 0]
min0 = [10, 10, 10, 10]
max1 = [0, 0, 0, 0]
min1 = [10 ,10, 10, 10]
max2 = [0, 0, 0, 0]
min2 = [10, 10, 10, 10]
p_ta = []
p_tt = []
for i in range(len(y_train)):
    if y_train[i] == 0:
        max0 = [max(max0[0], x_train[i][0]), max(max0[1], x_train[i][1]), max(max0[2], x_train[i][2]), max(max0[3], x_train[i][3])]
        min0 = [min(max0[0], x_train[i][0]), min(max0[1], x_train[i][1]), min(max0[2], x_train[i][2]), min(max0[3], x_train[i][3])]
    if y_train[i] == 1:
        max1 = [max(max1[0], x_train[i][0]), max(max1[1], x_train[i][1]), max(max1[2], x_train[i][2]), max(max1[3], x_train[i][3])]
        min1 = [min(max1[0], x_train[i][0]), min(max1[1], x_train[i][1]), min(max1[2], x_train[i][2]), min(max1[3], x_train[i][3])]
    if y_train[i] == 2:
        max2 = [max(max2[0], x_train[i][0]), max(max2[1], x_train[i][1]), max(max2[2], x_train[i][2]), max(max2[3], x_train[i][3])]
        min2 = [min(max2[0], x_train[i][0]), min(max2[1], x_train[i][1]), min(max2[2], x_train[i][2]), min(max2[3], x_train[i][3])]
for i in range(5000):
    q = random.randint(0, 3)
    if q == 0:
        p_tt.append([random.randint(int(min0[0]*100), int(max0[0]*100))/100, random.randint(int(min0[1]*100), int(max0[1]*100))/100, random.randint(int(min0[2]*100), int(max0[2]*100))/100, random.randint(int(min0[3]*100), int(max0[3]*100))/100])
        p_ta.append(0)
    if q == 1:
        p_tt.append([random.randint(int(min1[0]*100), int(max1[0]*100))/100, random.randint(int(min1[1]*100), int(max1[1]*100))/100, random.randint(int(min1[2]*100), int(max1[2]*100))/100, random.randint(int(min1[3]*100), int(max1[3]*100))/100])
        p_ta.append(1)
    if q == 2:
        p_tt.append([random.randint(int(min2[0]*100), int(max2[0]*100))/100, random.randint(int(min2[1]*100), int(max2[1]*100))/100, random.randint(int(min2[2]*100), int(max2[2]*100))/100, random.randint(int(min2[3]*100), int(max2[3]*100))/100])
        p_ta.append(2)
x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
def calculator(res1, res2, res3, res4):
    l = list()
    for i in x_train:
        l.append(((i[2] - res3)**2 + (i[3] - res4)**2)**0.5)
    at = l.index(min(l))
    aa = y_train[at]
    at = l[at]
    l.remove(at)
    bt = l.index(min(l))
    ba = y_train[bt]
    bt = l[bt]
    l.remove(bt)
    ct = l.index(min(l))
    ca = y_train[ct]
    ct = l[ct]
    l.remove(ct)
    if ca != ba and aa != ca and ba != ca:
        return aa
    elif ba == aa or ba == ca:
        return ba
    elif aa == ca:
        return aa
count = 0
c = 0
for i in x_test:
    q = calculator(i[0], i[1], i[2], i[3])
    if q == y_test[count]:
        c += 1
    count += 1
print(c/count)
