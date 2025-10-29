
def text_one(sentence):
    upper_count=0
    upper_text=sentence.upper()
    for i in sentence:
        if i.isupper():
            upper_count+=1
    print(f"There are {upper_count} capital letters in your text")
    print(f"This is your text with all capital letters: {upper_text}")
    
while True:
 text_one(sentence=input("Please enter your text: "))


    