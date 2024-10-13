N=int(input("Enter the number To print Table:\n"))
for i in range(1,11):
    if i ==5:
        continue
    print(N,"X",i,"=",N*i)