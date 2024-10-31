from pymongo import MongoClient
from bson.objectid import ObjectId

url = "mongodb+srv://Youtubepy:Pass123@cluster1yt.e0u2s.mongodb.net/"
client = MongoClient(url)
db = client['Youtube']
collection = db['Youtube_Video']

def Add_Video():
    name = input("Enter the Name of the Video: ")
    time = input("Enter the Time of the Video: ")
    video = {"Name": name, "Time": time}
    collection.insert_one(video)
    print("Video added successfully.")

def delete_video():
    _id = input("Enter the ID of the video you want to delete: ")
    try:
        collection.delete_one({"_id": ObjectId(_id)})
        print(f"The video with ID {_id} is deleted.")
    except Exception as e:
        print(f"Error: {e}. Make sure the ID is correct.")

def update_video():
    _id = input("Enter the ID of the video you want to update: ")
    try:
        video = collection.find_one({"_id": ObjectId(_id)})
        if video:
            print(f"Current details - Name: {video['Name']}, Time: {video['Time']}")
            name = input("Enter the new Name of the Video: ")
            time = input("Enter the new Time of the Video: ")
            collection.update_one({"_id": ObjectId(_id)}, {"$set": {"Name": name, "Time": time}})
            print("Video updated successfully.")
        else:
            print("Invalid ID. Video not found.")
    except Exception as e:
        print(f"Error: {e}. Make sure the ID is correct.")

def main():
    while True:
        print("\nYoutube Manager | Choose an option:")
        print("1- List All Videos")
        print("2- Add Video")
        print("3- Update Video")
        print("4- Delete Video")
        print("5- Exit App")

        ch = input("Enter your choice: ")
        
        if ch == "1":
            for video in collection.find():
                print(f"ID: {video['_id']} -- Name: {video['Name']}, Time: {video['Time']}")
        elif ch == "2":
            Add_Video()
        elif ch == "3":
            update_video()
        elif ch == "4":
            delete_video()
        elif ch == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
