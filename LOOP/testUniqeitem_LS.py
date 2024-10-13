
n=int(input("Enter this size of item list"))
it=[n]
for i in range(n):
      item = input(f"Enter item {i + 1}: ")  # Prompt user for item
      it.append(item) 
    
UI=set()
for i  in it:
    if i in UI:
        print("Duplicate Item:",i)
        break 
    UI.add(i)