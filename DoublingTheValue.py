class Solution:
    def solve(self, b: int, arr: list[int]) -> int:
        # code here
        for i in arr:
            if i==b:
                b=b*2
        return b    
