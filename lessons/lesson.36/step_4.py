import pandas as pd

salary = [169.5, 211.1, 169.5, 157.3, 541.9]
workers = ['Иван', 'Алиса', 'Боб', 'Иван', 'Петр']
salary_s = pd.Series(salary,
                     index=workers,
                     name='salary',
                     dtype='float32')
print(salary_s)
# print(salary_s[0], salary_s[1])
# print(salary_s[0:3])
# print(salary_s[0::2])
# print(salary_s['Алиса'])
# print(salary_s['Петр'])
print(salary_s['Иван'])
