class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
    
        for word in strs:
            key = "".join(sorted(word))
            
            if not words.get(key):
                words[key] = [word] 
            else:
                words[key].append(word) 
            
        return list(words.values())