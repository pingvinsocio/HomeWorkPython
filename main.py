# Знакомство с языком Python (семинары)
# Урок 10. Построение графиков
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# Метод astype() Метод astype в библиотеке pandas используется для преобразования типов данных в столбцах данных.
# В даннм случае мы преобразоваем логические значения
# (True/False) в целочисленные значения (1/0).

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.DataFrame()
one_hot['robot'] = (data['whoAmI'] == 'robot').astype(int)
one_hot['human'] = (data['whoAmI'] == 'human').astype(int)


one_hot.to_csv('csv.csv')
print(one_hot.head(20))