class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        all_words= sentence.split()
        
        if all_words[0][0] != all_words[-1][-1]:
            return False
        
        for word1, word2 in zip(all_words[:-1], all_words[1:]):
            if word1[-1] != word2[0]:
                return False
            
        return True
            
        