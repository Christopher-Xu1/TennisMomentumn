from LinkedBinaryTree import LinkedBinaryTree
import random
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

# Cell 3: Define the simulate_sets function
def simulate_sets(tree, max_steps=200):  # Increased max_steps to 200
    results = {"WIN": 0, "LOSE": 0}
    points_over_time = []  # Track points scored during each set

    for _ in range(1000):  # Run 1000 simulations
        current_node = tree.root
        steps = 0
        points = 0  # Points scored in the current set

        while current_node and steps < max_steps:
            if current_node.data == "WIN":
                results["WIN"] += 1
                points_over_time.append(points)
                break
            elif current_node.data == "LOSE":
                results["LOSE"] += 1
                points_over_time.append(points)
                break

            # Randomly decide the next step based on weights
            random_value = random.random()

            if current_node.left and current_node.left_weight is not None:
                if random_value < current_node.left_weight:
                    current_node = current_node.left
                    points += 1  # Increment points for moving left
                    continue

            if current_node.right and current_node.right_weight is not None:
                current_node = current_node.right
                points += 1  # Increment points for moving right
            else:
                # Fallback: If stuck, force a move
                if current_node.left:
                    current_node = current_node.left
                    points += 1
                elif current_node.right:
                    current_node = current_node.right
                    points += 1

            steps += 1

    return results, points_over_time

# Cell 4: Define the visualize_points function
def visualize_points(points_over_time):
    plt.figure(figsize=(10, 6))
    plt.hist(points_over_time, bins=20, edgecolor="black", alpha=0.7)
    plt.title("Distribution of Points Scored Per Set")
    plt.xlabel("Points Scored")
    plt.ylabel("Frequency")
    plt.show()

# Cell 5: Construct the tree, run simulations, and visualize results
binary_tree = build_set_tree()

results, points_over_time = simulate_sets(binary_tree)
print("Simulation Results:", results)

visualize_points(points_over_time)
