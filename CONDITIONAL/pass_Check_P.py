pss=str(input("Enter the pass"))
if len(pss)<6:
        print("Weak password")
        pss()
elif len(pss)<10:
        print("Medium password")
        pss()
else:
        print("Strong password")