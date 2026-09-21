class Solution:
    def remConsonants(self, s):
        # code here
        str=""
        for i in s:
            if i in "aAeEiIoOuU":
                str=str+i
        return str   
