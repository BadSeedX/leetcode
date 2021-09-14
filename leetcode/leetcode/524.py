class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        # 双指针
        l = 0
        pos = ""
        for idx in dictionary:
            i = 0 
            j = 0
            while(i<len(idx) and j<len(s)):
                if idx[i] == s[j]:
                    i+=1
                j+=1
            if i == len(idx) and l<=len(idx):
                if l == len(idx):
                    pos=min(pos,idx)
                else:
                    l = len(idx)
                    pos = idx
        return pos
