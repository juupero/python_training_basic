import random


def generate_cipher():
    return random.sample(range(10), 4)


def get_bulls_and_cows(cipher, guess):
    assert len(cipher) == len(guess), 'the arguments must be the same length'
    bulls = 0
    cows = 0
    for i in range(len(cipher)):
        if guess[i] == cipher[i]:
            bulls += 1
        elif guess[i] in cipher:
            cows += 1
    return bulls, cows


def main_game():
    bulls = 0

    attempts = ''
    cipher = generate_cipher()
    print(cipher)
    while bulls != 4:
        guess = ''
        while len(set(guess)) != 4 or not guess.isdigit():
            print('Enter your guess without spaces: ')
            guess = input()
        bulls, cows = get_bulls_and_cows(cipher, list(map(int, list(guess))))
        attempts += '%s bulls: %d, cows: %d\n' % (guess, bulls, cows)
        print(attempts)
    print('Congrats, You win')


# def test():
#     print get_bulls_and_cows([1,2,3,4],[1,2,3,4]) == (4, 0)
#     print get_bulls_and_cows([1,2,3,4],[2,1,4,3]) == (0, 4)
#     print get_bulls_and_cows([1,2,3,4],[1,6,2,3]) == (1, 2)
#     print get_bulls_and_cows([1,2,3,4],[5,6,7,8]) == (0, 0)


main_game()
