from LinkedBinaryTree import LinkedBinaryTree
import random

def build_set_tree():
    # Define all nodes explicitly to mimic the diagram
    nodes = {}
    for i in range(7):
        for j in range(7):
            nodes[(i, j)] = LinkedBinaryTree.Node(f"{i}-{j}")

    # Add WIN and LOSE nodes
    win_node = LinkedBinaryTree.Node("WIN")
    lose_node = LinkedBinaryTree.Node("LOSE")

    # Connect nodes with weights based on the image transitions
    for i in range(6):
        for j in range(6):
            if j < 6:
                nodes[(i, j)].right = nodes[(i + 1, j)]  # p_g edge
                nodes[(i, j)].right_weight = "p_g"
            if i < 6:
                nodes[(i, j)].left = nodes[(i, j + 1)]  # q_g edge
                nodes[(i, j)].left_weight = "q_g"

    # Connect final nodes to WIN and LOSE
    nodes[(6, 5)].right = win_node  # p_t edge
    nodes[(6, 5)].right_weight = "p_t"

    nodes[(6, 5)].left = lose_node  # q_t edge
    nodes[(6, 5)].left_weight = "q_t"

    return LinkedBinaryTree(nodes[(0, 0)])

# Construct the tree
binary_tree = build_set_tree()

