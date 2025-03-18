import pytest
from src.binary_tree_traversals import Node, traverse_in_order, traverse_pre_order, traverse_post_order

def test_empty_tree():
    """Test traversals on an empty tree (None)"""
    assert traverse_in_order(None) == []
    assert traverse_pre_order(None) == []
    assert traverse_post_order(None) == []

def test_single_node_tree():
    """Test traversals on a tree with a single node"""
    root = Node(5)
    assert traverse_in_order(root) == [5]
    assert traverse_pre_order(root) == [5]
    assert traverse_post_order(root) == [5]

def test_simple_binary_tree():
    """Test traversals on a simple binary tree"""
    #        1
    #       / \
    #      2   3
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    assert traverse_in_order(root) == [2, 1, 3]
    assert traverse_pre_order(root) == [1, 2, 3]
    assert traverse_post_order(root) == [2, 3, 1]

def test_complex_binary_tree():
    """Test traversals on a more complex binary tree"""
    #        4
    #       / \
    #      2   6
    #     / \ / \
    #    1  3 5  7
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    assert traverse_in_order(root) == [1, 2, 3, 4, 5, 6, 7]
    assert traverse_pre_order(root) == [4, 2, 1, 3, 6, 5, 7]
    assert traverse_post_order(root) == [1, 3, 2, 5, 7, 6, 4]

def test_unbalanced_tree():
    """Test traversals on an unbalanced tree"""
    #        1
    #       /
    #      2
    #     /
    #    3
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)

    assert traverse_in_order(root) == [3, 2, 1]
    assert traverse_pre_order(root) == [1, 2, 3]
    assert traverse_post_order(root) == [3, 2, 1]