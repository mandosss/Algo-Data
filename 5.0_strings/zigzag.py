"""
    Given a string and a number of lines k, print the string in zigzag form. 
    In the zigzag, character are printed out diagonally from top left to bottom right
    until reaching the kth line, then back up to top right, and so on. 
"""

def spacing(row, desc, k):
    max_spacing = (k-1) * 2 - 1
    if desc:
        spacing = max_spacing - row * 2
    else:
        spacing = max_spacing - (k - 1 - row)*2
    return spacing

def isDescending(value, k):
    return value % (2*(k-1)) < k-1

def zigzag(user_string, k):
    length = len(user_string)
    for row in range(k):
        i = row
        line = [" " for _ in range(length)]
        while i < length:
            line[i] = user_string[i]
            desc = isDescending(i,k)
            spaces = spacing(row, desc, k)
            i += spaces + 1
        print("".join(line))


def main():
    user_string = input("Enter string: ")
    number = input("Please enter the number of lines: ")
    try:
        k = int(number)
    except ValueError:
        print("it is not a number")
    zigzag(user_string, k)

if __name__ == '__main__':
    main()
    