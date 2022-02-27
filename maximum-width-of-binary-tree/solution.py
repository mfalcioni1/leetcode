from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)

# Function to build a binary tree from the given parent list
def createTree(parent, root, i, n):
    if i < n:
        temp = TreeNode(parent[i])
        root = temp

        # left nodes are odd numbers in the array due to 0 index
        root.left = createTree(parent, root.left, 2 * i + 1, n)

        # right nodes are even numbers in the array
        root.right = createTree(parent, root.right, 2 * (i + 1), n)
    
    return root

# Return Tree as a dictionary
def treeToDict(root, i, d):
    if root != None:
        i += 1
        d = treeToDict(root.left, i, d)
        if i in d:
            d[i].append(root.val)
        else:
            d[i] = [root.val]
        d = treeToDict(root.right, i , d)
    else:
        i += 1
        if i in d:
            d[i].append(root)
    return d

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        d = treeToDict(root, i=0, d={})
        width = 0
        for key in d:
            if d[key][len(d[key])-1] != None:
                if width < len(d[key]):
                    width = len(d[key])
            
        return width

parent = [1, 3, 2, 5, 3, None, 9]
n = len(parent)
root = None
ex_1 = createTree(parent, tree=root, i=0, n=n)
res = treeToDict(ex_1, 0, d={})
parent = [1,3,2,5,None,None,9,6,None,None,7]
n = len(parent)
root = None
ex_2 = createTree(parent, tree=root, i=0, n=n)
res = treeToDict(ex_2, 0, d={})

sol = Solution()
sol.widthOfBinaryTree(ex_1) # 4
sol.widthOfBinaryTree(ex_2) # 8

