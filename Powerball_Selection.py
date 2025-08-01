import random

def powerball_selection():
    #Quickly generating a list of numbers
    number_pool = list(range(1,36))
    numbers = random.sample(number_pool, 7)
    print(f'Lottery Numbers are: {sorted(numbers)}')
    return sorted(numbers)