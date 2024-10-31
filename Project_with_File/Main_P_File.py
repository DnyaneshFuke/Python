import json

def Load_Data():
    try:
        with open("videos.txt","r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        return []
def Helper_Save_Data(videos):
    with open("videos.txt","w") as file:
        json.dump(videos,file)

def Lst_Video(videos):
    print()
    print("*"*50)
    for index ,video in enumerate(videos,start=1):
        print(f"{index} : {video['Name']}  {video['Time']}\n")
    print("*"*50)
def Add_Video(videos):
    name = input("Enter the Name of the Video: ")
    time = input("Enter the Time of the Video: ")
    videos.append({"Name":name,"Time":time})
    Helper_Save_Data(videos)
    
def Update_Video(videos):
    Lst_Video(videos)
    index = int(input("Enter the index of the video: "))
    if 1<=index<=len(videos):
        name = input("Enter the Name of the Video: ")
        time = input("Enter the Time of the Video: ")
        videos[index-1] = {"Name":name,"Time":time}
        Helper_Save_Data(videos)
    else:
        print("Invalid Index")    
    
def Delete_Video(videos):
    Lst_Video(videos)
    index = int(input("Enter the index of the video: "))
    if 1<=index<=len(videos):
        Del=videos[index-1]
        del videos[index-1]
        print()
        Helper_Save_Data(videos)
        
        print("\nThe video is deleted:",Del['Name'])
        print("\n After deletion")
        Lst_Video(videos)
    
    else:
        print("Invalid Index")
        

def main():
    videos =Load_Data()
    while True:
        # print(videos)
        print("Youtube Manager | ")
        print("Choose an option:\n1-List_ALL_Video\n2-Add_Video\n3-Update_Video\n4-Delete_Video\n5-Exit_App\n")
        ch=input("Enter the Choise: ")
       
        match ch:
            case "1":
                Lst_Video(videos)
            case "2":
                Add_Video(videos)
            case "3":
                Update_Video(videos)
            case "4":
                Delete_Video(videos)
            case "5":
                print("Exit_App")
                break
            case _:
                print("Invalid Choise")

if __name__ =="__main__":
    main()