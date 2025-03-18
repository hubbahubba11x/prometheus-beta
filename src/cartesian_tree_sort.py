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
    
    # Use a stack to build the Cartesian Tree
    stack = []
    
    for value in arr:
        # Create the new node
        node = CartesianTreeNode(value)
        
        # Find the last node that is smaller than the current node
        while stack and stack[-1].value > value:
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
    return stack[0]

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