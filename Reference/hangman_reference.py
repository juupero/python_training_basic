TRIES = 10
OFFER_NEXT_GAME = 'Would you like to have another try? (y/n)\n'
GAME_WON_PHRASE = 'Congratulations!'
GAME_LOST_PHRASE = 'GAME OVER'
LETTERS_LEFT = 'Letters left:'
INPUT_PROMPT = 'Guess a letter:\n'
INVALID_INPUT = 'Invalid input, try again'
REMAINING_TRIES = 'Tries left:'


def initialize(word_list):
    i = 0
    while i < len(word_list) and start_new_game(word_list[i], TRIES):
        i += 1


def obfuscate(word, letters_guessed):
    # obfuscated_word = ''
    # for char in word:
    #     if char in letters_guessed or not char.isalpha():
    #         obfuscated_word += char
    #     else:
    #         obfuscated_word += '_'
    # return obfuscated_word
    # A more 'pythonic' way
    #
    masked = [c if (c in letters_guessed or not c.isalpha()) else '_' for c in word]
    return ''.join(masked)


def start_new_game(word, max_tries):
    # set things up
    letters_guessed = ''
    word = word.upper()
    game_lost, game_won = False, False
    # initial print of the word obfuscated
    print(obfuscate(word, ''))
    # start the loop
    while not (game_lost or game_won):
        print(LETTERS_LEFT)
        print(''.join(
            c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if c not in letters_guessed
        ))
        print(INPUT_PROMPT)
        char = input().upper()
        if char in letters_guessed or not char.isalpha() or len(char) > 1:
            print(INVALID_INPUT)
            continue
        letters_guessed += char
        if char not in word:
            max_tries -= 1
            print(REMAINING_TRIES + str(max_tries))
            if max_tries == 0:
                game_lost = True
        print(obfuscate(word, letters_guessed))
        if obfuscate(word, letters_guessed) == word.upper():
            game_won = True
    if game_lost:
        print(GAME_LOST_PHRASE)
    if game_won:
        print(GAME_WON_PHRASE)

    print(OFFER_NEXT_GAME)
    response = input().lower()
    if response == 'n':
        return False
    if response == 'y':
        return True


initialize(['Obi-Wan Kenobi', 'Alladin'])
