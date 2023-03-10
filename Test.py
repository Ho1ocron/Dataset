from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import mglearn
import pandas as pd
import copy

iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)

list0 = []
k = 1
x = 0

print(
    f"Train 0: {((X_train[0][0] - X_train[1][0])**2 + (X_train[0][1] - X_train[1][1])**2 + (X_train[0][2] - X_train[1][2])**2 +(X_train[0][3] - X_train[1][3])**2)**0.5}")
for i in range(len(X_train)):
    if x == 3:
        x = 0
    try:
        list0.append(((X_train[0][x] - X_train[k][x])**2 + (X_train[0][x+1] - X_train[k][x+1])**2 + (X_train[0][x+2] - X_train[k][x+2])**2 + (X_train[0][x+3] - X_train[k][x+3])**2)**0.5)
    except:
        #print(list0)
        break
    k+=1
list1 = copy.deepcopy(sorted(list0))
list3 = []
list3.append(list1[0])
list3.append(list1[1])
list3.append(list1[2])
print(f"Ближайшие точки к первой точке: \n", *list3)


def search(list_in, list_s):
    q = -1
    for i in list_in:
        q+=1
        if i == list_s:
            return q


x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

#print(f"x_train: \n{x_train}, \nx_test: \n{x_test}, \ny_train: \n{y_train}, \ny_test: \n{y_test}")

def dataset(list0, list3, y_train):
    result = search(list0, list3[0])
    result1 = search(list0, list3[1])
    result2 = search(list0, list3[2])
    #print(result, result1, result2)
    print(y_train[result])
    print(y_train[result1])
    print(y_train[result2])
    if y_train[result] == y_train[result1] == y_train[result2]:
        print(f"Точка относится к цветку {y_train[result]}")
        


dataset(list0, list3, y_train)