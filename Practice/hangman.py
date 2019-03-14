TRIES = 10
OFFER_NEXT_GAME = 'Would you like to have another try? (y/n)\n'
GAME_WON_PHRASE = 'Congratulations!'
GAME_LOST_PHRASE = 'GAME OVER'
LETTERS_LEFT = 'Letters left:'
INPUT_PROMPT = 'Guess a letter:\n'
INVALID_INPUT = 'Invalid input, try again'
REMAINING_TRIES = 'Tries left:'



# DO NOT MODIFY THE initialize function
def initialize(word_list):
    """
    Takes a list of words as a parameter.
    Starting with the word in the word_list,
    starts a new game using the word.
    If the user wants to play again, starts the next
    game with the next word.
    Runs until user doesn't want to play or
    until it runs out of new words.
    """
    i = 0
    while i < len(word_list):
        start_new_game(word_list[i], TRIES)
        i += 1

def obfuscate(word, letters_guessed):
    """
    Takes the current word being guessed and
    a string containing letters that user has
    tried to guess during current playthrough.

    Returns a string, that only shows letters
    that the user has guessed correctly. Return
    the guessed letter in uppercase. The letters,
    that user still has to guess are replaced with
    underscores.


    Example:
        input: 'claire','abcd'
        ouput: 'C_A___'
    Example:
        input: 'Amanda','etai'
        output: 'A_A__A'
    Example:
        input: 'Obi-Wan KENOBI','oteai'
        output: 'O_I-_A_ _E_O_I'
    """
    available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    obfuscated_word = word.upper()
    for char in obfuscated_word:
        if char in available_letters:
            if char not in letters_guessed.upper():
                obfuscated_word = obfuscated_word.replace(char, "_")
    for char in available_letters:
        if char in obfuscated_word:
            available_letters = available_letters.replace(char, "")
    if "_" not in obfuscated_word:
        print(GAME_WON_PHRASE)
        print(OFFER_NEXT_GAME)
        user_decision = input()
        if user_decision is "y":
            start_new_game('Alladin', TRIES)
    if REMAINING_TRIES == 0:
        print(GAME_LOST_PHRASE)
        print(OFFER_NEXT_GAME)
        user_decision = input()
        if user_decision is "y":
            start_new_game('Alladin', TRIES)
    print(obfuscated_word)
    print(available_letters)


def start_new_game(word, max_tries):
    """
    # Arguments
    Takes a word (string) that the user has to guess,
    and max_tries (int) - the number of tries user has
    before he loses the game.


    # Description
    Before prompting the user always show the letters he still hasn't tried to guess.
    This function should prompt user for a letter, and
    check, whether the letter guessed is in the word.
    If user guessed correctly, reveal the letter to him.
    If user guessed wrong, decrease the number of tries and show the amount of tries remaining.

    Keep asking user for more letters, until he wins or loses.
    When the game ends, ask user to choose, whether they want
    to play the game again.
    If the user types 'n', return False.
    If the user types 'y', return True.
    User will only input 'n','N','y' or 'Y', so no need to handle other cases

    # Return
    Returns a boolean, stating whether user
    wants to have another game.

    Example:
        input: 'Obi-Wan Kenobi',
        execution: user wins, wants to play again,
                    types 'y' when prompted
        output: True
    Example:
        input: 'GANDALF',
        execution: user wins, doesn't want to play again,
                    types 'n' when prompted
        output: False

    """
    try_number = 0
    letters_guessed = ""
    available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while try_number < max_tries:
        obfuscate(word, letters_guessed)
        print(INPUT_PROMPT)
        letter_given = input()
        if letter_given.upper() not in available_letters:
            print(INVALID_INPUT)
            continue
        else:
            available_letters = available_letters.replace(letter_given, "")
        max_tries -= 1
        print(f"Tries left {max_tries}")
    print(GAME_LOST_PHRASE)


initialize(['Obi-Wan Kenobi', 'Alladin'])
