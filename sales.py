import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sale = pd.read_csv('./advertising.csv')
sale.head()

sale.info()

sale.describe()

sns.pairplot(sale,x_vars=['TV','Radio','Newspaper'],y_vars='Sales', kind='scatter')

plt.show()

sns.heatmap(sale.corr(), annot=True)

plt.show

sale['TV'].plot.hist(bins=10,color='green')

plt.show()

sale['Radio'].plot.hist(bins=10,color='yellow')

plt.show()

sale['Newspaper'].plot.hist(bins=10,color='orange')

plt.show()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(sale[['TV','Radio','Newspaper']],sale['Sales'],test_size=0.2,random_state=42)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)
res=model.predict(x_test)
print(res)

model.coef_

model.intercept_

model.score(x_test,y_test)


plt.plot(res)
plt.show()

plt.scatter(x_test['TV'],y_test)
plt.show()