# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

print('введите количество элементов масива :')
N = int(input())
if N == 0:
    print("В массиве должен присутствовать хотя бы один элемент! ")
    exit()

A = [] # базовый массив

for i in range(N):
    flag = True
    print("Введите элемент массива N(",i,") :")
    while flag==True:
        k = (input())
        if k.isnumeric(): 
            flag = False
        else:
            print("Неправильный ввод - попробуйте снова (N(i) должно быть целым числом)")
    k = int(k)
    A.append(k)

print("введите min и max для поиска индексов в диапозоне чисел:")
max = int(input("max ="))
min = max + 1
while max < min:
    min = int(input("min ="))
    if max < min :
        print("max должно быть больше min")

for i in range(N):
    if A[i] >= min and A[i] <= max:
        print("i =",i)