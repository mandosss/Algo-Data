
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_value):
        self.next = new_value

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()   
        return current
    
    def search(self, value):
        is_found = False
        current = self.head
        while not is_found and current:
            if current.get_data() == value:
                is_found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Value not in list")
        return current

    def delete(self, value):
        current = self.head
        previous = None
        is_found = False
        while not is_found and current:
            if current.get_data() == value:
                is_found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Value not in list")
        elif previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
    def print_linked_list(self):
        current = self.head
        result = []
        position = 0
        while current:
            result.append(current.get_data())
            current = current.get_next()
            position += 1
        print(result, end="\n")
