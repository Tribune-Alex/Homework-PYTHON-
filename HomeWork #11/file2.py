import string

def soft1(file, word):
    
    count=0
    try:
        file= open('test.txt','r')
        line=file.read().strip(string.punctuation).lower().split()
        for i in line:
          words = i
          count += words.count(word)
        
    finally:
        file.close()
        return f"Word [{word}] meets {count} times in file" 
    
print(soft1('test.txt',word=input("Enter word to find in file: ").lower().strip(string.punctuation)))
    