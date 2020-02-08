# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

#this function was already prebuilt with the hangman problem set.
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


#this function was already prebuilt with the hangman problem set
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    #return "apple"
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

#Retruns True or False based if the word was guessed
def is_word_guessed(secret_word:str, letters_guessed:list):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    #split the word into unique letters:
    secret_word_deconstructed = []
    for letter in secret_word:
      if letter not in secret_word_deconstructed:
        secret_word_deconstructed.append(letter)
      #else:
        #if you want to debug to see duplicate letters:
        #print('the following letter already exists:', letter)
    #if all the letters in the secret_word deconstructed is found, then the length will be equal
    length = 0
    for letter in secret_word_deconstructed:
      if letter in letters_guessed:
        length += 1
      else:
        length += 0
    if len(secret_word_deconstructed) == length:
      return True
    else:
      return False
    #returns True or False

#Returns the current portion of secret_word that has been guessed
def get_guessed_word(secret_word:str, letters_guessed:list):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = [] #list for guessed word
    #appending letters based on if they have been guessed or not
    for letter in secret_word:
      if letter in letters_guessed:
        guessed_word.append(letter)
      else:
        guessed_word.append('_')
      guessed_word.append(' ')
    guessed_word.pop() #remove last/extra space
    #convert list to string so it looks better
    guessed_word_string = ''
    for letter in guessed_word:
      guessed_word_string += letter
    return(guessed_word_string)

#Returns the list of letters that are available to be guessed
def get_available_letters(letters_guessed:list):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    #generate both a list of ASCII characters
    lettersNotGuessed = []
    for l in string.ascii_lowercase:
      lettersNotGuessed.append(l)
    letters_guessed.sort()
    for l in letters_guessed:
      if l in lettersNotGuessed:
        lettersNotGuessed.remove(l)
    strLettersNotGuessed = ''
    for obj in lettersNotGuessed:
      strLettersNotGuessed += obj
    return strLettersNotGuessed

#Asks for a guesssed letter, checks if it is valid, outputs a lowercase letter OR a "notaletter"
def guessALetterPrompt():
  guessedLetterInput = input("What is your letter guess: ")
  if guessedLetterInput == "*":
      return "*"
  elif guessedLetterInput in string.ascii_letters:
      guessedLetterInput = guessedLetterInput.lower()
      return guessedLetterInput
  else:
    guessedLetterInput = "notaletter"
    return guessedLetterInput

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    # At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
 
    # The user should start with 6 guesses

    # Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    # Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #fun initialization steps
    letters_guessed = []
    wordlength = len(secret_word)
    round = 1 #round counter
    guesses_remaining = 6 #guess counter
    warnings_remaining = 3 #warning counter

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is:", wordlength, "letters long.")
    print("The secret word you are guessing is:", wordlength, "characters long.")
    print("You start with 6 guesses! Every incorrect guess counts against you")
    
    while is_word_guessed(secret_word, letters_guessed) == False:
      print("------------")
      if guesses_remaining <= 0:
        break
      #print("Currently it is round #:", round)
      print("You have", guesses_remaining, "guesses left.")
      #print("You have", warnings_remaining, "warnings left.")
      print("Available letters:", get_available_letters(letters_guessed))
      guessedletter = guessALetterPrompt()
      
      #if it is not a letter input
      if guessedletter == "notaletter" or guessedletter == "*":
        warnings_remaining -= 1
        if warnings_remaining >= 0:
          print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        else:
          print("Oops! That is not a valid letter. You have no warnings left so you lose one guess", get_guessed_word(secret_word, letters_guessed))
          guesses_remaining -= 1
      
      #if it is an already guessed letter
      elif guessedletter in letters_guessed:
        warnings_remaining -= 1
        if warnings_remaining >=0:
          print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        else:
          print("Oops! You've already guessed that letter. You have no more warnings left.", get_guessed_word(secret_word, letters_guessed))
          guesses_remaining -= 1
      
      #new valid letter guessed
      else:
        letters_guessed.append(guessedletter)
        if guessedletter in secret_word:
          print("Good guess:", get_guessed_word(secret_word,letters_guessed))
        else:
          if guessedletter in "aeiou": #vowel
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word,letters_guessed))
            guesses_remaining -= 2
          else: #constant
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word,letters_guessed))
            guesses_remaining -= 1
    
    #
    uniqueletterslist = []
    for i in secret_word:
      if i not in uniqueletterslist:
        uniqueletterslist.append(i)

      
    #score calculation:
    intTotalScore = guesses_remaining*len(uniqueletterslist)
    #Concluding the game
    if is_word_guessed(secret_word, letters_guessed) == True:
      print("Congratulations, you won!")
      print("Yor total score for the game is:", intTotalScore)
    else:
      print("Sorry, you ran out of guesses. The word was", secret_word)


