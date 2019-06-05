# Add two linked lists and return the result in reverse
#   1 -> 2  
#   3 -> 9
#   114(21+93)
#   4 -> 1 -> 1 
#TODO: finish thi problem

from single_linked_list import LinkedList
from single_linked_list import Node
    
def add_linked_list(first_list, second_list, leftover=0):
    if not first_list and not second_list and not leftover:
        return None
    


def main():
    first_list = LinkedList()
    second_list = LinkedList()
    for i in range(3):
        first_list.insert(i)
    for i in range(3):
        second_list.insert(i)
    

if __name__ == '__main__':
    main()
