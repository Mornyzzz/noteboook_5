import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn import metrics


url = r'https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv'
dataset = pd.read_csv(url)
dataset.head()

print(dataset.shape)
dataset.describe()

# Нарисуем точечную диаграмму
plt.scatter(dataset['density'], dataset['alcohol'], color = 'b', label = "Заработная плата")
plt.xlabel("density")
plt.ylabel("alcohol")
plt.show()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
#print(X)
#print(y)

# Теперь, когда у нас есть атрибуты и метки, необходимо разделить их на а обучающий и тестовый наборы. # Приведенный фрагмент разделяет 80% данных на обучающий набор, а 20% данных - на набор тестоб
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# далее можно обучить алгоритм линейной регрессии
# необходимо импортировать класс LinearRegression, создать его экземпляр и вызвать метод fit()
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)

tree.plot_tree(regressor)
y_pred = regressor.predict(X_test)
#print(y_pred)

df = pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})
print(df)

print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Error %: ', metrics.mean_absolute_error(y_test, y_pred) / np.average(y) * 100)