class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        
        wordCount= 1
        word= ""
        cSkip= False
        
        for c in sentence:
            if c == " ":
                wordCount +=1
                word= ""
                cSkip= False
                continue
                
            if cSkip is True:
                continue
            else:
                word+= c
                
            if len(word) == len(searchWord):
                # print(word, wordCount)
                cSkip = True
                
                if word == searchWord:
                    return wordCount
                
        else:
            return -1
            
            
            


