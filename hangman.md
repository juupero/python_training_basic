
# Hangman assignment

Make a hangman game. If you want to know what the game looks like, head over to hangman.no and play for a bit

# Story

User starts the game with a list of words.  
The first word is printed obfuscated (see template).  
  
User tries to guess it by inputting a character.
If user was correct, reveal all of these letters.
If user was wrong, deduct one try.  
  
If try count reached zero before user guessed the word, the game is over.  
Otherwise, the user is presented with a choice: continue with the next word or not (tries are reset for every word).  
  
If user inputs `y`(or `Y`), game starts with the next word.
If user inputs `n`(or `N`), game stops.
If user inputs `y`(or `Y`), but there are no words left, the game stops.
If user inputs neither of `n`,`y`,`Y`,`N`, the user is a bad person. Don't handle this case.

# Technical details

See the template for some predefined strings and function to fill in.  
Some notes concerning input:

  + Valid input:
    + Single letter character
  + If invalid:
    + Do not decrease TRIES_LEFT
    + Notify user

# Tips

## Input(text) vs Print(text)

Instead of passing an argument to `input`, `print` first, and then do `input()`.  
E.g.: instead of  

        something = input('Please punch some keys')

please do

        print('Please punch some keys')
        something = input()

## File name

Don't forget to rename your `hangman_template.py` to `hangman.py` 

## Testing

Comment out the `initialize` line at the end of the template, and uncomment the `import` line. Note that `hangman_test.pyc` file must be in the same folder as your `hangman.py` file.

Your tests will fail if your prints are different from suggested. Make sure you use the supplied strings and DO NOT use any extra newlines nor spaces. Input examples (at the end of this PDF) will guide you.

## Imports

You shouldn't need to import any modules. However, if you are trying to import the `hangman_test` module, you might get an error, saying:

        ModuleNotFoundError: No module named 'mock'

A simple solution is to open the command line and type `pip install mock`.

# Input exampes

## Making some mistakes

>py -3 hangman.py

    ______
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

    j
    Tries left:9
    ______
    Letters left:
    ABCDEFGHIKLMNOPQRSTUVWXYZ
    Guess a letter:

    y
    Tries left:8
    ______
    Letters left:
    ABCDEFGHIKLMNOPQRSTUVWXZ
    Guess a letter:

    u
    Tries left:7
    ______
    Letters left:
    ABCDEFGHIKLMNOPQRSTVWXZ
    Guess a letter:


## Guessing a word

>py -3 hangman.py

    ______
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

    m
    M_____
    Letters left:
    ABCDEFGHIJKLNOPQRSTUVWXYZ
    Guess a letter:

    E
    ME____
    Letters left:
    ABCDFGHIJKLNOPQRSTUVWXYZ
    Guess a letter:

    l
    MEL___
    Letters left:
    ABCDFGHIJKNOPQRSTUVWXYZ
    Guess a letter:

    K
    MELK__
    Letters left:
    ABCDFGHIJNOPQRSTUVWXYZ
    Guess a letter:

    o
    MELKO_
    Letters left:
    ABCDFGHIJNPQRSTUVWXYZ
    Guess a letter:

    R
    MELKOR
    Congratulations!
    Would you like to have another try? (y/n)
    
    n

## Invalid input (multiple characters, or non-alpha characters)

>py -3 hangman_reference.py

    ______
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

    qwerty
    Invalid input, try again
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

    .
    Invalid input, try again
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

    3
    Invalid input, try again
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

        <-- this is a space
    Invalid input, try again
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

        <-- this is a newline
    Invalid input, try again
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

## Guessing two words (the first one is a bit of a tough case (Obi-Wan Kenobi))

>py -3 hangman_reference.py

    ___-___ ______
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

    o
    O__-___ ___O__
    Letters left:
    ABCDEFGHIJKLMNPQRSTUVWXYZ
    Guess a letter:

    b
    OB_-___ ___OB_
    Letters left:
    ACDEFGHIJKLMNPQRSTUVWXYZ
    Guess a letter:

    i
    OBI-___ ___OBI
    Letters left:
    ACDEFGHJKLMNPQRSTUVWXYZ
    Guess a letter:

    w
    OBI-W__ ___OBI
    Letters left:
    ACDEFGHJKLMNPQRSTUVXYZ
    Guess a letter:

    a
    OBI-WA_ ___OBI
    Letters left:
    CDEFGHJKLMNPQRSTUVXYZ
    Guess a letter:

    n
    OBI-WAN __NOBI
    Letters left:
    CDEFGHJKLMPQRSTUVXYZ
    Guess a letter:

    k
    OBI-WAN K_NOBI
    Letters left:
    CDEFGHJLMPQRSTUVXYZ
    Guess a letter:

    e
    OBI-WAN KENOBI
    Congratulations!
    Would you like to have another try? (y/n)

    y
    _______
    Letters left:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

    a
    A__A___
    Letters left:
    BCDEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

    d
    A__AD__
    Letters left:
    BCEFGHIJKLMNOPQRSTUVWXYZ
    Guess a letter:

    L
    ALLAD__
    Letters left:
    BCEFGHIJKMNOPQRSTUVWXYZ
    Guess a letter:

    n
    ALLAD_N
    Letters left:
    BCEFGHIJKMOPQRSTUVWXYZ
    Guess a letter:

    i
    ALLADIN
    Congratulations!
    Would you like to have another try? (y/n)

    y