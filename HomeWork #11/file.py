def soft(test):
    file = open(test, 'r')
    try:
         lines = file.readlines()
         total = 0
         word = 0
         for i in lines:
           count1 = lines.count(i)
           total += count1
           longest = max(lines, key=len)
           word += len(i.strip())
    finally:
        file.close()

        return f"The are {total} lines in file", f"The longest line in file is: {longest}",f"The are {word} characters in  file"

print(soft('test.txt'))