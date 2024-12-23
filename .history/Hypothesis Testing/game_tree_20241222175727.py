from LinkedBinaryTree import * 

def construct_tree(tree):
    tree.root = LinkedBinaryTree.Node("0-0")  # Start at 0-0

    n0_0 = tree.root
    n0_0.right = LinkedBinaryTree.Node("15-0")
    n0_0.left = LinkedBinaryTree.Node("0-15")

    # Player 1 scoring
    n15_0 = n0_0.right
    n15_0.right = LinkedBinaryTree.Node("30-0")
    n15_0.left = LinkedBinaryTree.Node("15-15")

    n30_0 = n15_0.right
    n30_0.right = LinkedBinaryTree.Node("40-0")
    n30_0.left = LinkedBinaryTree.Node("30-15")

    n40_0 = n30_0.right
    n40_0.right = LinkedBinaryTree.Node("WIN")
    n40_0.left = LinkedBinaryTree.Node("40-15")

    # Opponent scoring
    n0_15 = n0_0.left
    n0_15.right = LinkedBinaryTree.Node("15-15")
    n0_15.left = LinkedBinaryTree.Node("0-30")

    n0_30 = n0_15.left
    n0_30.right = LinkedBinaryTree.Node("15-30")
    n0_30.left = LinkedBinaryTree.Node("0-40")

    n0_40 = n0_30.left
    n0_40.right = LinkedBinaryTree.Node("15-40")
    n0_40.left = LinkedBinaryTree.Node("LOSE")

    # Handle DEUCE and ADV states
    n30_15 = n30_0.left
    n30_15.right = LinkedBinaryTree.Node("40-15")
    n30_15.left = LinkedBinaryTree.Node("DEUCE")

    n15_40 = n0_40.right
    n15_40.right = LinkedBinaryTree.Node("30-40, A2")
    n15_40.left = LinkedBinaryTree.Node("LOSE")

    nDeuce = n30_15.left
    nDeuce.right = LinkedBinaryTree.Node("40-30, A1")
    nDeuce.left = LinkedBinaryTree.Node("30-40, A2")

    # Advantage states
    nA_1 = nDeuce.right
    nA_1.right = LinkedBinaryTree.Node("WIN")  # Player 1 wins from advantage
    nA_1.left = nDeuce  # Returns to DEUCE if opponent wins next point

    nA_2 = nDeuce.left
    nA_2.right = nDeuce  # Returns to DEUCE if Player 1 wins next point
    nA_2.left = LinkedBinaryTree.Node("LOSE")  # Player 2 wins from advantage
