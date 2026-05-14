class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
        ")":"(",
        "]":"[",
        "}":"{"
        }
        
        queue = []
        
        for i in s:
            if queue and queue[-1] == brackets.get(i, 0):
                queue.pop()
            else:
                queue.append(i)
                
        return False if queue else True
        