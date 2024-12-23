from LinkedBinaryTree import * 

def construct_tree(tree):
    win= LinkedBinaryTree.Node("WIN")
    lose= LinkedBinaryTree().Node("LOSE")
    
    tree.root = LinkedBinaryTree.Node("0-0")

    n0_0 = tree.root
    n0_0.right = LinkedBinaryTree().Node("15-0")
    n15_0 = n0_0.right
    n0_0.left = LinkedBinaryTree().Node("0-15")

    n0_15 = n0_0.left
    n15_0.right = LinkedBinaryTree().Node("30-0")
    n30_0 = n15_0.right 
    n15_0.left = LinkedBinaryTree().Node("15-15")

    n15_15 = n15_0.left
    n0_15.right = n15_15
    n0_15.left = LinkedBinaryTree().Node("0-30")
    n0_30 = n0_15.left

    n30_0.right = LinkedBinaryTree().Node("40-0")
    n40_0 = n30_0.right
    n30_0.left = LinkedBinaryTree().Node("30-15")
    n30_15 = n30_0.left
    n15_15.right = n30_15

    n15_15.left = LinkedBinaryTree().Node("15-30")
    n15_30 = n15_15.left
    n0_30.right = n15_30
    n0_30.left = LinkedBinaryTree().Node("0-40")

    n0_40 = n0_30.left
    n40_0.right = win

    nWin = n40_0.right
    n40_0.left = LinkedBinaryTree().Node("40-15")
    n40_15 = n40_0.left

    n30_15.right = n40_15
    n30_15.left = LinkedBinaryTree().Node("30-30, DEUCE")
    nDeuce = n30_15.left

    n15_30.right = nDeuce
    n15_30.left = LinkedBinaryTree().Node("15-40")
    n15_40 = n15_30.left


    n0_40.right = n15_40
    n0_40.left = lose

    n40_15.left = win
    n40_15.right = LinkedBinaryTree().Node("40-30, A1")
    nA_1 = n40_15.right
    nA_1 = n40_15.right

    nDeuce.right = LinkedBinaryTree().Node("40-30, A1") #player 1 advantange
    nDeuce.left = LinkedBinaryTree().Node("30-40, A2")
    nA_2 = nDeuce.left

    n15_40.right = nA_2
    n15_40.left = nLose

    nA_1.right = win

    nA_2.right = nDeuce
    nA_2.left = LinkedBinaryTree.Node("WIN")
    
    return 

# tree = LinkedBinaryTree()
#weights are implicit
#right pointer means p
#left pointer means 1-p
