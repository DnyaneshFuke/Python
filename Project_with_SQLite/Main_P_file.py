import sqlite3
from prettytable import PrettyTable
con =sqlite3.connect('Youtube_DB.db')
cur=con.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS video (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Correctly defined as an auto-incrementing integer primary key
    Name TEXT,
    Time TEXT
)''')

def List_ALL_Video():
    cur.execute("Select * from video")
    rows=cur.fetchall()
    table = PrettyTable(["ID", "Name", "Time"])
    for row in rows:
        table.add_row(row)
    print(table)
def check_id_exists(ID):
    """Helper function to check if the given ID already exists in the database."""
    cur.execute("SELECT 1 FROM video WHERE ID = ?", (ID,))
    return cur.fetchone() is not None  # Returns True if ID exists, False otherwise

def Add_Video():
    ID = input("Enter the ID of the video : ")
        
    if ID.strip() == "":
        # No ID provided by the user, let SQLite auto-generate it
        Name = input("Enter the Name of the Video: ")
        Time = input("Enter the Time of the Video: ")

        # Skip ID in the insert statement so SQLite can autoincrement
        cur.execute("INSERT INTO video(Name, Time) VALUES(?, ?)", (Name, Time))
    else:
        try:
            # Try converting the input to an integer (user provided an ID)
            ID = int(ID)
            if check_id_exists(ID):
                print(f"ID {ID} already exists. Please provide a unique ID.")
                return Add_Video()
            Name = input("Enter the Name of the Video: ")
            Time = input("Enter the Time of the Video: ")

            # Insert with user-provided ID
            cur.execute("INSERT INTO video(ID, Name, Time) VALUES(?, ?, ?)", (ID, Name, Time))
        except ValueError:
            # If the input is not a valid integer, show an error and retry
            print("Invalid ID. Please enter a numeric value.")
            return Add_Video()  # Call the function again for retry

    # Commit the changes to the database
    con.commit()
print("Video added successfully.")
def Update_Video():
    List_ALL_Video()
    ID = int(input("Enter the ID of the video: "))
    Name = input("Enter the Name of the Video: ")
    Time = input("Enter the Time of the Video: ")
    cur.execute("UPDATE video SET Name=?,Time=? WHERE ID=?",(Name,Time,ID))
    con.commit()
def Delete_Video():
    List_ALL_Video()
    ID = int(input("Enter the ID of the video: "))
    cur.execute("DELETE FROM video WHERE ID=?",(ID,))
    con.commit()
def Delet_ALL():
    #cur.execute("Drop Table video")
    #con.commit()
    pass
def main():
    while True:
        print("Youtube Manager | ")
        print("Choose an option:\n1-List_ALL_Video\n2-Add_Video\n3-Update_Video\n4-Delete_Video\n5-Delet_All\n6-Exit_App\n")
        ch=input("Enter the Choise: ")
        match ch:
            case "1":
                List_ALL_Video()
            case "2":
                Add_Video()
            case "3":
                Update_Video()
            case "4":
                Delete_Video()
            case "5":
                Delet_ALL()
            case "6":
                print("Exit_App")
                break
            case _:
                print("Invalid Choise")
    con.close()

if __name__ =="__main__":
    main()

