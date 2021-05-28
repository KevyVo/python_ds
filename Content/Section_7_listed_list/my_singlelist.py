# Node class
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

# The top class
class Linkedlist:
    def __init__(self):
        #Head pointer
        self.head = None
        #Track the number of nodes in the list
        self.numNodes = 0

    # Traverse Function
    def traverse(self):
        print ("There are a total of " + str(self.numNodes) + " nodes in the list.")

        curr_node = self.head
        count = 1

        #Base case the list is empty 
        if curr_node is None:
            print ("This list is empty.")
            return

        #Now we have to the traverse the list
        while curr_node is not None:
            print("The " + str(count) + " node is " +  str(curr_node.data))
            curr_node = curr_node.next
            count += 1
        return

    # append method
    def append(self, data):

        new_node = Node(data)

        # There is no pre-existing node in the list
        if self.head is None:
            self.head = new_node
            self.numNodes += 1
            print("The first node in the list is now created.")
            return
        # This mean the list is not empty
        else:
            curr_node = self.head
            #Traverse the list to the end
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
            self.numNodes += 1
            print("The " + str(self.numNodes) + " Node is now appended.")
            return

    # Prepend Function
    def prepend(self, data):

        new_node = Node(data)

        # There is no node in the list 
        if self.head is None:
            self.head = new_node
            self.numNodes += 1
            print("The first node in the list is now created.")
            return
        else:
            # Now take the new node and append to start and switch the head pointer
            new_node.next = self.head
            self.head = new_node
            self.numNodes += 1
            print("The node " + str(self.numNodes) + " is now prepend.")
            return

    # Get number of Nodes
    def get_numnodes(self):

        return self.numNodes

    # Insert Node
    def insert(self, pev_data, data):
        
        found = False
        curr = self.head
        new_node = Node(data)

        while curr.data != pev_data and curr.next is not None:
            curr = curr.next

        if curr.next is None:
            print ("There is no node with the data: " + pev_data)
            return
        else:
            new_node.next = curr.next
            curr.next = new_node
            print("New node has been inserted.")
            self.numNodes += 1
            return

    # Middle Node
    def middle(self):
        
        #Pointers
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


    # Remove Node

    # Swap Node(does not work)
    def swap(self, val1, val2):

        #Setup pointers
        curr = self.head
        pev = curr
        v1 = None
        v2 = None
        p1 = None
        p2 = None

        #Loop through once
        while curr != None:

            if curr.data == val1:
                v1 = curr
                p1 = pev
            if curr.data == val2:
                v2 = curr
                p2 = pev
            
            pev = curr
            curr = curr.next

        #Check if v1 and v2 is in the list at all
        if v1 is None and v2 is None:
            print("Both of these values do not exist in this list.")
        #Check if v1 or v2 is in the list at all
        elif v1 is None or v2 is None:
            print("Ones of these values does not exist in the list.")
        else:
        #Swap the nodes
            p1.next = v1
            v1.next = v2.next
            v2.next = p2
            p2.next = v1
            print("The nodes have been swap")
        return


    # Reverse Node




if __name__ == "__main__":
    l1 = Linkedlist()
    l1.traverse()
    l1.append("A")
    l1.append("B")
    l1.append("C")
    l1.prepend("Z")
    l1.prepend("X")
    l1.traverse()
    l1.insert("D", "Y")
    l1.insert("B", "Y")
    l1.swap("A", "C")
    l1.traverse()
    #print("Nums: ", l1.get_numnodes())
    #print("The middle node data is ", l1.middle().data)


            
            

    