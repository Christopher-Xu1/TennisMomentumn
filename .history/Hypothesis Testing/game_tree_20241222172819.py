from LinkedBinaryTree import LinkedBinaryTree  # Assuming LinkedBinaryTree is defined elsewhere

def construct_tree(tree):
    tree.root = LinkedBinaryTree.Node("0-0")  # Start at 0-0

    # Root node
    n0_0 = tree.root
    n0_0.right = LinkedBinaryTree.Node("15-0")  # Player wins first point
    n0_0.left = LinkedBinaryTree.Node("0-15")  # Opponent wins first point

    # Build the tree following tennis scoring rules
    n15_0 = n0_0.right
    n0_15 = n0_0.left

    # From 15-0
    n15_0.right = LinkedBinaryTree.Node("30-0")  # Player wins again
    n15_0.left = LinkedBinaryTree.Node("15-15")  # Opponent wins next point

    # From 0-15
    n0_15.right = n15_0.left  # Back to 15-15 if player wins
    n0_15.left = LinkedBinaryTree.Node("0-30")  # Opponent wins again

    # Add the next levels
    n30_0 = n15_0.right
    n15_15 = n15_0.left
    n0_30 = n0_15.left

    # From 30-0
    n30_0.right = LinkedBinaryTree.Node("40-0")  # Player wins next point
    n30_0.left = LinkedBinaryTree.Node("30-15")  # Opponent wins next point

    # From 15-15
    n15_15.right = n30_0.left  # Goes to 30-15 if player wins
    n15_15.left = LinkedBinaryTree.Node("15-30")  # Opponent wins next point

    # Continue building the tree
    n0_30.right = n15_15.left  # Back to 15-30
    n0_30.left = LinkedBinaryTree.Node("0-40")  # Opponent wins next point

    # Terminal states
    n40_0 = n30_0.right
    n40_0.right = LinkedBinaryTree.Node("WIN")  # Player wins game
    n40_0.left = LinkedBinaryTree.Node("40-15")  # Opponent wins next point

    n0_40 = n0_30.left
    n0_40.right = LinkedBinaryTree.Node("15-40")  # Player wins next point
    n0_40.left = LinkedBinaryTree.Node("LOSE")  # Opponent wins game

    # Handle deuce and advantage states
    n40_15 = n40_0.left
    n30_15 = n15_15.right
    n30_15.right = n40_15  # Goes to 40-15
    n30_15.left = LinkedBinaryTree.Node("DEUCE")  # Back to deuce

    n40_15.left = n40_0.right  # Back to WIN
    n40_15.right = LinkedBinaryTree.Node("40-30")  # Advantage player

    # From DEUCE
    nDeuce = n30_15.left
    nDeuce.right = n40_15.right  # Advantage player
    nDeuce.left = LinkedBinaryTree.Node("30-40")  # Advantage opponent

    # Advantage nodes
    nA_1 = n40_15.right
    nA_2 = nDeuce.left
    nA_1.right = LinkedBinaryTree.Node("WIN")  # Player wins from advantage
    nA_1.left = nDeuce  # Back to deuce
    nA_2.right = nDeuce  # Back to deuce
    nA_2.left = LinkedBinaryTree.Node("LOSE")  # Opponent wins from advantage

    return
