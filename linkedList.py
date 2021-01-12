# creating from scratch a LL. 

# the basic node class for the linked list, its the building block for a LL
# A Constructor that takes two arguments, data(d) and next node(n)
class Node(object):
    def __init__(self, d, n =None):  # a constructor
        self.data = d
        self.next_node = n

    # now, getter and setter functions for d and n
    def get_next (self):
        return self.next_node
    def set_next (self, n):
        self.next_node = n
    def get_data (self):
        return self.data
    def set_data (self, d):
        self.data = d

# now the LL class contructor
class LinkedList(object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    def get_size (self):
        return self.size
    def add (self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True  # data now removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False   # data not found
    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

# instatiate a new list
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
#myList.remove(8)

print(myList.remove(12))
print(myList.find(5))

print(myList.get_size())


# I want to make these into lambdas as an exercise

