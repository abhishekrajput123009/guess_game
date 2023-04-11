import random as rd


def Game():
    print('If entered number will  match then you will get a Surprise gift')
    for i in range(3):
        n = int(input('Guess any number between 1 to 6: '))
        r = rd.randint(1, 3)
        if n == r:
            print('Yeeeh ! Your Guess is matched , you won !')
            break
        else:
            print('Sorry ,your guess is not matched')
    else:
        print('Better luck next time')


Game()
