sentence=input("Input the sentences:")
sentenceedit=sentence.split()
print("Now input the word which will change ther first word in your sentence")
word=input("Input the  word:")
sentenceedit[0]=word

end =" ".join(sentenceedit)

print(end)




