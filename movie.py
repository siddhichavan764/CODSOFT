import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./IMDb_Movies_India.csv', encoding='latin-1')
data.head(10)

data.tail(10)

data.shape

data.info()

data.describe()

data.isnull().sum()

data.dropna(inplace=True)

data.isnull().sum()

data.duplicated().sum()

data.drop_duplicates(inplace=True)

data.duplicated().sum()

data.shape

data.describe(include='all')

data.columns
data['Duration'] = pd.to_numeric(data['Duration'], errors='coerce')
data[data['Duration'] >= 140]['Name']
data.columns
data['Votes'] = data['Votes'].str.replace(',','').astype(int)
data.groupby('Year')['Votes'].mean().sort_values(ascending=False)

sns.barplot(x= 'Year',y= 'Votes', data=data)

plt.title('Votes by Year')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

data.columns
data.groupby('Director')['Rating'].mean().sort_values(ascending=False)

top10_len=data.nlargest(10,'Duration')[['Name','Duration']]
top10_len
sns.barplot(x='Name',y='Duration',data=top10_len)
plt.title('Top 10 Movies by Duration')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()
data.columns
data[data['Rating'].max()==data['Rating']]


data.columns
data.groupby('Genre')['Rating'].mean().sort_values(ascending=False)

data.columns
def rating(rating):
  if rating>=7.0:
    return 'Excellent'
  elif rating>=6.0:
    return 'Good'
  elif rating>=5.0:
    return 'Average'
  else:
    return 'Poor'
    data['Rating_good']=data['Rating'].apply(rating)

data.describe()

data.columns
data['Genre'].dtype
len(data[data['Genre'].str.contains('Action',case=False)])

data.columns
data['Genre']
listl=[]
for value in data['Genre']:
  listl.append(value.split(','))
  listl
len(listl)

one_d=[]
for item in listl:
  for item1 in item:
    one_d.append(item1)
    one_d
pd.Series(one_d).value_counts()

uni_list=[]
for item in one_d:
  if item not in uni_list:{
      uni_list.append(item)}

uni_list
pd.Series(uni_list).value_counts()

one_d=[]
for item in listl:
  for item1 in item:
    one_d.append(item1)
    one_d
pd.Series(one_d).value_counts()
from collections import Counter
Counter(one_d)