print("This soft will help you to find out, are the words you choose are anagram")

word1= input("Input first word:").lower()
word2=input("Input second word:").lower()

count1={}
count2={}



for char in word1:
        count1[char]=count1.get(char,0)+1


for char in word2:
        count2[char]=count2.get(char,0)+1


if count1==count2:
    print(f"{word1} and {word2} are anagram")
    
else:
    print(f"{word1} and {word2} are not anagram")
    
    

    
         



         

        



