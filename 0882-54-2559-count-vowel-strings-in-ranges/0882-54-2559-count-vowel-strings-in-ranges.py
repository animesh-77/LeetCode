class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowelWordCount= [0 for i in words]

        if words[0][0] in ("a", "e", "i", "o", "u") and words[0][-1] in ("a", "e", "i", "o", "u"):
            vowelWordCount[0] += 1

        for i, word in enumerate(words[1:], 1):
            if word[0] in ("a", "e", "i", "o", "u") and word[-1] in ("a", "e", "i", "o", "u"):
                vowelWordCount[i] = vowelWordCount[i-1] + 1
            else:
                vowelWordCount[i] = vowelWordCount[i-1]
        # print(vowelWordCount)

        ret= []
        for query in queries:
            left, right= query[0], query[1]

            beforeLeft= 0 if left==0 else vowelWordCount[left-1]
            tillRight= vowelWordCount[right]
            # total= tillRight- 
            ret.append(tillRight- beforeLeft)

        return ret