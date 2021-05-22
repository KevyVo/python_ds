class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # this operation inserts items at the end of the linked list
    # so we have to manipulate the tail node in O(1) running time
    def insert(self, data):

        new_node = Node(data)

        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # there is at least 1 item in the data structure
        # we keep inserting items at the end of the linked list
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, data):

        #Case 1: list is empty
        if self.head == None and self.tail == None:
            print("The Doubly linked-list is empty, no removal")
            return

        #Case 2: data does not exist
        curr_node = self.head

        while curr_node.data != data:
            if curr_node.next is None:
                print ("This data does not exist.")
                return
            curr_node = curr_node.next

        #Case 3: Data has been found, not have to deal with 3 case of removal

        #1: Data is found at the head node
            #Check if it is the head node
        if curr_node.previous is None:
            self.head = curr_node.next
            self.head.previous = None
            curr_node.next = None
        
        #2: Data is found at the end node
        elif curr_node.next is None:
            self.tail = curr_node.previous
            self.tail.next = None
            curr_node.previous = None

        #3: Data is found between two nodes
        else:
            curr_node.previous.next = curr_node.next
            curr_node.next.previous = curr_node.previous
            curr_node.next = None
            curr_node.previous = None
        
        #Delete the Node
        del curr_node


    # we can traverse a doubly linked list in both directions
    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous


if __name__ == '__main__':

    linked_list = DoublyLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    # 1 2 3
    linked_list.traverse_forward()

    print("---")

    linked_list.remove(2)

    # 3 2 1
    linked_list.traverse_backward()