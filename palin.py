def palin():  #to check whether the first word is a Palindrome
    word=input('enter the word\n')
    word=word.lower().strip().split(' ')
    word=word[0]
    print(word)
    for j in range(len(word)):
         if word[j]!=word[-1-j]:        
            return False
    return True

print(palin())