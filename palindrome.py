print("       program checked of palindromes        ")
word =input("\nwrite one word: ")

def checkPalindrome(input):
    input = input.replace(' ', '').lower()
    if(input == input[::-1]):
      return True
    else:
      return False

def main(input):
    if(checkPalindrome(input) == True):
      print("is palindrome")
    else:
        print("not is palindrome")    


if __name__ == '__main__':
  main(word)
