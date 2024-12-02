class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        
        words= sentence.split()
        for i,word in enumerate(words, 1):

            if len(word) >= len(searchWord):
                if searchWord == word[0:len(searchWord)]:
                    return i
        else:
            return -1


