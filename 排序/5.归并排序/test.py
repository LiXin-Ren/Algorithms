# -*- coding:utf-8 -*-
import re
class Solution:
    class Solution:
        # s字符串
        def isNumeric(self, s):
            # write code here
            if s.startswith('+') or s.startswith('-'):  #去除正负号
                s = s[1:]
            if re.match('^\d', s):
                


sod = Solution()

print(sod.isNumeric("", ".*"))
