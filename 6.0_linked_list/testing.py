from single_linked_list import LinkedList
from single_linked_list import Node
    
def main():
    linked_list = LinkedList(0)
    for i in range(10):
        linked_list.insert(i+1)
    linked_list.print_linked_list()
    linked_list.delete(3)
    linked_list.print_linked_list()

if __name__ == '__main__':
    main()
