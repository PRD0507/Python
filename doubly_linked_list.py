class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        if self.head == None :
            self.head = Node(data, self.head, self.head)
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data, self.head, self.head)
        else:
            itr = self.head

            while itr:
                if itr.next == None:
                    itr.next = Node(data, None, itr)
                itr = itr.next

    def print(self):
        if self.head == None:
            print("List Empty")

        itr = self.head  # iterator is of type Node i.e object of class Node
        dllstr = ''
        while itr:
            dllstr = dllstr + str(itr.data) + '-->'
            itr = itr.next
        print(dllstr)

    def print_forward(self):
        if self.head == None:
            print("List Empty")

        itr = self.head  # iterator is of type Node i.e object of class Node
        dllstr = ''
        while itr:
            dllstr = dllstr + str(itr.data) + '-->'
            itr = itr.next
        print(dllstr)

    def print_backward(self):
        itr = self.head

        while itr:
            if itr.next == None:
                break
            itr = itr.next

        dllstr = ''
        while itr:
            dllstr = dllstr + str(itr.data) + '-->'
            itr = itr.prev
        print(dllstr)

    def insert_at(self,index,data):
        if index < 0 and index > self.get_length():
            print("Not a valid index")
            return

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next,itr)
                if node.next:
                    itr.next.prev = node
                itr.next = node
                break

            count += 1
            itr = itr.next


if __name__ == '__main__':
    dll = Doubly_linked_list()
    dll.insert_at_beginning(10)
    dll.print()
    dll.insert_at_beginning(20)
    dll.print()
    dll.insert_at_beginning(30)
    dll.print()
    dll.insert_at_beginning(40)
    dll.print()

    dll.print_forward()
    dll.print_backward()

    dll.insert_at(0,200)
    dll.print()