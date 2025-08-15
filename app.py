import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# Нулевая гипотиза H0: Количество событий в группах control и test не изменились
data = pd.read_csv('./data/user_event_data_streaming_mini.csv')
 
prices = {
    'renew': 9.99,
    'purchase_annual': 89.99,
    'purchase_quarterly': 27.99,
    'purchase_monthly': 9.99,
}
data['cost'] = data['event'].map(prices).fillna(0)
# Показать всю таблицу: pd.set_option('display.max_rows', None)

def user_contribution(group: str):
    users = data[(data['group'] == group)].copy()
    users_ltv = users.groupby('user_id')['cost'].sum().reset_index()
    return users_ltv

control_users_contribution = user_contribution('control')
test_users_contribution = user_contribution('test')

def conversion_rate(data_contribution):
    users = len(data_contribution)
    buyers = len(data_contribution[data_contribution['cost'] > 0])
    conversion_rate = buyers/users
    return conversion_rate

# def zero_hypothesis(event: str):
#     control_count = control_events[event]
#     test_count = test_events[event]

#     stat, p_value = proportions_ztest([control_count, test_count], [total_control, total_test])

#     print(f"Для {event}: Z-статистика: {stat}, p-значение: {p_value}")

#     alpha = 0.05
#     if p_value < alpha:
#         print("Отвергаем нулевую гипотезу, группы различаются. \n")
#     else:
#         print("Не отвергаем нулевую гипотезу, различий нет. \n")
# # Подсчет количества событий для каждой группы
# control_events = data[data['group'] == 'control']['event'].value_counts()
# test_events = data[data['group'] == 'test']['event'].value_counts()

# # Общее количество пользователей в каждой группе
# total_control = data[data['group'] == 'control'].shape[0]
# total_test = data[data['group'] == 'test'].shape[0]

# unique_events = data['event'].unique()

# for event in unique_events:
#     zero_hypothesis(event)