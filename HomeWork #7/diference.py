

word1=input("Enter the first word: ")
word2=input("Enter the second word: ")

set1=set(word1)
set2=set(word2)

print("Difference between your words: ",set1.difference(set2))
print("Common in your words: ",set1.intersection(set2))
print("Two words symbols together: ",set1.union(set2))

