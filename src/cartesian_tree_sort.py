from typing import List, TypeVar, Optional

T = TypeVar('T')

class CartesianTreeNode:
    """
    Node class for Cartesian Tree representation.
    
    Attributes:
        value: The value stored in the node
        left: Left child node
        right: Right child node
    """
    def __init__(self, value):
        """
        Initialize a Cartesian Tree Node.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr: List[T]) -> Optional[CartesianTreeNode]:
    """
    Build a Cartesian Tree from the given array.
    
    A Cartesian Tree is a binary tree derived from an array such that:
    1. It is a min-heap based on the value 
    2. In-order traversal gives the original array
    
    Args:
        arr: Input list to build the Cartesian Tree from
    
    Returns:
        Root of the Cartesian Tree, or None if input is empty
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return None
    
    # Create a single-linked list to track elements
    class LinkedNode:
        def __init__(self, value, index):
            self.value = value
            self.index = index
            self.next = None
    
    # Create linked list to preserve original indices
    head = curr = LinkedNode(arr[0], 0)
    for i in range(1, len(arr)):
        curr.next = LinkedNode(arr[i], i)
        curr = curr.next
    
    # Sort the linked list
    def merge_sort(head):
        # Base cases
        if not head or not head.next:
            return head
        
        # Split the list
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Detach the two halves
        if prev:
            prev.next = None
        
        # Recursively sort both halves
        left = merge_sort(head)
        right = merge_sort(slow)
        
        # Merge sorted halves
        dummy = curr = LinkedNode(0, -1)
        while left and right:
            if left.value <= right.value:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        # Attach remaining nodes
        curr.next = left if left else right
        
        return dummy.next
    
    # Sort the linked list while preserving original indices
    sorted_list = merge_sort(head)
    
    # Rebuild array from sorted linked list
    sorted_arr = []
    indices = []
    curr = sorted_list
    while curr:
        sorted_arr.append(curr.value)
        indices.append(curr.index)
        curr = curr.next
    
    # Rebuild Cartesian Tree from sorted array
    # Use array indices to match original positions
    stack = []
    for i, value in enumerate(sorted_arr):
        # Create the new node
        node = CartesianTreeNode(value)
        
        # Find the last node that is smaller than the current node
        while stack and sorted_arr[stack[-1].index] > value:
            stack.pop()
        
        # If stack is empty, current node becomes the root
        if not stack:
            node.left = None
        else:
            # Current node becomes right child of the last smaller node
            node.left = stack[-1].right
            stack[-1].right = node
        
        # Add current node to stack
        stack.append(node)
    
    # The last node in stack is the root
    root = stack[0]
    
    return root

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Perform Cartesian Tree Sort on the input list.
    
    Args:
        arr: Input list to be sorted
    
    Returns:
        Sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, return as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Build Cartesian Tree
    root = build_cartesian_tree(arr)
    
    # Result list to store sorted elements
    result = []
    
    def in_order_traversal(node):
        """
        Perform in-order traversal to get sorted elements.
        
        Args:
            node: Current node in the Cartesian Tree
        """
        if not node:
            return
        
        # Traverse left subtree
        in_order_traversal(node.left)
        
        # Add current node's value to result
        result.append(node.value)
        
        # Traverse right subtree
        in_order_traversal(node.right)
    
    # Perform in-order traversal to get sorted list
    in_order_traversal(root)
    
    return result