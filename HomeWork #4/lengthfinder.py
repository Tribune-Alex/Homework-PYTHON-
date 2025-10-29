print("This soft will find the longest word in your sentence")


sentence = input("Enter the sentence:")
words = sentence.split()  

longest_word = ""  
max_length = 0  

for word in words:
    if len(word) > max_length:  
        max_length = len(word)
        longest_word = word

print(f"The longest word is: {longest_word}")
