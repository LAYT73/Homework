import turtle as t
import time
from random import randint
rand = 0 # Переменная для дальнейшего случайного выбора цвета для закрашивания

#Функция для создание окружности и смещения на координаты начала следующей окружности
def circle_func(index, angle): #Index - номер окружности; Angle - Угол для диагонали (90 - От левого верхнего До правого нижнего; 270 - От правого верхнего До левого нижнего)
    t.begin_fill()

    #Создаем случайное закрашивание при помощи условных операторов
    rand = randint(0,1)
    if rand == 0: #Условный оператор для случайного выбора цвета закрашивания
        t.color('black', 'black')
    else:
        t.color('black', 'white')


    if index != 8: #Исключаем этим условие центральную окружность для второй диагонали
        t.circle(35)


    t.end_fill()

    #Смещение после окружности на координаты след. окружности
    if index != 5 and index != 10: #Условие не дает после создание посл-их окружностей делать смещение
        t.begin_fill()
        t.color('white')
        t.forward(140)
        t.end_fill()
        t.begin_fill()
        t.color('white')
        t.right(angle)
        t.forward(140)
        t.left(angle)
        t.end_fill()
        return counter


#Переносим Pointer в левый верхний угол и устанавливаем на начало первой окружности
t.color('white', 'white')
t.speed(10)
t.begin_fill()
t.left(90)
t.forward(350)
t.left(90)
t.forward(350)
t.left(90)
t.forward(70)
t.left(90)
t.end_fill()


#Создаем первые 5 окружностей по диагонали
for index in range(1,6):
    circle_func(index, 90)

#Переносим Pointer в правый верхний угол на начало первой окружности второй диагонали

t.begin_fill()     #Эта часть отвечает за обход последней окружности
t.color("white")   #Если пересекать окружность напрямую, то есть шанс что при рандомном закрашивании вдоль окружности появится вертикальная полоса другого цвета
t.forward(35)
t.left(90)
t.end_fill()
t.begin_fill()
t.forward(70)
t.end_fill()
t.begin_fill()
t.left(90)
t.forward(35)
t.end_fill()

#Правый верхний угол
t.begin_fill()
t.right(90)
t.forward(560)
t.left(90)
t.end_fill()

#Цикл для последних 4х окружностей (4 потому что центральный уже был создан предыдущей диагональю)
for index in range(6,11):
    circle_func(index, 270)

#Таймер для того чтобы успеть посмотреть результат программы (В секундах)
time.sleep(10)
