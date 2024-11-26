class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusted_people= [0]*(n+1)
        trusts_people= [0]*(n+1)
        
        
        for p1, t1 in trust:
            
            trusted_people[t1] += 1
            trusts_people[p1] += 1
            
        for i in range(1, n+1):
            if trusted_people[i] == n-1 and trusts_people[i] == 0:
                return i
        else:
            return -1