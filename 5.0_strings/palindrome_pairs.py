"""
    Givena list of words, find all pairs of unique indices such as the 
    concatenation of the two words is palindrome.
    For example, given the list ["code", "edoc", "da", "d"], return
    [(0,1), (1,0),(2,3)]
"""
# O(n^2) speed
def is_palindrome(concatenated_word):
    return concatenated_word == concatenated_word[::-1]

def palindromic_list(list_of_words):
    result = []
    #enumerate helps to keep track of the list with an index
    for i, word in enumerate(list_of_words):
          for j, other_word in enumerate(list_of_words):
              if i == j:
                  continue
              if is_palindrome(word + other_word):
                  result.append((i,j))
    return result

def main():
    list_of_words = input("Enter words: ").split()
    print (palindromic_list(list_of_words))

if __name__ == '__main__':
    main()
    