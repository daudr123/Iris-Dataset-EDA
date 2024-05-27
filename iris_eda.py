# -*- coding: utf-8 -*-
"""Iris_EDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g1YxmLHp3sETkmH5IhPt5nFnjRQpvbPQ
"""

from google.colab import drive
drive.mount('/content/drive')

"""# Importing Libraries"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

"""# Importing Iris Dataset

Importing the dataset and creating a dataframe, printing the head to see the dataset.
"""

orig_df = pd.read_csv("/content/drive/MyDrive/csv_files/Iris.csv")
df = orig_df
df.head()

"""Printing the shape to see the size of the dataset"""

df.shape

"""Checking info of the dataframe"""

df.info()

"""# Cleaning and preprocessing

Renaming the columns.
"""

df = df.rename(columns={
                        'Id':'id',
                        'SepalLengthCm':'sepal_length_cm',
                        'SepalWidthCm':'sepal_width_cm',
                        'PetalLengthCm':'petal_length_cm',
                        'PetalWidthCm':'petal_width_cm',
                        'Species':'species'
                        })

"""checking for null values"""

df.isnull().sum()

"""Since there are no null values and the dataset is clean we will look at the dataset using describe"""

df.describe()

"""Now we will look at any duplicates in dataframe since our dataset is small."""

data = df.drop_duplicates(subset ="species",)
data

df['species'].unique()

"""Since we know that there are three species categories we will find the counts of each species"""

df.value_counts('species')

"""# Visualisation of the dataset

Now we will try to visualise our dataset using sns and matplotlib libraries. Our goal is to observe relationship between the variables
"""

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='species',data=df, palette = 'Set1')

plt.title('Counts of species')
plt.show()

"""Now we will observe the relationship between sepal length and sepal width and also followed by petal length and petal width

"""

sns.scatterplot(x = 'sepal_length_cm', y = 'sepal_width_cm', hue = 'species', data = df,)
plt.legend(bbox_to_anchor=(1,1),loc=2)
plt.title('Sepal width Vs Sepal Length', size = 16)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')


plt.show()

"""The key observations from this scatter plot


*   Setosa species has smaller Sepal length but larger Sepal Width
*   Versicolor lies in the middle of both and tends to have generally lower width and higher length.
* Virginica species has larger lengths but smaller widths.

Now we will be comparing the petal lengths and width similarly





"""

sns.scatterplot(x = 'petal_length_cm', y = 'petal_width_cm', hue = 'species', data = df,)
plt.legend(bbox_to_anchor=(1,1),loc=2)
plt.title('Petal width Vs Petal Length', size = 16)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')


plt.show()

"""As we can observe, there is clear distinction between petal lengths and widths of each species

* Setosa has the smallest petal length and width
*Versicolor lies in the middle but has bigger petals than setosa
*Virginica has the biggest petals both in terms of petal length and width

Now we will make use of pair plots to compare the the relationships for multivariate analysis

"""

sns.pairplot(df.drop(['id'],axis =1),
             hue = 'species',height = 2)

"""There are some clear observations that can be made here, the species setosa has the smallest overall petal lengths and widths, it also has smaller sepal lengths but greater sepal widths. Virginica tends to have generally bigger lengths and widths than the other categories.

# Histograms

the use of histograms will allow us to see the distributio of data for various columns, it can be used for uni as well as bi variate analysis.
"""

fig, axes = plt.subplots(2,2,figsize=(10,10))

axes[0,0].set_title('Sepal Length')
axes[0,0].hist(df['sepal_length_cm'],bins=7)

axes[0,1].set_title('Sepal Width')
axes[0,1].hist(df['sepal_width_cm'],bins=5)

axes[1,0].set_title('Petal Length')
axes[1,0].hist(df['petal_length_cm'],bins=6)

axes[1,1].set_title('Petal Width')
axes[1,1].hist(df['petal_width_cm'],bins=6)

"""There are a few key observations to be made here


*   The highest sepal length lies between 30-35 which is between 5.5-6
*  The highest sepal width is around 70 which is betwen 3-3.5
*The highest petal length is around 50 which is around 1-2
*The highest frequency of Petal width is between 40-50 which is between 0.0-0.05.

# Histograms and Distplots
Distplot is used basically for the univariant set of observations and visualizes it through a histogram i.e. only one observation and hence we choose one particular column of the dataset.
"""

plot = sns.FacetGrid(df,hue='species')
plot.map(sns.distplot,"sepal_length_cm").add_legend()

plot = sns.FacetGrid(df,hue='species')
plot.map(sns.distplot,"sepal_width_cm").add_legend()

plot = sns.FacetGrid(df,hue='species')
plot.map(sns.distplot,"petal_length_cm").add_legend()

plot = sns.FacetGrid(df,hue='species')
plot.map(sns.distplot,"petal_width_cm").add_legend()

plt.show()

"""From the above plots, we can see that –

* In the case of Sepal Length, there is a huge amount of
overlapping.
* In the case of Sepal Width also, there is a huge amount of overlapping.
* In the case of Petal Length, there is a very little amount of overlapping.
* In the case of Petal Width also, there is a very little amount of overlapping.

So we can use Petal Length and Petal Width as the classification feature.

# Finding Correlation

We will use heatmaps to find the correlation.
"""

print(data.dtypes)

data = data.drop('species', axis=1)

data.corr(method='pearson')

"""The heatmap is a data visualization technique that is used to analyze the dataset as colors in two dimensions. Basically, it shows a correlation between all numerical variables in the dataset. In simpler terms, we can plot the above-found correlation using the heatmaps."""

new_df = df.drop('species', axis=1)
sns.heatmap(new_df.corr(method='pearson').drop(['id'],axis = 1).drop(['id'],axis = 0),annot = True);
plt.show()

"""We can observe that:

*   Petal lenght and petal width have high correlation
*   Petal len and sepal len have high corr
*   Petal width and sepal len have a good corr



Now moving on to box plots

# Box Plots

We can use boxplots to see how the categorical value os distributed with other numerical values.
"""

def graph(y):
  sns.boxplot(x = "species", y=y, data = df)
plt.figure(figsize = (10,10))

plt.subplot(221)
graph('sepal_length_cm')

plt.subplot(222)
graph('sepal_width_cm')

plt.subplot(223)
graph('petal_length_cm')

plt.subplot(224)
graph('petal_width_cm')

plt.show()

"""* Species Setosa has the smallest features and less distributed with some outliers.
* Species Versicolor has the average features.
* Species Virginica has the highest features

However this has outliers and outliers can deviate us from the actual results. Hence they should be removed or dropped or capped off to get more accurate results

# Handling Outliers
"""

sns.boxplot(x = 'sepal_width_cm', data=df)

"""The values above 4 and below 2 are acting as outliers.

We must remove the outliers

we can do this by examining the IQR
"""

import sklearn

q1 = np.percentile(df['sepal_width_cm'],25, interpolation = 'midpoint')
q3 = np.percentile(df['sepal_width_cm'],75,interpolation = 'midpoint')

IQR = q3-q1

print('Old Shape: ', df.shape)

upper = np.where(df['sepal_width_cm'] >= (q3 + 1.5*IQR))

lower = np.where(df['sepal_width_cm'] <= (q1 - 1.5*IQR))

df.drop(upper[0],inplace = True)
df.drop(lower[0], inplace = True)

print('New Shape: ',df.shape)

sns.boxplot(x = 'sepal_width_cm', data = df)

"""Hence we can observe that the outliers in the sepal width have been removed and the new box plot seems better than the original one."""