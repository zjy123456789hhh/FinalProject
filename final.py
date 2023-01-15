#1
class ListNode:
        # Constructor to create a new node
        def __init__(self, data):
            self.data = data
            self.next = None
       
# Binary Tree Node structure
class BinaryTreeNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Class to convert the linked list to Binary Tree
class Conversion:
    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self, data = None):
        self.head = None
        self.root = None
       


         #def push(self, new_data):
        # Creating a new linked list node and storing data
        #new_node = ListNode(new_data)
        # Make next of new node as head
        #new_node.next = self.head
        # Move the head to point to new node
        #self.head = new_node(头插法结果颠倒)

    def push(self, new_data):#(尾插法)
       
        new_node = ListNode(new_data)
        if self.head==None:
          self.head = new_node
        else:
          p = self.head
          while p.next!=None:
            p = p.next
          p.next = new_node
#Because for a complete binary tree, if the subscript of a node in the list is p, 
#then the subscript of its left child node is 2p and the right node is 2p+1.
# When we want to find the parent of any node, we can directly use python's divisible method.
# If the node is subscript n in the list, then the parent node is subscript n//2.

# Function to return the index of the
# parent node of a given node
    def parent(self,i) :
     return (i // 2)
# Function to return the index of the
# left child of the given node
    def leftChild(self,i) :
     return (2 * i)
# Function to return the index of the
# right child of the given node
    def rightChild(self,i) :
     return ((2 * i) + 1)


    def length(self):
        c= self.head
        count = 0
        while c is not None:
            count += 1
            c = c.next
        return count

    def get_l(self,i):
        if i<0 or i>=self.length():
            return None
        c_node=self.head
        index=0
        if c_node and index!=i:
            for index in range(i):
                c_node=c_node.next
                index+=1
            return c_node
            
#2
class BH:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0 
# Function to shift up the 
# node in order to maintain 
# the heap property
    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
# Function to insert a 
# new element in 
# the Binary Heap
    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

# Function to shift down the node in
# order to maintain the heap property
    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc
#Function to find the minchild by comparing the left and right subtrees
    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1
#Function to returns the smallest item in the heap and removes it from the heap
    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval
#Function to creates a new heap from a list of nodes
    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1






#3 By using heap datastructure to implement Priority Queues, Time complexity:
#insert Operation: O(log(n))
#delMin Operation: O(log(n))






#4
if __name__ == "__main__":

    ll = Conversion()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    p=ll.parent(4)
    print(ll.get_l(p).data)
    
    

bh=BH()
bh.buildHeap([9,6,5,8,3])
bh.insert(55)
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())