#!/usr/bin/env python
# coding: utf-8

# ## Задание 1
# Даны 2 переменных, в которых хранятся строки произвольной длины: **phrase_1** и **phrase_2**.
# Напишите код, который проверяет,какая из этих строк длиннее.

# In[1]:


#Делаю универсальный код, который будет проверять фразы не только из самого задания
phrase_1 = str(input('Введите первую фразу: '))
phrase_2 = str(input('Введите вторую фразу: '))

if phrase_1 > phrase_2:
    print ('Фраза 1 длиннее Фразы 2')
else:
    print ('Фраза 1 короче Фразы 2')


# In[3]:


phrase_1 = str(input('Введите первую фразу: '))
phrase_2 = str(input('Введите вторую фразу: '))

if phrase_1 > phrase_2:
    print ('Фраза 1 длиннее Фразы 2')
    elif phrase_1 == phrase_2:
    print ('Фразы равной длины')
else:
    print ('Фраза 1 короче Фразы 2') 


# In[4]:


phrase_1 = str(input('Введите первую фразу: '))
phrase_2 = str(input('Введите вторую фразу: '))

if phrase_1 > phrase_2:
    print ('Фраза 1 длиннее Фразы 2')
    elif phrase_1 == phrase_2:
    print ('Фразы равной длины')
else:
    print ('Фраза 1 короче Фразы 2') 


# ## Задание 2
# Дана переменная, в которой хранится **четырехзначное число (год)**. Необходимо написать программу, которая выведет, является ли данный год високосным или обычным.

# In[6]:


year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print ("Високосный год") 
else:
    print ("Обычный год") 


# In[7]:


year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print ("Високосный год") 
else:
    print ("Обычный год") 


# ## Задание 3
# Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить соответствующий знак зодиака.

# In[16]:


def program():
    """Print zodiac sigh by setting day and month of birth"""
    day_of_birth = int(input('Введите день: '))
    month_of_birth = str(input('Введите месяц с большой буквы: '))

    if month_of_birth == 'Декабрь' and day_of_birth >= 22 or month_of_birth=='Январь' and day_of_birth<= 19:
        zodiac_sign = ("Козерог")
    elif month_of_birth=='Январь' and day_of_birth >= 20 or month_of_birth=='Февраль' and day_of_birth<= 17:
            zodiac_sign = ("Водолей")
    elif month_of_birth=='Февраль' and day_of_birth >= 18 or month_of_birth=='Март' and day_of_birth<= 19:
            zodiac_sign = ("Рыбы")
    elif month_of_birth=='Март' and day_of_birth >= 20 or month_of_birth=='Апрель' and day_of_birth<= 19:
            zodiac_sign = ("Овен")
    elif month_of_birth=='Апрель' and day_of_birth >= 20 or month_of_birth=='Май' and day_of_birth<= 20:
            zodiac_sign = ("Телец")
    elif month_of_birth=='Май' and day_of_birth >= 21 or month_of_birth=='Июнь' and iday_of_birth<= 20:
            zodiac_sign = ("Дева")
    elif month_of_birth=='Июнь' and day_of_birth >= 21 or month_of_birth=='Июль' and day_of_birth<= 22:
            zodiac_sign = ("Рак")
    elif month_of_birth=='Июль' and day_of_birth >= 23 or month_of_birth=='Август' and day_of_birth<= 22: 
            zodiac_sign = ("Лев")
    elif month_of_birth=='Август' and day_of_birth >= 23 or month_of_birth=='Сентябрь' and day_of_birth<= 22: 
            zodiac_sign = ("Дева")
    elif month_of_birth=='Сентябрь' and day_of_birth >= 23 or month_of_birth=='Октябрь' and day_of_birth<= 22:
            zodiac_sign = ("Весы")
    elif month_of_birth=='Октябрь' and day_of_birth >= 23 or month_of_birth=='Ноябрь' and day_of_birth<= 21: 
            zodiac_sign = ("Скорпион")
    elif month_of_birth=='Ноябрь' and day_of_birth >= 22 or month_of_birth=='Декабрь' and day_of_birth<= 21:
            zodiac_sign = ("Стрельцы")
                                                      
    print('Ваш знак зодиака: ' + (zodiac_sign))

program()


# In[17]:


program()


# ## Задание 4
# Вам нужно написать программу для подбора упаковок по размерам товара. Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):
# 
# Используйте следующие правила:
# 
# - если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран “Коробка №1”;
# - если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите “Коробка №2”;
# - если длина товара больше 2 метров, то выводите “Упаковка для лыж”;
# - во всех остальных случаях выводите “Стандартная коробка №3”.

# In[18]:


def box_size():
    """Program chooses the right size by measurments"""
    width = int(input('Введите ширину: '))
    length = int(input('Введите длину: '))
    height = int(input('Введите высоту: '))
    
    if length >= 200:
        print('Ищите упаковку для лыж')
    elif 15 < width < 50 or 15 < length < 50 or 15 < height < 50:
        print('Коробка №2')
    elif width <= 15 and length <= 15 and height <= 15:
        print('Коробка №1')
    else:
        print('Стандартная коробка №3')
        
box_size()  


# In[19]:


box_size()


# ## Задание 5
# Дана переменная, в которой хранится шестизначное число (номер проездного билета). Напишите программу, которая будет определять, является ли данный билет “счастливым”.
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.

# In[21]:


def is_winning_ticket():
    """This program defines the winning tickets by the first 3 and the last 3 digits sum identity"""
    ticket_number = [int(i) for i in input('Введите номер билета: ')]
    
    if sum(ticket_number[:3]) == sum(ticket_number[3:]):
        print('Счастливый билет ')
    else:
        print('Несчастливый билет')
        
is_winning_ticket()   


# In[22]:


is_winning_ticket()   


# ## Задание 6
# Напишите программу, которая сможет вычислять площади трех фигур (круг, треугольник и прямоугольник). Тип фигуры запрашиваем через пользовательский ввод, после чего делаем запрос характеристик фигуры:
# 
# - если пользователь выбрал круг, запрашиваем его радиус,
# - если треугольник – длины трех его сторон;
# - если прямоугольник – длины двух его сторон.

# In[29]:


# Решила поизучать, как сделать код менее объемным и получилось не совсем как в задании, 
# но работает аналогично

def area(figure, measurments):
    """This program gets the shape's name and its measurments and then prints its area """
    if figure == 'Круг':
        print(measurments[0])
        result = 3.14*(measurments[0]**2)
    if figure == 'Прямоугольник':
        a,b = measurments
        result = a*b
    if figure == 'Треугольник':
        a,b,c = measurments
        p = (a+b+c)/2
        result = (p*(p-a)*(p-b)*(p-c))**0.5
    return 'Площадь {} = {}'.format(figure, result)
    
figure = input('Выберите фигуру: ')
measurments = [ float(i) for i in input('Введите длину сторон или радиус через пробел: ').split()]
print(area(figure, measurments))


# In[36]:


def area(figure, measurments):
    """This program gets the shape's name and its measurments and then prints its area """
    if figure == 'Круг':
        print(measurments[0])
        result = 3.14*(measurments[0]**2)
    if figure == 'Прямоугольник':
        a,b = measurments
        result = a*b
    if figure == 'Треугольник':
        a,b,c = measurments
        p = (a+b+c)/2
        result = (p*(p-a)*(p-b)*(p-c))**0.5
    return 'Площадь {} = {}'.format(figure, result)
    
figure = input('Выберите фигуру: ')
measurments = [ float(i) for i in input('Введите длину сторон или радиус через пробел: ').split()]
print(area(figure, measurments))


# In[ ]:




