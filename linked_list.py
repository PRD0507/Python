class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


    def print(self):
        if self.head == None:
            print("List Empty")

        itr = self.head         #iterator is of type Node i.e object of class Node
        llstr = ''
        while itr:
            llstr = llstr + str(itr.data)+'-->'
            itr = itr.next
        print(llstr)

    def insert_values(self, data_list):
        #self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count +=1
        return count

    def remove_at(self,index):
        if index<0 and index>self.get_length():
            print("Not a valid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count = count+1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 and index > self.get_length():
            print("Not a valid index")
            return

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break

            count+=1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, None)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

        if itr == None:
            print("Element not found")

    def remove_by_value(self, data):
        if self.head == None:
            print("Empty Linked List")
            return
        else:
            if self.head.data == data:
                self.head = self.head.next
                return

            itr = self.head
            while itr:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break
            itr = itr.next


if __name__ == '__main__':
    ll = Linked_List()
    ll.insert_at_beginning(10)
    ll.print()
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(20)
    ll.insert_values(['banana','apple','mango'])
    ll.print()
    ll.insert_at_beginning(89)
    print(ll.get_length())
    ll.print()
    #ll.remove_at(1)
    ll.insert_at(3,220)
    ll.print()

    ll.insert_after_value('banana', 44)
    ll.insert_after_value(2,20)
    ll.remove_by_value(89)
    ll.print()