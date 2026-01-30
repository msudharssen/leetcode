def subsequenceFinder(s: str, words:list):
    
    res = 0
    for word in words:
        firstPointer = 0
        secondPointer=0
        while firstPointer < len(s) and secondPointer < len(word):
            if s[firstPointer]==word[secondPointer]:
                secondPointer+=1
            firstPointer+=1
        if secondPointer==len(word):
            res+=1
    return res

print(subsequenceFinder("abcde", ["a", "bb", "acd", "ace"]))
        
