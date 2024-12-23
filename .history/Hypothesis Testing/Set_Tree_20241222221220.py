from LinkedBinaryTree import LinkedBinaryTree
import random
import random
# Cell 1: Import libraries and define the LinkedBinaryTree class
import random
import matplotlib.pyplot as plt

# Cell 2: Define the build_set_tree function
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
                nodes[(i, j)].right_weight = 0.7  # Example weight for p_g
            if i < 6:
                nodes[(i, j)].left = nodes[(i, j + 1)]  # q_g edge
                nodes[(i, j)].left_weight = 0.3  # Example weight for q_g

    # Connect final nodes to WIN and LOSE
    nodes[(6, 5)].right = win_node  # p_t edge
    nodes[(6, 5)].right_weight = 0.5  # Example weight for p_t

    nodes[(6, 5)].left = lose_node  # q_t edge
    nodes[(6, 5)].left_weight = 0.5  # Example weight for q_t

    return LinkedBinaryTree(nodes[(0, 0)])

# Cell 3: Define the simulate_sets function
def simulate_sets(tree, max_steps=200):  # Increased max_steps to 200
    results = {"WIN": 0, "LOSE": 0}
    points_per_step = []  # Track points scored at each step
    debug_path = []  # Track the path of the first simulation for debugging

    for sim in range(1000):  # Run 1000 simulations
        current_node = tree.root
        steps = 0
        path_points = []  # Track points per step
        path = []  # Debug path

        while current_node and steps < max_steps:
            path.append(current_node.data)

            if current_node.data == "WIN":
                results["WIN"] += 1
                points_per_step.append(path_points)
                if sim == 0:
                    debug_path = path
                break
            elif current_node.data == "LOSE":
                results["LOSE"] += 1
                points_per_step.append(path_points)
                if sim == 0:
                    debug_path = path
                break

            # Assign points based on the current edge probabilities
            if current_node.right and current_node.right_weight is not None:
                if random.random() < current_node.right_weight:
                    path_points.append(1)
                    current_node = current_node.right
                else:
                    path_points.append(0)
                    current_node = current_node.left
            elif current_node.left and current_node.left_weight is not None:
                if random.random() < current_node.left_weight:
                    path_points.append(1)
                    current_node = current_node.left
                else:
                    path_points.append(0)
                    current_node = current_node.right
            else:
                break

            steps += 1

        if not current_node:
            path.append("STALL")  # Mark as stalled if no further progress is possible

    # Handle case where no points were scored
    if not points_per_step:
        return results, [0], debug_path

    # Calculate average points scored per step
    max_steps_tracked = max(len(path) for path in points_per_step)
    avg_points_per_step = [0] * max_steps_tracked
    for step in range(max_steps_tracked):
        step_points = [path[step] for path in points_per_step if step < len(path)]
        avg_points_per_step[step] = sum(step_points) / len(step_points)

    return results, avg_points_per_step, debug_path

# Cell 4: Define the visualization functions
def visualize_avg_points(avg_points_per_step):
    plt.figure(figsize=(10, 6))
    if avg_points_per_step:
        plt.plot(range(len(avg_points_per_step)), avg_points_per_step, marker='o', linestyle='-', alpha=0.7)
        plt.title("Average Points Scored Per Step")
        plt.xlabel("Steps")
        plt.ylabel("Average Points Scored")
    else:
        plt.text(0.5, 0.5, "No data to plot", fontsize=12, ha='center')
    plt.show()

# Cell 5: Construct the tree, run simulations, and visualize results
binary_tree = build_set_tree()

results, avg_points_per_step, debug_path = simulate_sets(binary_tree)
print("Simulation Results:", results)
print("Debug Path (First Simulation):", debug_path)

visualize_avg_points(avg_points_per_step)
