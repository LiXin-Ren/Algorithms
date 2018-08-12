# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return ''
        return self.SerializeCore(root)

    def SerializeCore(self, root):
        if not root:
            return '$,'
        s = str(root.val) + ','
        left = self.SerializeCore(root.left)
        right = self.SerializeCore(root.right)
        s += left + right
        return s

    def Deserialize(self, s):
        self.flag += 1
        # write code here
        l = s.split(',')
        if len(l) <= 0 or l[0] == '$':
            return None
        root = None
        if l[self.flag] != '$':
            root = int(s[self.flag])
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

s = Solution()
print(s.Serialize())