import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing a number
    Args:
        number (int, optional): Guessed number. Defaults to 1.
        
    Returns:
        int: number of tries
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
    
        if predict_number == number:
            break
    return count


number = np.random.randint(1, 101)

print(f'Количество попыток: {random_predict(number)}')
