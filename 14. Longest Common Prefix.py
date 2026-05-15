class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=strs[1]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return " "
        return prefix

        """
        :type strs: List[str]
        :rtype: str
        """
        