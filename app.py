import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# Нулевая гипотиза H0: Количество событий в группах control и test одинаково
data = pd.read_csv('./data/user_event_data_streaming_mini.csv')

# Подсчет количества событий для каждой группы
control_events = data[data['group'] == 'control']['event'].value_counts()
test_events = data[data['group'] == 'test']['event'].value_counts()

print(control_events, test_events)

# Количество событий в каждой группе
control_count = control_events['add_to_playlist']
test_count = test_events['add_to_playlist']

# Общее количество пользователей в каждой группе
total_control = data[data['group'] == 'control'].shape[0]
total_test = data[data['group'] == 'test'].shape[0]

# Проведение z-теста
stat, p_value = proportions_ztest([control_count, test_count], [total_control, total_test])

print(f"Z-статистика: {stat}, p-значение: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Отвергаем нулевую гипотезу, группы различаются.")
else:
    print("Не отвергаем нулевую гипотезу, различий нет.")