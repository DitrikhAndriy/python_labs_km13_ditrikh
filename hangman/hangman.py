# Problem Set 2, hangman.py
# Name: Ditrikh Andriy
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
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  for i in secret_word:
    if i not in letters_guessed:
      return False
  return True


def get_guessed_word(secret_word, letters_guessed):
  word = []
  for i in secret_word:
    if i in letters_guessed:
      word.append(i)
    else:
      word.append("_ ")
  return "".join(word)


def get_available_letters(letters_guessed):
  alphabet = list(string.ascii_lowercase)
  for i in letters_guessed:
    if i in alphabet:
      alphabet.remove(i)
  return "".join(alphabet)
    

def hangman(secret_word):
  warnings_remaining = 3
  guesses_remaining = 6
  letters_guessed = []
  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is", len(secret_word), "letters long.")
  print("You have 3 warnings left.")
  print("-"*20)
  while 1:
    if guesses_remaining <= 0:
      print("Sorry, you ran out of guesses. The word was:", secret_word)
      break
    elif is_word_guessed(secret_word, letters_guessed):
      print("Congratulations, you won! Your total score for this game is:", len(secret_word)*guesses_remaining)
      break
    else:
      print("You have", guesses_remaining, "guesses left.")
      print("Available letters:", get_available_letters(letters_guessed))
      try:
        letter = input("Please guess a letter: ").lower()
        if len(letter) != 1:
          warnings_remaining -= 1
          if warnings_remaining < 0:
            guesses_remaining -= 1
            raise IndexError
          raise ZeroDivisionError
        elif letter in letters_guessed:
          warnings_remaining -= 1
          if warnings_remaining < 0:
            guesses_remaining -= 1
            raise IndexError
          raise TypeError
        elif letter not in string.ascii_lowercase:
          warnings_remaining -= 1
          if warnings_remaining < 0:
            guesses_remaining -= 1
            raise IndexError
          raise ValueError
        else:
          letters_guessed.append(letter)
          if letter in secret_word: 
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            print("-"*20)
            continue
          else:
            if letter in "aeiou":
              guesses_remaining -= 2
            else:
              guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            print("-"*20)
            continue
      except ZeroDivisionError:
        print("Oops! This is the wrong length. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("-"*20)
        continue
      except TypeError:
        print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("-"*20)
        continue
      except ValueError:
        print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("-"*20)
        continue
      except IndexError:
        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        print("-"*20)
        continue


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
  my_word = my_word.replace(" ", "")
  if len(my_word) != len(other_word):
    return False
  else:
    j = 0
    for i in my_word:
      if i == "_":
        j += 1
        continue
      elif my_word[j] == other_word[j]:
        j += 1
        continue
      else:
        return False
  return True


def show_possible_matches(my_word):
  '''
  my_word: string with _ characters, current guess of secret word
  returns: nothing, but should print out every word in wordlist that matches my_word
           Keep in mind that in hangman when a letter is guessed, all the positions
           at which that letter occurs in the secret word are revealed.
           Therefore, the hidden letter(_ ) cannot be one of the letters in the word
           that has already been revealed.
  '''
  matches = ""
  for i in wordlist:
    if match_with_gaps(my_word, i):
      matches = matches + i + " "
    else:
      continue
  return matches.strip()
    

def hangman_with_hints(secret_word):
  warnings_remaining = 3
  guesses_remaining = 6
  letters_guessed = []
  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is", len(secret_word), "letters long.")
  print("You have 3 warnings left.")
  print("-"*20)
  while 1:
    if guesses_remaining <= 0:
      print("Sorry, you ran out of guesses. The word was:", secret_word)
      break
    elif is_word_guessed(secret_word, letters_guessed):
      print("Congratulations, you won! Your total score for this game is:", len(secret_word)*guesses_remaining)
      break
    else:
      print("You have", guesses_remaining, "guesses left.")
      print("Available letters:", get_available_letters(letters_guessed))
      try:
        letter = input("Please guess a letter: ").lower()
        if len(letter) != 1:
          warnings_remaining -= 1
          if warnings_remaining < 0:
            guesses_remaining -= 1
            raise IndexError
          raise ZeroDivisionError
        elif letter in letters_guessed:
          warnings_remaining -= 1
          if warnings_remaining < 0:
            guesses_remaining -= 1
            raise IndexError
          raise TypeError
        elif letter == "*":
          print("Possible word matches are:", show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
          print("-"*20)
          continue
        elif letter not in string.ascii_lowercase:
          warnings_remaining -= 1
          if warnings_remaining < 0:
            guesses_remaining -= 1
            raise IndexError
          raise ValueError
        else:
          letters_guessed.append(letter)
          if letter in secret_word: 
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            print("-"*20)
            continue
          else:
            if letter in "aeiou":
              guesses_remaining -= 2
            else:
              guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            print("-"*20)
            continue
      except ZeroDivisionError:
        print("Oops! This is the wrong length. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("-"*20)
        continue
      except TypeError:
        print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("-"*20)
        continue
      except ValueError:
        print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("-"*20)
        continue
      except IndexError:
        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        print("-"*20)
        continue


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)