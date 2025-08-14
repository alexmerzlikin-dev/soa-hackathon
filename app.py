import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# Нулевая гипотиза H0: Количество событий в группах control и test не изменились
data = pd.read_csv('./data/user_event_data_streaming_mini.csv')
data_unique = data['user_id'].unique()
print(data_unique)

# Подсчет количества событий для каждой группы
control_events = data[data['group'] == 'control']['event'].value_counts()
test_events = data[data['group'] == 'test']['event'].value_counts()

# Общее количество пользователей в каждой группе
total_control = data[data['group'] == 'control']
total_test = data[data['group'] == 'test']

def zero_hypothesis(event: str):
    control_count = control_events[event]
    test_count = test_events[event]

    stat, p_value = proportions_ztest([control_count, test_count], [total_control, total_test])

    print(f"Для {event}: Z-статистика: {stat}, p-значение: {p_value}")

    alpha = 0.05
    if p_value < alpha:
        print("Отвергаем нулевую гипотезу, группы различаются. \n")
    else:
        print("Не отвергаем нулевую гипотезу, различий нет.\n")

unique_events = data['event'].unique()

for event in unique_events:
    zero_hypothesis(event)