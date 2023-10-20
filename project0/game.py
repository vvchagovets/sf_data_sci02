import numpy as np

number = np.random.randint(1, 101)
count = 0


while True:
    count += 1
    predict_number = int(input("Guess a number from 1 to 100 \n"))
    
    if predict_number > number:
        print("Need less")
    elif predict_number < number:
        print("Need more")
    else:
        print(f"You guessed the number! The number is {number} in {count} tries")
        break