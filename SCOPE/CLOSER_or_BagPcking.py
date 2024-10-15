def one(x):
    def two(z):
        for i in range(x+1):
            print(i,"X",z,"=",i*z)
        return 
    return two
v=one(10)
i=one(2)
print(v)
print(i)
# print(v(3))
print(v(3))

#factory function