# testing secret word and using it to run the program
# secret_word = "apple"
# hangman(secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    charactercounter = 0

    #list of unique letters not guessed
    listofletters = string.ascii_lowercase
    my_word = my_word.replace(" ", "")
    guessedletters = set(my_word)
    guessedletters.discard('_')
    for l in guessedletters:
      listofletters = listofletters.replace(l, '')

    #checking word length
    if len(my_word) != len(other_word):
      return False
    else:
      for l in my_word:
        if l != "_": #non-blank
          if l == other_word[charactercounter]:
            charactercounter += 1
          else:
            return False
        else: #blank character
          if other_word[charactercounter] in listofletters:
            charactercounter += 1
          else:
            return False
      if len(my_word) == charactercounter:
        return True
      else: #not sure how you would get here, but I guess this is a catch all
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possibleMatchList = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            possibleMatchList.append(other_word)
    print(possibleMatchList)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    wordlength = len(secret_word)
    round = 1 #round counter
    guesses_remaining = 6 #guess counter
    warnings_remaining = 3 #warning counter
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is:", wordlength, "letters long.")
    print("The secret word you are guessing is:", wordlength, "characters long.")
    print("You start with 6 guesses! Every incorrect guess counts against you")
    print("If you ever need a hint, input '*' and it will print out some possible words that may match! Watch out for letters you have already guessed though!")
    
    while is_word_guessed(secret_word, letters_guessed) == False:
      print("------------")
      if guesses_remaining <= 0:
        break
      #print("Currently it is round #:", round)
      print("You have", guesses_remaining, "guesses left.")
      #print("You have", warnings_remaining, "warnings left.")
      print("Available letters:", get_available_letters(letters_guessed))
      guessedletter = guessALetterPrompt()
      
      #if it is not a letter input
      
      #if it is either * or "not a letter"
      if guessedletter == "*":
          my_word = get_guessed_word(secret_word, letters_guessed)
          show_possible_matches(my_word)
      elif guessedletter == "notaletter":
          warnings_remaining -= 1
          if warnings_remaining >= 0:
            print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
          else:
            print("Oops! That is not a valid letter. You have no warnings left so you lose one guess", get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1
    
      #if it is an already guessed letter
      elif guessedletter in letters_guessed:
        warnings_remaining -= 1
        if warnings_remaining >=0:
          print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        else:
          print("Oops! You've already guessed that letter. You have no more warnings left.", get_guessed_word(secret_word, letters_guessed))
          guesses_remaining -= 1
      
      #new valid letter is guessed
      else:
        letters_guessed.append(guessedletter)
        if guessedletter in secret_word:
          print("Good guess:", get_guessed_word(secret_word,letters_guessed))
        else:
          if guessedletter in "aeiou": #vowel
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word,letters_guessed))
            guesses_remaining -= 2
          else: #constant
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word,letters_guessed))
            guesses_remaining -= 1
    
    #
    uniqueletterslist = []
    for i in secret_word:
      if i not in uniqueletterslist:
        uniqueletterslist.append(i)

      
    #score calculation:
    intTotalScore = guesses_remaining*len(uniqueletterslist)
    #Concluding the game
    if is_word_guessed(secret_word, letters_guessed) == True:
      print("Congratulations, you won!")
      print("Yor total score for the game is:", intTotalScore)
    else:
      print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)