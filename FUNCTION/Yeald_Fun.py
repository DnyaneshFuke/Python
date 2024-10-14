def generator(l):
    for i in range(2,l+1,2):
        yield i

for i in generator(10):
    print(i)