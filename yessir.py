import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('StudentPerfomace.csv')
df.info()
print(df.head())
print(df['parental level of education'].value_counts())
print('Кто умнее мальчиики или девочки')

men_math_result = df[df['gender']=='male']['math score'].mean()
women_math_result = df[df['gender']=='female']['math score'].mean()
men_reading_result = df[df['gender']=='male']['reading score'].mean()
women_reading_result = df[df['gender']=='female']['reading score'].mean()
men_writing_result = df[df]['gender']=='male'['writing score'].mean()
women_writing_result = df[df]['gender']=='female'['writing score'].mean()

female_free = 0
female_standart = 0

def lunch_counter(row):
    global female_free, female_standart
    if row['gender'] == 'female' and row['lunch'] == 'standart':
        female_standart+=1
    if row['gender'] == 'female' and row['lunch'] == 'free/reduced':
        female_free+=1
    return False

df.apply(lunch_counter, axis = 1)
print(female_free, female_standart)


print('Рзультат парней по математике:', round(men_math_result, 2))
print('Рзультат девушек по математике:', round(women_math_result, 2))
print('Рзультат парней по чтению:', round(men_reading_result, 2))
print('Рзультат девушек по чтению:', round(women_reading_result, 2))
print('Рзультат парней по письму:', round(men_writing_result, 2))
print('Рзультат девушек по письму:', round(women_writing_result, 2))

print('ДЕвочки сильнее в гуманитарных науках, а мальчики в точных науках')

print('Влияет ли качество питания на результаты теста?')
standart_math = df[df['lunch']=='standart']['math score'].mean()
free_math = df[df['lunch']=='free/reduced']['math score'].mean()
standart_reading = df[df['lunch']=='standart']['reading score'].mean()
free_reading = df[df['lunch']=='free/reduced']['reading score'].mean()
standart_writing= df[df['lunch']=='standart']['writing score'].mean()
free_writing = df[df['lunch']=='free/reduced']['writing score'].mean()

print('Результат по математике:', 'Стандарт', round(standart_math, 2), 'Бесплатное:', round(free_math, 2))
print('Результат по чтению:', 'Стандарт', round(standart_reading, 2), 'Бесплатное:', round(free_reading, 2))
print('Результат по письму:', 'Стандарт', round(standart_writing, 2), 'Бесплатное:', round(free_writing, 2))

print('Гипотеза подтверждена. Питание влияет на качество обучения')

genders = df['gender'].value_counts()
genders.plot(kind = 'pie')
plt.show()
s = pd.Series(data=[men_math_result, women_math_result, men_reading_result, women_reading_result, men_writing_result, women_writing_result])
index = ['Математика парни', 'Математика девочки', 'Чтение парни', 'Чтение девочки', 'Письмо парни', 'Письмо девочки'])
s.plot(kind = 'barh')
plt.show()









