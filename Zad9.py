import numpy as np
import pandas as pd

#зАюзать replace на замену знаков


rows = int(input()) # Создание и заполнение матрицы

cols = int(input())

matrix = []
for i in range(rows):
	row = []
	for j in range(cols):
		str = input()
		row.append(str)
	matrix.append(row)

#print(matrix)
#print("//////////////")


#Преобразования

#Транспонирование матрицы
for i in matrix:
	if matrix.count(i) > 1: #Проверка на повторы
		matrix.remove(i) # Удаление повторов
		#new.append(i)
t_mat = matrix
new = np.transpose(matrix)
print(new, '\n', 'Транспонирована')# Вывод матрицы без повторов и её транспонир

print("//////////////")


# заменить - на / 1 и 0 на да и нет
# заменить 2747169496 на 274 716-9496
# заменить vesuk53@yandex.ru на vesuk53

# Замена данных в матрице

print("Замена")
a = np.shape(new)
value1 = a[0]
value2 = a[1]
for i in t_mat:
		if t_mat.count(i) == '1':
			i = 'да'
		else:
			i = 'нет'
print(t_mat)
# матрица 4 на 3



'''
f = []
for k in matrix:
	b = 0
	for h in matrix:
		if k == h:
			b += 1
	if b == 1:
		f.append(k)
print(f)
'''

'''
#new = f'{matrix}'
#print(np.unique(new, return_counts=True))
 # '%s' %  | f'{_}'
'''




'''
list = []# Заполнение массива
n = int(input())
for i in range(0, n):
	stroka = input()
	list.append(stroka)
print(list)
'''

