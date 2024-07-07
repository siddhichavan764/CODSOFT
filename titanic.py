import pandas as pd 
import matplotlib.pyplot as plt


train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')

train.shape
train.describe()

train['Survived'].value_counts()

plt.figure(figsize=(5,5))
plt.bar(list(train['Survived'].value_counts().keys()),list(train['Survived'].value_counts()),color=["r","b"])
plt.show()

train['Pclass'].value_counts()

plt.figure(figsize=(5,5))
plt.bar(list(train['Pclass'].value_counts().keys()),list(train['Pclass'].value_counts()),color=["Purple","pink","orange"])
plt.show()

train['Sex'].value_counts()

plt.figure(figsize=(5,5))
plt.bar(list(train['Sex'].value_counts().keys()),list(train['Sex'].value_counts()),color=["blue","pink"])
plt.show()


plt.figure(figsize=(5,7))
plt.hist(train['Age'])
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.show()

sum(train['Survived'].isnull())
sum(train['Age'].isnull())

train=train.dropna()

sum(train['Survived'].isnull())
sum(train['Age'].isnull())

x_train=train[['Age']]
y_train=train[['Survived']]

from sklearn.tree import DecisionTreeClassifier
dtc =  DecisionTreeClassifier()

dtc.fit(x_train,y_train)

sum(test['Age'].isnull())

test=test.dropna()

sum(test['Age'].isnull())

x_test=test[['Age']]
y_pred=dtc.predict(x_test)
y_pred