#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


def game_core_v3(number):
    '''Устанавливается произвольное число в диапозоне от 1 до 100.
    Затем диапозон произвольного числа изменяется и значение перезадается в новом диапозоне в зависимости от того, больше произвольное число или меньше указанного числа.
    Функция принимает загаданное число и возвращает число попыток'''
    
    count = 0 
    first=1 # переменная начала диапозона, которая будет изменятся в цикле
    last=101 # переменная конца диапозона, которая будет изменятся в цикле
    predict = np.random.randint(1,101)
    
    while number!= predict: 
        count+=1 
        if number > predict: 
            first = predict 
        elif number < predict: 
            last = predict 
        predict = np.random.randint(first,last+1) #предполагаемое число перезадается в меньшем диапозоне, который ближе к указываемому числу number
    return(count)
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# In[ ]:


score_game(game_core_v3)


# In[ ]:




