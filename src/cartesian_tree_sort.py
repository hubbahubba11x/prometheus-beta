from typing import List, TypeVar, Optional

T = TypeVar('T')

class CartesianTreeNode:
    """
    Node class for Cartesian Tree representation.
    
    Attributes:
        value: The value stored in the node
        index: Original index of the value
        left: Left child node
        right: Right child node
    """
    def __init__(self, value, index):
        """
        Initialize a Cartesian Tree Node.
        
        Args:
            value: The value to be stored in the node
            index: Original index of the value
        """
        self.value = value
        self.index = index
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
    
    # Nodes for each element with their original indices
    nodes = [CartesianTreeNode(val, i) for i, val in enumerate(arr)]
    
    # Track the root node
    root = nodes[0]
    
    # Track the stack of nodes to build the tree
    stack = [root]
    
    # Iterate through the rest of the nodes
    for node in nodes[1:]:
        # Find the appropriate parent for the current node
        while stack and (stack[-1].value > node.value or 
                         (stack[-1].value == node.value and stack[-1].index > node.index)):
            last_node = stack.pop()
            
            # If stack becomes empty, the last node becomes the left child
            if not stack:
                node.left = last_node
            else:
                # If the stack's top is still larger, set last_node as left child
                if stack[-1].value > node.value or \
                   (stack[-1].value == node.value and stack[-1].index > node.index):
                    node.left = last_node
                else:
                    # Otherwise, attach last_node as right child
                    stack[-1].right = last_node
        
        # Push current node to stack
        stack.append(node)
    
    # Handle any remaining nodes in the stack
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