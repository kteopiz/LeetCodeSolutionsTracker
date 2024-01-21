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

def inorder_traversal(root):
    l = []
    if root:
        l += inorder_traversal(root.left)
        l += [root.val]
        l += inorder_traversal(root.right)
    return l

def symmetric_tree(root):
    def dfs(left, right):
        if not left and not right:
            return True
        # If we make it this far, we know at least ONE node exists.
        # We can just do or
        if not left or not right:
            return False
        # 3 conditions must return true:
            # 1) vals at these nodes must be equal
            # 2) and 3) the values from all nodes of the subtrees must be True also
        return ((left.val == right.val) and dfs(left.right, right.left) and dfs(left.left, right.right))
    return dfs(root.left, root.right)



if __name__ == "__main__":
   pass