# Given a non-empty string of lowercase letters and a non-negative integer
# representing a key, write a function that returns a new string obtained by
# shifting every letter in the input string by k positions in the alphabet,
# where k is the key.
# Note that letters should "wrap" around the alphabet; in other words, the
# letter <span>z</span> shifted by one returns the letter <span>a</span>.
# Sample Input = "xyz"
# key = 2
# Sample Output = "zab"
# Most languages have built-in functions that give you the Unicode value of a character as well as the character corresponding to a Unicode value.
# Consider using such functions to determine which letters the input string's letters should be mapped to.
# Try creating your own mapping of letters to codes. In other words, try associating each letter in the alphabet with a specific number - its position in the alphabet,
#   for instance - and using that to determine which letters the input string's letters should be mapped to.
# How do you handle cases where a letter gets shifted to a position that requires wrapping around the alphabet? What about cases where the key is very
# large and causes multiple wrappings around the alphabet? The modulo operator should be your friend here.

def caesarCipherEncryptor(string, key):
  newLetters =  []
  newKey = key % 26
  for letter in string:
    newLetters.append(getNewLetter(letter, newKey))
  return "".join(newLetters)

def getNewLetter(letter, key):
  newLetterCode = ord(letter) + key
  return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


def caesarCipherEncryptor2(string, key):
  newLetters =  []
  newKey = key % 26
  alphabet = list('abcdefghijklmnopqrstuvwxyz')
  for letter in string:
    newLetters.append(getNewLetter2(letter, newKey, alphabet))
  return "".join(newLetters)

def getNewLetter2(letter, key, alphabet):
  newLetterCode = alphabet(letter) + key
  return alphabet[newLetterCode % 26]