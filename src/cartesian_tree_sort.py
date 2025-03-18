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
    
    # Stack to keep track of nodes
    stack = []
    
    for value in arr:
        node = CartesianTreeNode(value)
        
        # While stack is not empty and top of stack is greater than current value
        while stack and stack[-1].value > value:
            # The top node becomes left child of the current node
            last_node = stack.pop()
            
            if not stack:
                node.left = last_node
            else:
                # If stack is not empty, put last_node 
                # between the current node and stack's top
                if stack[-1].value > value:
                    node.left = last_node
                else:
                    stack[-1].right = last_node
        
        # Push current node to stack
        stack.append(node)
    
    # The last node in the stack is the root
    root = stack[0]
    
    # Handle cases where right subtree is unbalanced
    while len(stack) > 1:
        last_node = stack.pop()
        stack[-1].right = last_node
    
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