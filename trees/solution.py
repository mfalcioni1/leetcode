# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def insert(temp,data):
    que = []
    que.append(temp)
    while (len(que)):
        temp = que[0]
        que.pop(0)
        if (not temp.left):
            temp.left = TreeNode(data)
            break
        else:
            que.append(temp.left)
        if (not temp.right):
            temp.right = TreeNode(data)
            break
        else:
            que.append(temp.right)

def make_tree(elements):
    Tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert(Tree, element)
    
    return Tree

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        subtree = []
        node = root
        while node or subtree:
            while node:
                if node.val != None:
                    traversal.append(node.val)
                subtree.append(node)
                node = node.left
            temp = subtree[-1]
            subtree.pop()
            if temp.right:
                node = temp.right
        return traversal

tree = make_tree([1, None, 2, 3])
traversal = Solution()
traversal.preorderTraversal(tree)