"""Игра - компьютер угадывает за наименьшее количество попыток"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Угадываем число
    Args:
        number (int, optional): _Загаданное число_. Defaults to 1.
    Returns:
        int: с какой попытки угадали
    """ 
       
    predict_number = np.random.randint(1, 101) # загадываем число
    count = 0  # задаем счетчик
    min_number = 1 # делаем переменную минимума
    max_number = 100 # делаем переменную максимума

    while True:
        count += 1
        print('Число:', number, ':', 'Попытка:', count)

        if predict_number > number:
           max_number = predict_number - 1
           predict_number = (max_number + min_number) // 2
 
 
        elif predict_number < number:
           min_number = predict_number + 1
           predict_number = (max_number + min_number) // 2
        else:
            print(f'Алгоритм рассчитал число {number} за {count} попыток')
            break
    return count
random_predict()

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number)) # расширяем наш список 

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # запуск
    score_game(random_predict)