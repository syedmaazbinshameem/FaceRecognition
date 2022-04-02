from random import randrange

while True:
    print("Guess the number between 0 and 50!")
    number = randrange(50)
    #print(number)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        guess = int(input("Insert your guess: "))
        if guess == number :
            print("YOU WIN!")
            #print("The number was " + str(number))
            attempts = max_attempts
        elif guess > number:
            print("Try a smaller number")
            attempts = attempts + 1
        elif guess < number:
            print("Try a larger number")
            attempts = attempts + 1

    if attempts >= max_attempts:
        print('Game Over!')
        #print('The number was '+ str(number))
        
    print('The number was '+ str(number))
    print('Play again? Y/N: ')
    response = input()
    if response.lower() == 'y':
        continue
    else:
        break