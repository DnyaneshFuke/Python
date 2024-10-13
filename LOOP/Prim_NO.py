

def prim(num):
    for i in range(2, int(num ** 0.5) + 1):  
            if num % i != 0:
                continue
            else:
                return False
    # print(num)
    return True            
num=int(input("Enter the upto which u want prim NO:"))
print(f"Prime numbers up to {num}:")
for num in range(1, num + 1):  # Start from 2 to the upper limit
    if prim(num):  # Check if the current number is prime
     print(num)   