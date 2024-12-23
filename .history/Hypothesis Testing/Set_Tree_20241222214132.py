from LinkedBinaryTree import LinkedBinaryTree
import random
import random

class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None, left_weight=None, right_weight=None):
            self.data = data
            self.left = left
            if left is not None:
                self.left.parent = self
            self.right = right
            if right is not None:
                self.right.parent = self
            self.parent = None

            self.left_weight = left_weight
            self.right_weight = right_weight

    def __init__(self, root=None):
        self.root = root

# Build the tree structure from the provided diagram

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
                nodes[(i, j)].right_weight = 0.6  # Example weight for p_g
            if i < 6:
                nodes[(i, j)].left = nodes[(i, j + 1)]  # q_g edge
                nodes[(i, j)].left_weight = 0.4  # Example weight for q_g

    # Connect final nodes to WIN and LOSE
    nodes[(6, 5)].right = win_node  # p_t edge
    nodes[(6, 5)].right_weight = 0.7  # Example weight for p_t

    nodes[(6, 5)].left = lose_node  # q_t edge
    nodes[(6, 5)].left_weight = 0.3  # Example weight for q_t

    return LinkedBinaryTree(nodes[(0, 0)])

# Simulate the sets and display results
def simulate_sets(tree, max_steps=200):  # Increased max_steps to 200
    results = {"WIN": 0, "LOSE": 0}
    
    for _ in range(1000):  # Run 1000 simulations
        current_node = tree.root
        steps = 0

        while current_node and steps < max_steps:
            if current_node.data == "WIN":
                results["WIN"] += 1
                break
            elif current_node.data == "LOSE":
                results["LOSE"] += 1
                break

            # Randomly decide the next step based on weights
            random_value = random.random()

            if current_node.left and current_node.left_weight is not None:
                if random_value < current_node.left_weight:
                    current_node = current_node.left
                    continue

            if current_node.right and current_node.right_weight is not None:
                current_node = current_node.right

            steps += 1

    return results

# Construct the tree
binary_tree = build_set_tree()

# Run simulations and display results
results = simulate_sets(binary_tree)
print("Simulation Results:", results)
