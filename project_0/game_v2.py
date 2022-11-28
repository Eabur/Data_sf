"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np
def random_predict(number:int = np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. По умолчанию
        рандомно загадывается компьютером в диапазоне 1-100.
    Returns:
        int: Количество попыток
    """
    count = 0
    lst_num = list(range(1, 101))
    while True:
        count += 1
        predict_number = int(np.mean(lst_num))
        if number == predict_number:
            break
        elif predict_number > number:
            lst_num = list (range (lst_num [0], predict_number+2))
        else:
            lst_num = list (range (predict_number, lst_num [-1]+2))
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее начение количества попыток
    """
    count_ls = [] # список для сохранения количества попыток
    #np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)