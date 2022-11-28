import numpy as np

def random_predict(number:int=10) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
   
    count = 0
    
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            for num in range(6,1,-1):
                predict +=num 
        elif number < predict:
            for nam in range(1,6,1):
                predict -=nam 
        elif number == predict:
            break #выход из цикла, если угадали

    return count

print(f'Количество попыток: {random_predict()}')