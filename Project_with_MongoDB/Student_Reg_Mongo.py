from pymongo import MongoClient

url = "mongodb+srv://Youtubepy:Pass123@cluster1yt.e0u2s.mongodb.net/"
client = MongoClient(url)
db = client['Register']
collection = db['Student_Register']

def stud_reg():
    Name=input("Enter the Name of Student:")
    Age=input("Enter the Age:")
    Branch=input("Enter the Branch:")
    Dep=input("Enter the Department:")
    Stud={"Name":Name,"Age":Age,"Branch":Branch,"Department":Dep}
    collection.insert_one(Stud)
    print("Enter Detail Successful")
def 
def main():
    while True:
        print("1-Register_student")
        print("2-Update_student")
        print("3-Delete_student")
        print("4-All_student")
        print("5-All_department")
        ch=input("Enter your choise:")
        match ch:
            case"1":
                stud_reg()
            case"2":
                stud_updt()
            case"3":
                pass
            case"4":
                pass
            case"5":
                pass
            case"6":
                print("Exit the app")
                break
            case _:
                print("Invalid Chosie:")

if __name__=="__main__":
    main()