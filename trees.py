class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         val = val
         left = left
         right = right

def max_depth_binary_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    result = 1
    # Base Case -> If the node we are at has no children, this is our last count
    if root.left is None and root.right is None:
        return result
    
    # Need to follow the longest path, this is the one with an existing child:
    # If either child DNE, follow where the child does exist
    elif root.left is None:
        return result + max_depth_binary_tree(root.right)
    elif root.right is None:
        return result + max_depth_binary_tree(root.left)
    
    # If both children exist, follow both paths saving their depth, keep the greatest one
    else:
        left_child = result + max_depth_binary_tree(root.left)
        right_child = result + max_depth_binary_tree(root.right)

        if left_child > right_child:
            return left_child
        else:
            return right_child

def same_tree(p,q):
    def preorder(root, traversal):
        if root:
            traversal = str(root.val)
            traversal += preorder(root.left, traversal)
            traversal += preorder(root.right, traversal)
        return traversal

    first = preorder(p,"")
    second = preorder(q,"")

    return first == second



if __name__ == "__main__":
   pass