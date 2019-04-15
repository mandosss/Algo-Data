"""
    Given a word w and a string s, find all indices in s which are the starting location 
    of anagrams of w. For example, given w is ab and s is abxaba, return [0,3,4].
"""

from collections import defaultdict


#The following method runs at o(string*word)
"""
def indices_location(word, s):
    result = []
    for i in range(len(s) - len(word) + 1):
        window = s[i:i + len(word)]
        if is_anagram(window, word):
            result.append(i)
    return result
"""
#This method runs in O(string)
def delete_if_zero(dictionary, character):
    if dictionary[character] == 0:
        del dictionary[character]

def indices_location_by_frequency(word, string):
    result = []
    frequency = defaultdict(int)
    
    for character in word:
        frequency[character] += 1
    
    for character in string[:len(word)]:
        frequency[character] -= 1
        delete_if_zero(frequency,character)
    
    if not frequency:
        result.append(0)
    
    for i in range(len(word), len(string)): 
        start_character, end_character = string[i-len(word)], string[i]
        frequency[start_character] += 1
        delete_if_zero(frequency, start_character)

        frequency[end_character] -= 1
        delete_if_zero(frequency,end_character)

        if not frequency: 
            beginning_index = i - len(word) + 1
            result.append(beginning_index)
    return result
    
def main():
    word = input("Enter word: ")
    string = input("Input string: ")
    print(indices_location_by_frequency(word, string))


if __name__ == '__main__':
    main()
    
