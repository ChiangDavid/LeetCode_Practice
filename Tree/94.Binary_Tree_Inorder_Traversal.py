# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Iterative solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Need to create the result list and stack (LIFO)
        result = []
        stack = []
        #need the value points to current node
        curr = root
        #Make sure curr or stack is not null, so we can move on
        while curr or stack:
            #Make sure curr is not null so we can traverse the node
            while curr:
                #Append the node to the stack
                stack.append(curr)
                #To the left first, until meet null
                curr = curr.left
            #If we meet the curr is null, we need to pop the last value 
            curr = stack.pop()
            #After pop, we need to append to the reuslt list to return
            result.append(curr.val)
            #After traverse to left, we need to go right
            curr = curr.right
        return result

  #Recursion:
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res
