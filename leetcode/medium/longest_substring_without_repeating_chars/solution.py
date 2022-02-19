class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_s = ''
        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                subs = s[i:j]
                is_unique = self.is_unique(subs)
                if is_unique:
                    if len(subs) > len(temp_s):
                        temp_s = subs
                        
                        
        return len(temp_s)
                
                
                
    def is_unique(self, s):
        memo = {}
        for i in s:
            if not i in memo:
                memo[i] = 1
            else:
                memo[i] += 1
                
            if memo[i] > 1:
                return False
            
        return True
        


def longestUniqueSubsttr(str):
     
    n = len(str)
     
    # Result
    res = 0
  
    for i in range(n):
          
        # Note : Default values in
        # visited are false
        visited = [0] * 256  
  
        for j in range(i, n):
  
            # If current character is visited
            # Break the loop
            if (visited[ord(str[j])] == True):
                break
  
            # Else update the result if
            # this window is larger, and mark
            # current character as visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(str[j])] = True
             
        # Remove the first character of previous
        # window
        visited[ord(str[i])] = False
     
    return res