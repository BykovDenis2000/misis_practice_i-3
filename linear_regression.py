import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data.csv', parse_dates=[0])
train, test = train_test_split(data, test_size=0.2) #разбиваем на обучающую и тестовую выборку

real_features = ['meanWidth', 'meanHeight', 'meanLength', 'meanVolume', 
                 'countStacking', 'countTurnover', 'boxesCount', 
                 'loadingWidth', 'loadingWidth', 'loadingLength']  # вещественные признаки
target_feature = 'density_percent'  # целевой признак

model = LinearRegression(fit_intercept=True)  # объявляем модель
model.fit(train[real_features], train[target_feature])  # обучаем

print('Оценки коэффициентов перед признаками\n', model.coef_)

print('Оценка свободного коэффициента\n', model.intercept_)

test_preds = model.predict(test[real_features])

print('MSE = ', round(np.sqrt(((test[target_feature] - test_preds) ** 2).mean()), 2))

def mean_absolute_percentage_error(y_true, y_pred):
    return 100 * (np.abs(y_true - y_pred) / y_true).mean()
print('MAPE = ', round(mean_absolute_percentage_error(test[target_feature], test_preds), 2))
