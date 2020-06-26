"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)    
        # compare to the new value we want to insert

        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            elif self.left is None:
                self.left = BSTNode(value)

        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            elif self.right is None:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
            if self.value == target:
                return True
            if self.value > target:
                if self.left is None:
                    return False
                found = self.left.contains(target)
            else:
                if self.right is None:
                    return False
                found = self.right.contains(target)
            return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        # if we cannot go right, return the current value
        if self.right == None:
            return self.value
        if self.right is not None:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value fn(self.value)
        # if you can go left, call for_each on the left tree
        # if you can go right, call for_each on the right tree
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    #def in_order_print(self, node):
    #    if node is None:
    #        return
    #    self.in_order_print(node.left)
    #    print(node.value)
    #    self.in_order_print(node.right)

    #def in_order_print(self, node):
    #    if node.left:
    #        node.in_order_print(node.left)
    #    print(int(node.value))
    #    if node.right:
    #        node.in_order_print(node.right)

    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # Print top layer, then one layer lower, then one layer lower, etc.
    # Use a QUEUE data structure
    def bft_print(self, node):
        queue = []
        queue.append(node)
        while len(queue) != 0:
            removed_node = queue.pop(0)
            print(removed_node.value)
            if removed_node.left is not None:
                queue.append(removed_node.left)
            if removed_node.right is not None:
                queue.append(removed_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Use a STACK data structure
    def dft_print(self, node):
        stack = []
        stack.append(node)
        while len(stack) != 0:
            removed_node = stack.pop(-1)
            print(removed_node.value)
            if removed_node.left is not None:
                stack.append(removed_node.left)
            if removed_node.right is not None:
                stack.append(removed_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)

# ORDER OF NODE INSERTS FROM TEST FILE
#test = BSTNode(1)
#test.insert(8)
#test.insert(5)
#test.insert(7)
#test.insert(6)
#test.insert(3)
#test.insert(4)
#test.insert(2)
#test.bft_print(test)