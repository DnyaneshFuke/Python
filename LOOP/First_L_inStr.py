str=str(input("Enter the String:"))

for i in str:
    print (i)
    if str.count(i) ==1:
        print("the non-repeating char is:",i)
        break
