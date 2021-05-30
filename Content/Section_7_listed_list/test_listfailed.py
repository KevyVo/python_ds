class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.num_node = 0
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        #Case 1: The list is empty
        if self.head is None:
            return -1
        #Case 2: If the index does not exist then return
        elif self.num_node < index:
            return -1
        #Case 3: Get the data from index
        else:
            curr = self.head
            #Traverse the list
            for i in range(index):
                print (curr.data)
                curr = curr.nxt
            return curr.data
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        
        #Case 1: Check if list is empty
        if self.head is None:
            print("none")
            self.head = new_node
        #Case 2: prepend the node
        else:
            print("add at head")
            new_node.nxt = self.head
            self.head = new_node
        self.num_node += 1
            
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        
        #Case 1: Check if the list is empty
        if self.head is None:
            self.head = new_node
        
        #Case 2: There is only one node in the list
        elif self.head.nxt is None:
            self.head.nxt = new_node
            
        #Case 3: append the new node
        else:
            curr = self.head
            
            #Traverse the list
            while curr.nxt is not None:
                curr = curr.nxt
                
            curr.nxt = new_node
        self.num_node += 1
        return
                
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        #Case 1: If index is greater then length, no node will be inserted
        if self.num_node < index:
            pass
    
        #Case 2: If the index is equal to the length
        elif self.num_node == index:
            self.addAtTail(val)
        
        #Case 3: Add the node before the index node of the list
        else:
            new_node = Node(val)
            curr = self.head
            pev = None
            
            #Traverse the list
            for i in range(index):
                pev = curr
                curr = curr.nxt
            self.num_node += 1

            #Link the node
            pev.nxt = new_node
            new_node.nxt = curr
        return
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        #Case 1: If index is greater then length, no node will be deleted
        if self.num_node < index:
            pass
        #Case 2: If there is only one node in the list
        elif self.num_node == 1:
            del self.head
            self.num_node -= 1
        
        #Case 3: Delete the node at the index
        else:
            
            curr = self.head
            pev = None
            
            #Traverse the list
            for i in range(index):
                pev = curr
                curr = curr.nxt
                
            # Delete Node is at the end of the list
            if curr.nxt is None:
                pev = None
            # The Node is inbetween two nodes
            else:
                pev.nxt = curr.nxt
                curr.nxt = None
            
            self.num_node -= 1
            del curr
        

 #Your MyLinkedList object will be instantiated and called as such:
##obj = MyLinkedList()
##obj.addAtHead(1)
##print(obj.get(0))
##obj.addAtHead(2)
##obj.addAtTail(3)
##obj.addAtIndex(1,2)
##print(obj.get(0))
##obj.addAtHead(3)
##obj.deleteAtIndex(1)
##print(obj.get(0))

print(["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
[[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]])
