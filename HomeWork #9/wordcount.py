def samewords(*args):
     args=input("Enter the text please:  ").strip().lower()
     words= args.split()
     count1={}
     for i in words:
          if i in count1:
               count1[i] += 1
          else:
               count1[i] = 1

     print(count1)

samewords()
     
    
