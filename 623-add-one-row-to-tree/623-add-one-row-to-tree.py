# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

#         dq = deque()
#         dq.append(root)
#         level = 1
#         while level < d - 1:
#             n = len(dq)
#             for _ in range(n):
#                 curr = dq.popleft()
#                 if curr.left:
#                     dq.append(curr.left)
#                 if curr.right:
#                     dq.append(curr.right)
#             level += 1

#         for _ in range(len(dq)):
#             curr = dq.popleft()

#             left = curr.left
#             right = curr.right

#             new1 = TreeNode(v)
#             new2 = TreeNode(v)

#             curr.left = new1
#             new1.left = left

#             curr.right = new2
#             new2.right = right

#         return root

 

        d = 1
        level = deque([root])
        while d < depth - 1:
            n = len(level)
            for _ in range(n):
                node = level.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            d += 1
            
        for node in level:
            left = node.left
            newNodeL = TreeNode(val, left, None)
            node.left = newNodeL


            right = node.right
            newNodeR = TreeNode(val, None, right)
            node.right = newNodeR

        return root
                
                
        
        