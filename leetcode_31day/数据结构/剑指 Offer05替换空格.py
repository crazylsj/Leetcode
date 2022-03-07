# 输入：s = "We are happy."
# 输出："We%20are%20happy."

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for s_data in s:
            if s_data ==" ":
                res.append("%20")
            else:
                res.append(s_data)
        return "".join(res)




